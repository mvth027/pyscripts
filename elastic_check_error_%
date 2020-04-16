
import argparse
import sys
import time
import requests
from datetime import timedelta, datetime
from pytz import UTC
from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser()
parser.add_argument('-host',   help='elasticsearch host')
parser.add_argument('-index',  help='index prefix before timestamp')
parser.add_argument('-period', help='The period of analysis in minutes', type=int)
args = parser.parse_args()

def calculate_datetime_values():
    now_utc = datetime.now(tz=UTC)
    # выравниваем по дату так, чтоб после minute были нули т.е. целая минута
    now_utc_truncated = now_utc.replace(microsecond=0, second=0)
    # считаем значения окон из опций
    time_shift = timedelta(minutes=1)
    time_window = timedelta(minutes=int(args.period))
    # считаем конечные значения, чтоб потом вставить их в фильтр по времени
    to_date = now_utc_truncated - time_shift
    from_date = now_utc_truncated - ( time_shift + time_window )
    return (to_date, from_date)

match_all= {"match_all" : {} }

match_error= {"query_string" : {"query" : "response_body: ( \\\"FAILURE\\\" , \\\"TIMEOUT\\\")"}}


def do_search(from_date,to_date,match):
	conn_timeout = 2
	socket_read_timeout = 180
	request_template = {
    "size": 0,
    "query": {
        "bool": {
            "must":[
            match
            ],
            "filter": {
                "range" : {
                    "@timestamp" : {
                        "gte" :  "{}".format(from_date),
                        "lte"  : "{}".format(to_date)
                    }
                }
            }
        }
    }
}
	url= args.host
	index = args.index
	es = Elasticsearch(url)
	response = es.search(index=index, body=request_template, request_timeout=30)
	count = response['hits']['total']['value']
	return count


all_requests_count = do_search(str(calculate_datetime_values()[1].isoformat()),str(calculate_datetime_values()[0].isoformat()),match_all)
error_requests_count = do_search(str(calculate_datetime_values()[1].isoformat()),str(calculate_datetime_values()[0].isoformat()),match_error)

def do_check(all,error):
	percent = error/all
	message = []
	if percent >= 0.01:
		message = """WARNING! Error count in last {} minutes is over 1%.
All requests: {}
Failed/Timout: {}
Percentage: {} %
Interval: {} UTC to {} UTC
		""".format(args.period,all,error,percent,calculate_datetime_values()[1],calculate_datetime_values()[0])
		
	elif percent < 0.01:
		message = """OK. Error count in last {} minutes is less than 1%.
All requests: {}
Failed/Timout: {}
Percentage: {} %
Interval: {} UTC to {} UTC
		""".format(args.period,all,error,percent,calculate_datetime_values()[1],calculate_datetime_values()[0])
		
	else:
		message = "unknown"
		
	return message, percent


print (do_check(all_requests_count,error_requests_count)[0])
if float(do_check(all_requests_count,error_requests_count)[1]) >= 0.01:
	sys.exit(1)
else:
	sys.exit(0)

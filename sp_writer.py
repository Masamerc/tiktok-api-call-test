import pygsheets
import pandas as pd

from tonton_utils.args import parse_query_into_args
from tonton_utils.get_records import get


def parse_response(resp):
    data = resp["data"]["list"]
    return [{**datum["dimensions"], **datum["metrics"]} for datum in data]



resp_json = get(args.json())


df = pd.DataFrame(parse(resp_json))


#authorization
gc = pygsheets.authorize(service_file='./tonton-spresheet-writer-47d76649c954.json')


#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('testsheet')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))
import pygsheets
import pandas as pd

from tonton_utils.args import parse_query_into_args
from tonton_utils.errors import RequestFailure
from tonton_utils.get_records import get


def parse_response(resp):
    data = resp["data"]["list"]
    return [{**datum["dimensions"], **datum["metrics"]} for datum in data]


args = parse_query_into_args()
resp_json = get(args.json())

try:
    df = pd.DataFrame(parse_response(resp_json))
except KeyError:
    raise RequestFailure(f"error in request: {resp_json}")


def write_to_googlesheet():
    #authorization
    gc = pygsheets.authorize(service_file='./tonton-spresheet-writer-47d76649c954.json')
    #open the google spreadsheet
    sh = gc.open('testsheet')
    #select the first sheet 
    wks = sh[0]
    #update the first sheet with df, starting at cell B2. 
    wks.set_dataframe(df,(1,1))
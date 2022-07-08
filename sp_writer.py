import pygsheets
import pandas as pd

from get_records import Args, get

def parse(resp):
    data = resp["data"]["list"]
    return [{**datum["dimensions"], **datum["metrics"]} for datum in data]


args = Args(
        metrics=["impressions"],
        data_level="AUCTION_CAMPAIGN",
        advertiser_id="7062557572875763714",
        service_type="AUCTION",
        lifetime="true",
        report_type="BASIC",
        dimensions=["campaign_id"]
    )


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
# coding=utf-8
import json
import requests

from dataclasses import dataclass, asdict
from six import string_types
from typing import List, Optional
from urllib.parse import urlencode, urlunparse  # noqa

from secrets import TOKEN


ACCESS_TOKEN = TOKEN
PATH = "/open_api/v1.2/reports/integrated/get/"


def build_url(path, query=""):
    # type: (str, str) -> str
    """
    Build request URL
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """
    scheme, netloc = "https", "business-api.tiktok.com"
    return urlunparse((scheme, netloc, path, "", query, ""))

def get(json_str):
    # type: (str) -> dict
    """
    Send GET request
    :param json_str: Args in JSON format
    :return: Response in JSON format
    """
    args = json.loads(json_str)
    query_string = urlencode({k: v if isinstance(v, string_types) else json.dumps(v) for k, v in args.items()})
    url = build_url(PATH, query_string)
    headers = {
        "Access-Token": ACCESS_TOKEN,
    }
    rsp = requests.get(url, headers=headers)
    return rsp.json()


@dataclass
class Filter:
    filter_value: str
    field_name: str
    filter_type: str


@dataclass
class Args:
    metrics: List[str] = None
    data_level: str = None
    end_date: Optional[str] = None
    order_type: Optional[str] = None
    order_field: Optional[str] = None
    page_size: Optional[int] = None
    start_date: Optional[str] = None
    advertiser_id: str = None
    filters: Optional[List[Filter]] = None
    field_name: Optional[str] = None
    filter_type: Optional[str] = None
    service_type: str = None
    lifetime: bool = None
    report_type: str = None
    page: Optional[int] = None
    dimensions: List[str] = None

    def get_args(self):
        all_attrs = asdict(self)
        return {original_key: all_attrs[original_key] for original_key in all_attrs.keys()\
             if all_attrs[original_key] is not None}
    
    def json(self):
        return json.dumps(self.get_args())





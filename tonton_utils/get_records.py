# coding=utf-8
import json
import requests

from six import string_types
from urllib.parse import urlencode, urlunparse

from config.secrets import TOKEN


ACCESS_TOKEN = TOKEN
PATH = "/open_api/v1.2/reports/integrated/get/"


def build_url(path: str, query: str="") -> str:
    """
    Build request URL
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """
    scheme, netloc = "https", "business-api.tiktok.com"
    return urlunparse((scheme, netloc, path, "", query, ""))


def get(json_str: str) -> dict:
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

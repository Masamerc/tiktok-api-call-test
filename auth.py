# coding=utf-8
import json
import requests

from six import string_types
from urllib.parse import urlencode, urlunparse  # noqa

from secrets import API_KEY, AUTH_CODE

PATH = "/open_api/v1.2/oauth2/access_token/"


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

def post(json_str):
    # type: (str) -> dict
    """
    Send POST request
    :param json_str: Args in JSON format
    :return: Response in JSON format
    """
    url = build_url(PATH)
    args = json.loads(json_str)
    headers = {
        "Content-Type": "application/json",
    }
    rsp = requests.post(url, headers=headers, json=args)
    return rsp.json()

if __name__ == '__main__':
    secret = API_KEY
    app_id = "7107453944774787074"
    auth_code = AUTH_CODE

    # Args in JSON format
    my_args = "{\"secret\": \"%s\", \"app_id\": \"%s\", \"auth_code\": \"%s\"}" % (secret, app_id, auth_code)
    print(post(my_args))
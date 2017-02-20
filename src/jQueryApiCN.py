# encoding: utf-8

from urllib import urlopen
import json
import CnDict

# api_url = 'http://www.jquery123.com/assets/js/apis.json'
# api_json_string = urlopen(api_url).read()
# api_json = json.loads(api_json_string)
cn_dict = CnDict.data


def query(api):
    d = {}
    for k in cn_dict.keys():
        b = False
        if api.lower() in k.lower():
            b = True
        if b:
            d[k] = cn_dict[k]

    return d

# encoding: utf-8

from urllib import urlopen
from workflow import web, Workflow
import util
from bs4 import BeautifulSoup as Soup

# cn_dict = CnDict.data
wf = Workflow()
cache_max_age = 15811200  # s


def query(api):
    d = {}
    cn_dict = wf.cached_data('workflow_jquery_api_cn_all', get_api_data, max_age=cache_max_age)
    for k in cn_dict.keys():
        if api.lower() in k.lower():
            desc = get_api_desc(k)
            if desc is not None:
                d[k] = desc
    return d


def get_api_data():
    api_json = web.get(util.api_url).json()
    d = {}
    for api in api_json:
        d[api[api.keys()[0]]] = api[api.keys()[1]]
    return d


def get_api_desc(api):
    api_link = util.get_link(api)
    desc = wf.cached_data('workflow_jquery_api_cn_' + api)
    if desc is None:
        def api_desc():
            resp = web.get(api_link)
            s = None
            if resp.status_code == 200:
                soup = Soup(resp.text, "html.parser")
                s = soup.select('.entry-wrapper > p.desc')[0].get_text()
                s = s[s.find(':') + 1:len(s)].strip()
            else:
                print 'resp.status_code %d' % resp.status_code
            return s

        desc = wf.cached_data('workflow_jquery_api_cn_' + api, api_desc, max_age=cache_max_age)  # half a year

    return desc

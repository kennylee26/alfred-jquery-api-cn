# encoding: utf-8

from workflow import web, Workflow
import util
from bs4 import BeautifulSoup as Soup

GITHUB_UPDATE_CONF = {'github_slug': 'kennylee26/alfred-jquery-api-cn'}

wf = Workflow(update_settings=GITHUB_UPDATE_CONF)
cache_max_age = 3600  # a day


def query(api):
    d = {}
    cn_dict = wf.cached_data('workflow_jquery_api_cn_all', get_api_dict, max_age=cache_max_age)
    for k in cn_dict.keys():
        if api.lower() in k.lower():
            desc = cn_dict[k]
            if desc is not None:
                d[k] = desc
    return d


def get_api_dict():
    s = web.get(util.base_url).text
    soup = Soup(s, "html.parser")
    articles = soup.select('article')
    d = {}
    for art in articles:
        title = art.select('.entry-title > a')[0]['href']
        if title not in d:
            title = title[0:len(title) - 1]
            desc = art.select('.entry-summary')[0].get_text().strip()
            d[title] = unicode(desc)
        else:
            print "existed key %s" % title
    return d

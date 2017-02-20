# encoding: utf-8

from workflow import web, ICON_INFO
import util
from bs4 import BeautifulSoup as Soup
from workflow.background import run_in_background, is_running


def query(api):
    d = {}
    cn_dict = get_jquery_api_dict()
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


def update_cache(wf):
    # Is cache over 1 hour old or non-existent?
    if not wf.cached_data_fresh(util.cache_name, util.cache_max_age):
        run_in_background(u'update_jquery_api_cn',
                          ['/usr/bin/python',
                           wf.workflowfile('update_dict.py')])

    # Add a notification if the script is running
    if is_running(u'update_jquery_api_cn'):
        wf.add_item(u'正在更新API缓存...', icon=ICON_INFO)


def get_jquery_api_dict():
    wf = util.get_wf()
    s = util.cache_name

    if wf.first_run:
        d = wf.cached_data(s, get_api_dict, max_age=util.cache_max_age)
    else:
        update_cache(wf)
        # max_age=0 will return the cached data regardless of age
        d = wf.cached_data(s, max_age=0)
    return d



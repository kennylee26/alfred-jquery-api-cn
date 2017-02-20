# encoding: utf-8
from workflow import Workflow

base_url = 'http://www.jquery123.com/'
GITHUB_UPDATE_CONF = {'github_slug': 'kennylee26/alfred-jquery-api-cn'}
cache_name = '__workflow_jquery_api_cn_dict'
cache_max_age = 3600  # 1 hours


def get_link(api_name):
    name = api_name
    if api_name.startswith('.'):
        name = api_name[1:len(api_name)]
    return base_url + name


def get_wf():
    return Workflow(update_settings=GITHUB_UPDATE_CONF)


def clear_all():
    wf = get_wf()
    wf.clear_cache()

# encoding: utf-8

base_url = 'http://www.jquery123.com/'
api_url = base_url + '/assets/js/apis.json'


def get_link(api_name):
    name = api_name
    if api_name.startswith('.'):
        name = api_name[1:len(api_name)]
    return base_url + name
# encoding: utf-8

import jQueryApiCN
import unittest

util = jQueryApiCN.util
web = jQueryApiCN.web
Soup = jQueryApiCN.Soup

api_url = util.base_url + '/assets/js/apis.json'


def get_api_data():
    api_json = web.get(api_url).json()
    d = {}
    for api in api_json:
        d[api[api.keys()[0]]] = api[api.keys()[1]]
    return d


def get_api_desc(api):
    api_link = util.get_link(api)
    resp = web.get(api_link)
    s = None
    if resp.status_code == 200:
        soup = Soup(resp.text, "html.parser")
        s = soup.select('.entry-wrapper > p.desc')[0].get_text()
        s = s[s.find(':') + 1:len(s)].strip()
    else:
        print 'resp.status_code %d' % resp.status_code
    return s


class ApiTestCase(unittest.TestCase):
    def testInt(self):
        main_dict = jQueryApiCN.get_api_dict()
        json_dict = get_api_data()
        self.assertEqual(len(main_dict), len(json_dict))


if __name__ == '__main__':
    unittest.main()

# encoding: utf-8

import util
import jQueryApiCN


def main(wf):
    wf.cached_data(util.cache_name, jQueryApiCN.get_api_dict, max_age=util.cache_max_age)


if __name__ == '__main__':
    wf = util.get_wf()
    wf.run(main)

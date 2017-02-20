# encoding: utf-8

import sys
from workflow import Workflow

base_url = 'http://www.jquery123.com/'


def main(wf):
    import jQueryApiCN

    # Get user input
    if len(wf.args):
        user_input = wf.args[0]

        result = jQueryApiCN.query(user_input)

        if len(result) > 0:
            for x in result.keys():
                wf.add_item(unicode(x), unicode(result[x]),
                            arg=get_link(x),
                            valid=True)
        else:
            wf.add_item(
                'cant find "%s" Api.' % user_input,
                valid=False
            )
        wf.send_feedback()


def get_link(api_name):
    name = api_name
    if api_name.startswith('.'):
        name = api_name[1:len(api_name)]
    return base_url + name


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))

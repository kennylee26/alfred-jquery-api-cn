# encoding: utf-8

import sys
import util
from workflow import Workflow


def main(wf):
    import jQueryApiCN

    # Get user input
    if len(wf.args):
        user_input = wf.args[0]

        result = jQueryApiCN.query(user_input)

        if len(result) > 0:
            for x in result.keys():
                wf.add_item(unicode(x), unicode(result[x]),
                            arg=util.get_link(x),
                            valid=True)
        else:
            wf.add_item(
                u'找不到 "%s" 的Api。' % user_input,
                valid=False
            )
        wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))

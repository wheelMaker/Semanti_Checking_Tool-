#!/usr/bin/python

# Very start of the software

import Initiator

# ---------------Init staffs as below------------------------
init_agent = Initiator.Initiator()
init_agent.config_parser()
init_agent.user_option_analysis()
init_agent.config_logger()
init_agent.get_all_code_files()
init_agent.init_report()

for key in init_agent.opts():
    init_agent.logger().debug(str(key) + ': ' + str(init_agent.opts()[key]))
init_agent.logger().info('Code files to be checked are: ')
init_agent.logger().info(init_agent.code_files())
init_agent.logger().critical('******      GCS Checker Start!!!      ******')
# -----------------------------------------------------------

'''
Checking python code files here.
'''
init_agent.report().close_file()

#!/usr/bin/python

# Very start of the software

import Initiator
import GCSChecker

# ---------------Init staffs as below------------------------
init_agent = Initiator.Initiator()
init_agent.config_parser()
init_agent.user_option_analysis()
init_agent.config_logger()
init_agent.get_all_code_files()
init_agent.init_report()

logger = init_agent.logger()

for key in init_agent.opts():
    # init_agent.logger().debug(str(key) + ': ' + str(init_agent.opts()[key]))
    logger.debug(str(key) + ': ' + str(init_agent.opts()[key]))
logger.info('Code files to be checked are: ')
logger.info(init_agent.code_files())
logger.critical('******      GCS Checker Start!!!      ******')
# -----------------------------------------------------------

'''
Checking python code files here.
'''
checker = GCSChecker.GCSChecker()
# checker.get_checker_type(init_agent.code_files(), init_agent.report())


init_agent.report().close_file()

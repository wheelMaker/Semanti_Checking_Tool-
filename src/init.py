#!/usr/bin/python
'''
   Verty start of this project
'''
import logging
import logging.config
import os
from optparse import OptionParser


class GCSException(Exception):
    _error_message = ''

    def __init__(self, msg=""):
        self._error_message = msg
        print self._error_message

# ---------------Init staffs as below------------------------

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-l", "--logFile", dest="logFileName",
                  help="log will be stored in this file")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

try:
    if not options.logFileName:
        raise GCSException('Null log file name')
except GCSException:
    print "Using default log file: GCS.log"

try:
    if not options.filename:
        raise GCSException('Null GCS report file name')
except GCSException:
    print "Using default log file: GCS.report"

print 'GCS checker init'

current_path = os.getcwd()
log_file_name = current_path + '/GCS.log'

logging.config.fileConfig('logging.conf')
logging.basicConfig(level=logging.DEBUG,
                    filename=log_file_name,
                    filemode='w')

'''
Here just implement the base logging functionality. For the rest sub modules, more sub logging functionality
should be implemented separately.

Below is the logging examples:

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
'''

logging.critical('******      GCS Checker Start!!!      ******')



#os.rmdir(log_file_name)

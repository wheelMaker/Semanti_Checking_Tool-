#!/usr/bin/python
'''
   Verty start of the software
'''
import logging
import logging.config
import os
import re
import GCSException as e
from optparse import OptionParser
import file_IO
import time


def user_option_analysis(t_options):

    opt = {}
    current_path = os.getcwd()

    try:
        if not t_options.logFileName:
            raise e.GCSException('### ---- Null log file name')
    except e.GCSException:
        print "Using default log file: GCS.log\n"
        t_options.logFileName = 'GCS.log'
    opt['logFileName'] = t_options.logFileName

    try:
        if not t_options.filename:
            raise e.GCSException('### ---- Null GCS report file name')
    except e.GCSException:
        print "Using default log file: GCS.report\n"
        t_options.filename = 'GCS.report'
    opt['filename'] = t_options.filename

    try:
        if not t_options.codeDir:
            raise e.GCSException('### ---- Null source code dir')
    except e.GCSException:
        t_options.codeDir = current_path
        print "Using CWD as source code dir\n"
    opt['codeDir'] = t_options.codeDir
    return opt


def get_all_code_files(code_dir):
    f = []
    files = os.listdir(code_dir)
    for i in range(len(files)):
        result = re.match("^.*\.py$", files[i])
        if result:
            f.append(files[i])
    return f

# ---------------Init staffs as below------------------------
# --------- step 1, get all user options

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-l", "--logFile", dest="logFileName",
                  help="log will be stored in this file")
parser.add_option("-d", "--dir", dest="codeDir",
                  help="source code directory, GCS will go through all .py files in this dir")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
opts = user_option_analysis(options)

# --------- step 2, config logging module

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('Init')
fh = logging.FileHandler(opts['logFileName'])
logger.addHandler(fh)

for key, item in opts.items():
    logger.debug(str(key) + ': ' + str(item))

codeFiles = get_all_code_files(opts['codeDir'])

logger.info('Code files to be checked are: ')
logger.info(codeFiles)

# --------- step 3, prepare report file

report = file_IO.FileIO("report.txt")
report.open_file(mode='w')
current_time = time.asctime()
report.write_to_file(current_time)
report.write_to_file(' Checking code files in dir: \n')
report.write_to_file(opts['codeDir'])
report.write_to_file('\nCode files are: ')
for item in codeFiles:
    report.write_to_file('\n')
    report.write_to_file(item)

# -----------------------------------------------------------

logger.critical('******      GCS Checker Start!!!      ******')
'''
Checking python code files here.
'''
report.close_file()
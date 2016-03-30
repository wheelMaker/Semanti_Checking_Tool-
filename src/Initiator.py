import os
import re
import GCSException as GE
from optparse import OptionParser
import logging
import logging.config
import file_IO
import time


class Initiator(object):
    __opt = {}
    __code_files = []
    __parser = None
    __logger = None
    __report = None

    def __init__(self):
        print "Software initiating!!!"

    def opts(self):
        return self.__opt

    def logger(self):
        return self.__logger

    def code_files(self):
        return self.__code_files

    def report(self):
        return self.__report

    def init_report(self):
        self.__report = file_IO.FileIO(self.__opt['filename'])
        self.__report.open_file(mode='w')
        self.__report.write_to_file(time.asctime())
        self.__report.write_to_file(' Checking code files in dir: \n')
        self.__report.write_to_file(self.__opt['codeDir'])
        self.__report.write_to_file('\nCode files are: ')
        for item in self.__code_files:
            self.__report.write_to_file('\n')
            self.__report.write_to_file(item)

    def config_logger(self):
        logging.config.fileConfig('logging.conf')
        self.__logger = logging.getLogger('Init')
        fh = logging.FileHandler(self.__opt['logFileName'])
        self.__logger.addHandler(fh)

    def user_option_analysis(self):

        (options, args) = self.__parser.parse_args()
        current_path = os.getcwd()

        try:
            if not options.logFileName:
                raise GE.GCSException('### ---- Null log file name')
        except GE.GCSException:
            print "Using default log file: GCS.log\n"
            options.logFileName = 'GCS.log'
        self.__opt['logFileName'] = options.logFileName

        try:
            if not options.filename:
                raise GE.GCSException('### ---- Null GCS report file name')
        except GE.GCSException:
            print "Using default log file: GCS.report\n"
            options.filename = 'GCS.report'
        self.__opt['filename'] = options.filename

        try:
            if not options.codeDir:
                raise GE.GCSException('### ---- Null source code dir')
        except GE.GCSException:
            options.codeDir = current_path
            print "Using CWD as source code dir\n"
        self.__opt['codeDir'] = options.codeDir
        print self.__opt

    def get_all_code_files(self):
        # need to re-write this function because it could not get all files in a dir recursively
        files = os.listdir(self.__opt['codeDir'])
        for item in files:
            result = re.match("^.*\.py$", item)
            if result:
                self.__code_files.append(item)

    def config_parser(self):

        self.__parser = OptionParser()
        self.__parser.add_option("-f", "--file", dest="filename",
                                 help="write report to FILE", metavar="FILE")
        self.__parser.add_option("-l", "--logFile", dest="logFileName",
                                 help="log will be stored in this file")
        self.__parser.add_option("-d", "--dir", dest="codeDir",
                                 help="source code directory, GCS will go through all .py files in this dir")
        self.__parser.add_option("-q", "--quiet",
                                 action="store_false", dest="verbose", default=True,
                                 help="don't print status messages to stdout")

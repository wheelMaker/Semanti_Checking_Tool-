#!/usr/bin/python
'''
   Verty start of this project
'''
import logging
import os

print 'GCS checker init'
print 'test for gerrit'

current_path = os.getcwd()
log_file_name = current_path + '/GCS.log'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_file_name,
                    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')


#os.rmdir(log_file_name)

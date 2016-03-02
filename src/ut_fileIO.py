#!/usr/bin/python

import os
import sys
import re
import file_IO as fIo


# case 1 for file open and close

def tc_file_open_close():
    current_path = os.getcwd()
    file_name = current_path + '/ut_io_file'
    file_path = current_path
    file_instance = fIo.FileIO(file_name)
    #print file_instance.get_file_name()

    file_instance.open_file('w')
    file_instance.close_file()
    if os.path.isfile(file_instance.get_file_name()):
        os.remove(file_instance.get_file_name())
    else:
        raise fIo.FileIOException("Case 1 failed! File does not exist, open file function down")


# case 2 for get file name

def tc_file_get_file_name():

    current_path = os.getcwd()
    file_name = current_path + '/ut_io_file'
    file_path = current_path
    file_instance = fIo.FileIO(file_name)
    #print file_instance.get_file_name()
    try:
        file_instance.set_file_name('a')
        result = re.match('a', file_instance.get_file_name())
        #print result
        if not result:
            raise fIo.FileIOException("Case 2 failed! file name is not match with set_file_name()")
    except fIo.FileIOException:
        print "Case 2 failed, null for the file name"


# case 3, test for file read and write

def tc_file_read_write():
    file_data = 'abcdefg'
    current_path = os.getcwd()
    file_name = current_path + '/ut_io_file'
    file_path = current_path
    file_instance = fIo.FileIO(file_name)
    #print file_instance.get_file_name()
    file_instance.open_file('w')
    file_instance.write_to_file(file_data)
    file_instance.close_file()
    file_instance.open_file('r')
    result = file_instance.read_file(len(file_data))
    #print len(file_data)
    #print result
    try:
        if not result == file_data:
            raise fIo.FileIOException("Case 3 failed, file write or read failure")
    except fIo.FileIOException:
        print "shit, file RW wrong~"

    if os.path.isfile(file_path + file_instance.get_file_name()):
        raise fIo.FileIOException("Case 2 failed! File does not exist, open file function down")
    else:
        os.remove(file_instance.get_file_name())

tc_file_open_close()
tc_file_get_file_name()
tc_file_read_write()
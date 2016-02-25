#!/usr/bin/python

import os
import sys
import re
import file_IO as fIo

current_path = os.getcwd()
file_name = current_path + '/ut_io_file'
file_path = current_path


# case 1 for file open and close

file_instance = fIo.FileIO(file_name)

file_instance.open_file('w')
file_instance.close_file()
if os.path.isfile(file_instance.get_file_name()):
    pass
else:
    raise fIo.FileIOException("Case 1 failed! File does not exist, open file function down")
os.remove(file_instance.get_file_name())

# case 2 for get file name

try:
    file_instance.set_file_name('/a')
    file_instance.open_file('w')
    file_instance.close_file()
except fIo.FileIOException:
    print "Case 2 failed, null for the file name"

if os.path.isfile(file_path + file_instance.get_file_name()):
    raise fIo.FileIOException("Case 2 failed! File does not exist, open file function down")
else:
    pass

# case 3 for create file




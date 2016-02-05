#!/usr/bin/python

import os
import file_IO as fIo

current_path = os.getcwd()
file_name = current_path + '/unit_test/ut_io_file'

file_instance = fIo.PyFileIO(file_name)

#  case for file open


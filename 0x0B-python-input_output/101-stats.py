#!/usr/bin/python3
""" This Module to log parsing """
import sys


total_size = 0
line_num = 0
possible_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_dic = {i: 0 for i in possible_status_code}
try:
    for line in sys.stdin:
        line_num += 1
        line_list = line.split()
        line_size = int(line_list[-1])
        status_code = int(line_list[-2])
        total_size += line_size
        status_code_dic[status_code] += 1
        if line_num % 10 == 0:
            print("File size: {}".format(total_size))
            for i in sorted(status_code_dic.keys()):
                if status_code_dic[i] > 0:
                    print("{}: {}".format(i, status_code_dic[i]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for i in sorted(status_code_dic.keys()):
        if status_code_dic[i] > 0:
            print("{}: {}".format(i, status_code_dic[i]))

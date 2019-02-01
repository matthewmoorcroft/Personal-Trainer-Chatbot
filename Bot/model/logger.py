# -*- coding: utf-8 -*-

import sys
import datetime
import time

class bcolors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAILURE = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

LOG_INFO = 0
LOG_STEP = 1
LOG_WARNING = 2
LOG_ERROR = 3
LOG_SUCCESS = 4

def log_type(log_type):
    if log_type == LOG_INFO:
        return "INFO",bcolors.INFO
    elif log_type == LOG_STEP:
        return "STEP PROCESSING",bcolors.INFO
    elif log_type == LOG_WARNING:
        return "WARNING",bcolors.WARNING
    elif log_type == LOG_ERROR:
        return "ERROR",bcolors.FAILURE
    elif log_type == LOG_SUCCESS:
        return "SUCCESS",bcolors.SUCCESS

def log(log_text, log_type=LOG_INFO):
    context_log_structure = "[%s] [%s] %s"
    log_type_text, log_type_color = log_type(log_type)
    context_log = log_type_color + bcolors.BOLD + context_log_structure % (log_type_text, datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S'), u' '.join((log_text,)).encode('utf-8').strip()) + bcolors.ENDC
    print (context_log)
    sys.stdout.flush()

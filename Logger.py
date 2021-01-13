#!/usr/bin/env python
#Autor: yaqingli
#Create date:
import time
import logging
from logging.handlers import RotatingFileHandler
import PartitionInsight.Config as Config



formatter = logging.Formatter('%(name)-12s %(asctime)-12s [line:%(lineno)d] %(levelname)-8s %(message)s', '%Y-%m-%d %H:%M:%S',)
file_handler = RotatingFileHandler(Config.Config().run_log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
file_handler.setFormatter(formatter)

logger_shell_command = logging.getLogger("ShellCommand")
logger_shell_command.addHandler(file_handler)
logger_shell_command.setLevel(logging.DEBUG)

logger_HiveSchemaETL = logging.getLogger("HiveSchemaETL")
logger_HiveSchemaETL.addHandler(file_handler)
logger_HiveSchemaETL.setLevel(logging.DEBUG)

logger_CleanData = logging.getLogger("CleanData")
logger_CleanData.addHandler(file_handler)
logger_CleanData.setLevel(logging.DEBUG)


log_functions = {'etl':logger_HiveSchemaETL,
 'clean_data':logger_CleanData,
 'shell':logger_shell_command}

def logit(log_name, message):
    def real_logit(function):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            log_message = "run {0}. message: {1} ".format(function.__name__, message)
            if log_name in log_functions:
                log_functions[log_name].info('Start ' + log_message)
            result = function(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            if log_name in log_functions:
                log_functions[log_name].info('Finish ' + log_message +'.Duration:{0}'.format(str(duration)))
            return result
        return wrapper
    return real_logit
    
    
#@logit(log_name='etl', message='download hive14')
#def download(self):
#    persistence = DataSaver(self._path, self.config)  

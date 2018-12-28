# 需求
# 1. 所有级别的日志写入磁盘文件
# 2. all.log 文件中记录所有的日志，日志格式为：日期和时间 - 日志级别 - 日志信息
# 3. error.log 文件中单独记录error及以上日志，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
# 4. 要求 all.log 在每天凌晨进行日志切割

import logging
import logging.handlers
import datetime

# 定义lgger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 为两个不同的文件设置不同的handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=None)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 把相应的处理器组装到logger
logger.addHandler(rf_handler)
logger.addHandler(f_handler)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
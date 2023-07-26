from log_processor import LogProcessor
from info_log_processor import InfoLogProcessor
from debug_log_processor import DebugLogProcessor
from error_log_processor import ErrorLogProcessor
from log_level import LogLevel

if __name__ == '__main__':
    lp: LogProcessor  = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))

    lp.log(LogLevel.INFO, 'This is INFO message')
    lp.log(LogLevel.DEBUG, 'This is DEBUG message')
    lp.log(LogLevel.ERROR, 'This is ERROR message')
    lp.log('TEST', 'This is TEST message')


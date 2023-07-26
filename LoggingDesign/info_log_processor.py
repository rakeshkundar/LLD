from log_processor import LogProcessor
from log_level import LogLevel

class InfoLogProcessor(LogProcessor):
    
    def __init__(self, next_log_processor: LogProcessor) -> None:
        super().__init__(next_log_processor)

    def log(self, log_level: LogLevel, message: str):
        if(log_level == LogLevel.INFO):
            print(f"INFO : {message}")
        else:
            super().log(log_level, message)
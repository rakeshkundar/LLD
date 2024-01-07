
class LogProcessor:

    next_log_processor = None

    def __init__(self, log_processor):
        self.next_log_processor = log_processor

    def log(self, log_level: int, message: str):
        if(self.next_log_processor):
            self.next_log_processor.log(log_level, message)
        else:
            print(f"This LOG is not handled in the code") 
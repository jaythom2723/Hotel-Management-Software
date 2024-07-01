class LogbookEntryMessage:
    def __init__(self, date: str, code: str, total: float):
        self.date: str = date
        self.code: str = code
        self.total: float = total
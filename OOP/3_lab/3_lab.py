from abc import ABC, abstractmethod
import re
import datetime
import socket
import ftplib
from enum import Enum
import tempfile
import os

class LogLevel(Enum):
    INFO = 1
    WARN = 2
    ERROR = 3


class ILogFilter(ABC):
    @abstractmethod
    def match(self, log_level: LogLevel, text: str) -> bool:
        ...


class SimpleLogFilter(ILogFilter):
    def __init__(self, pattern: str):
        self.pattern = pattern.lower()
    
    def match(self, log_level: LogLevel, text: str) -> bool:
        return self.pattern in text.lower()
    

class ReLogFilter(ILogFilter):
    def __init__(self, pattern: str):
        self.pattern = re.compile(pattern, re.IGNORECASE)
    
    def match(self, log_level: LogLevel, text: str) -> bool:
        return bool(self.pattern.search(text))
    

class LevelFilter(ILogFilter):
    def __init__(self, min_level: LogLevel):
        self.min_level = min_level
    
    def match(self, log_level: LogLevel, text: str) -> bool:
        return log_level.value == self.min_level.value
    

class ILogHandler(ABC):
    @abstractmethod
    def handle(self, log_level: LogLevel, text: str) -> None:
        pass


class ConsoleHandler(ILogHandler):
    def handle(self, log_level: LogLevel, text: str) -> None:
        print(f"CONSOLE: {text}")


class FileHandler(ILogHandler):
    def __init__(self, filename: str):
        self.filename = filename
    
    def handle(self, log_level: LogLevel, text: str) -> None:
        try:
            with open(self.filename, 'a', encoding = 'utf-8') as f:
                f.write(f"{text}\n")
        except Exception as e:
            print(f"FileHandler error: {e}")


class SocketHandler(ILogHandler):
    def __init__(self, host: str = "localhost", port: int = 6000):
        self.host = host
        self.port = port
    
    def handle(self, log_level: LogLevel, text: str) -> None:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                sock.sendall(f"{text}\n".encode('utf-8'))
        except Exception as e:
            print(f"SocketHandler error: {e}")


class SyslogHandler(ILogHandler):
    def __init__(self, log_dir: str = "3_lab/logs", app_name: str = "app_logs") -> None:
            self.log_dir = log_dir
            self.app_name = app_name
            os.makedirs(log_dir, exist_ok = True)
            self.log_file = os.path.join(log_dir, f"{app_name}.log")

    def handle(self, log_level: LogLevel, text: str) -> None:
        try:
            with open(self.log_file, "a", encoding="utf-8") as file:
                file.write(f"{text}\n")
        except Exception as e:
            print(f"SyslogHandler error: {e}")


class FtpHandler(ILogHandler):
    def __init__(self, host: str, username: str, password: str, remote_path: str = "/logs/app.log"):
        self.host = host
        self.username = username
        self.password = password
        self.remote_path = remote_path
    
    def handle(self, log_level: LogLevel, text: str) -> None:
        try:
            with tempfile.NamedTemporaryFile(mode = 'w', delete = False, encoding = 'utf-8') as temp_file:
                temp_file.write(text)
                temp_filename = temp_file.name
            
            with ftplib.FTP(self.host) as ftp:
                ftp.login(self.username, self.password)
                with open(temp_filename, 'r') as file:
                    ftp.storbinary(f"STOR {self.remote_path}", file)
            os.remove(temp_filename)
        except Exception as e:
            print(f"FtpHandler error: {e}")


class ILogFormatter(ABC):
    @abstractmethod
    def format(self, log_level: LogLevel, text: str) -> str:
        pass


class data_Formatter(ILogFormatter):
    def __init__(self, time_format: str = "%Y.%m.%d %H:%M:%S"):
        self.time_format = time_format

    def format(self, log_level: LogLevel, text: str) -> str:
        current_time = datetime.datetime.now().strftime(self.time_format)
        level_name = log_level.name
        return f"[{level_name}] [data:{current_time}] {text}"
    

class StupidFormatter(ILogFormatter):
    def __init__(self, format_string: str):
        self.format_string = format_string
    
    def format(self, log_level: LogLevel, text: str) -> str:
        return f"[{self.format_string}: {text}]"
    

class Logger:
    def __init__(
        self,
        filters: list[ILogFilter],
        formatters: list[ILogFormatter],
        handlers: list[ILogHandler]
    ):
        self.filters = filters
        self.formatters = formatters
        self.handlers = handlers
    
    def log(self, log_level: LogLevel, text: str) -> None:
        for filter_obj in self.filters:
            if not filter_obj.match(log_level, text):
                return
        
        formatted_text = text
        for formatter in self.formatters:
            formatted_text = formatter.format(log_level, formatted_text)
        
        for handler in self.handlers:
            handler.handle(log_level, formatted_text)
    
    def log_info(self, text: str) -> None:
        self.log(LogLevel.INFO, text)
    
    def log_warn(self, text: str) -> None:
        self.log(LogLevel.WARN, text)
    
    def log_error(self, text: str) -> None:
        self.log(LogLevel.ERROR, text)


filters = [
    LevelFilter(LogLevel.WARN),
    ReLogFilter(r"Важно|Ошибка"),
]

formatters = [data_Formatter('%Y.%d.%H')]

handlers = [
    ConsoleHandler(),
    FileHandler("3_lab/test_3_lab.log"),
    #SocketHandler(),
    SyslogHandler(),
]

logger = Logger(filters, formatters, handlers)

logger.log_info("Информационное сообщение")
logger.log_info("Важное информационное сообщение")
logger.log_warn("Важное информационное сообщение")
logger.log_warn("Ошибка системы")
logger.log_warn("Важное предупреждение")
logger.log_error("Критическая ошибка")
import sys
import uuid
import logging

from pathlib import Path
from datetime import datetime

class TraceLogger:
    def __init__(self):
        current_date = datetime.now().strftime("%Y%m%d")
        log_file_name = f"backend_{current_date}.log"
        
        log_directory = Path("logs")
        log_directory.mkdir(parents = True, exist_ok = True)
        log_file_path = f"{log_directory}/{log_file_name}"
        
        logging.root.handlers = []
        logging.basicConfig(
            level = logging.INFO,
            format = "%(levelname)-8s [%(asctime)s] | [%(trace_id)s] | [%(filename)s.%(funcName)s:%(lineno)d] %(message)s",
            handlers = [ 
                logging.FileHandler(log_file_path),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
    
    def get_logger(self, trace_id: str):
        return logging.LoggerAdapter(self.logger, {"trace_id": trace_id if trace_id else str(uuid.uuid4())})
    
trace_logger = TraceLogger()
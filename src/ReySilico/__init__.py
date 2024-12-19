import os
import sys
import logging

#log string details and formate
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#making log folder and path for log to be saved
log_dir="logs"
log_filepath= os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

#initialisation of log
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handler=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout), # printing log in terminal
    ]
)


logger=logging.getLogger(name="ReySilico_logger")



# Logger is for the purpose that if exception occurs we should be able to log
# all the information in some files

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# .strftime("%m_%d_%Y_%H_%M_%S") → Formats the datetime into a
# string like 08_24_2025_12_10_33.

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# "logs" → A folder where you want to store all log files.
os.makedirs(logs_path,exist_ok=True)
# exist_ok=True → No error if the folder already exists.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
# his again appends the file name to logs_path.
# C:/your_project/logs/08_24_2025_12_10_33.log/08_24_2025_12_10_33.log


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,
    


)
# filename=LOG_FILE_PATH → Where logs will be saved.
# %(asctime)s → Timestamp of the log.

# %(lineno)d → Line number where the log was triggered.

# %(name)s → Logger’s name (often module name).

# %(levelname)s → Logging level (INFO, ERROR, WARNING, etc.).

# %(message)s → Actual log message.
# level=logging.INFO → Minimum level to log.
#  This means INFO, WARNING, ERROR, and CRITICAL will be logged, 
# but DEBUG will be ignored.


if __name__=="__main__":
    logging.info("Logging has started")

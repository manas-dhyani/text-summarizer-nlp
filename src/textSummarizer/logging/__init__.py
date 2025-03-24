import os
import logging
import sys

logging_str = "[%(asctime)s]: %(levelname)s : %(message)s]" # Format of the log message
log_dir = "logs"# Directory to save the logs
log_filepath = os.path.join(log_dir, "running_logs.log")# Filepath to save the logs
os.makedirs(log_dir, exist_ok=True) # Create the directory if it does not exist



logging.basicConfig(
    level=logging.INFO,# Set the logging level
    format=logging_str,# Set the format of the log message
    handlers=[
        logging.FileHandler(log_filepath),  # Save the logs to a file
        logging.StreamHandler(sys.stdout)   # Print the logs to the console
    ]
)


logger = logging.getLogger("textSummarizerLogger") # Get the logger object
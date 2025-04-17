#python function frequently in the code, we use utils to store them we use util to import them
import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read the yaml file and return the ConfigBox object

    Args:
    path_to_yaml (Path): Path to the yaml file as input

    Returns:
    ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file read successfully from {path_to_yaml}")
            return ConfigBox(config)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories 

    Args:
         path_to_directories (list): list of directories
         ignore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size of the directory

    Args:
        path (Path): path to the directory

    Returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

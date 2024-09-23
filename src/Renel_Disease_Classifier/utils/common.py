import os 
from box.exceptions import BoxValueError
import yaml
from Renel_Disease_Classifier.logger import logging
from Renel_Disease_Classifier.exception import RenelException
import sys
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise RenelException(e,sys)
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"jason file saved at: {path}")
    except Exception as e:
        raise RenelException(e,sys)
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path, "rb") as f:
            content = json.load(f)
            return ConfigBox(content)
    except Exception as e:
        raise RenelException(e,sys)
    

@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data, filename=path)
    except Exception as e:
        raise RenelException(e,sys)
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        return joblib.load(path)
    except Exception as e:
        raise RenelException(e,sys)


@ensure_annotations
def get_size(path: Path) -> str:
    """
    path: str
    """
    size_in_mb = round(os.path.getsize(path)/(1024*1024), 2)
    return f"{size_in_mb} MB"


@ensure_annotations
def encode_to_base64(file_path: Path) -> str:
    with open(file_path, 'rb') as f:
        data = f.read()
        return base64.b64encode(data).decode('utf-8')
    

@ensure_annotations
def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')
    
    


    

import os 
import urllib.request as request
import zipfile
import gdown
from Renel_Disease_Classifier.logger import logging
from Renel_Disease_Classifier.exception import RenelException
from Renel_Disease_Classifier.utils.common import get_size
import sys
from Renel_Disease_Classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)->str:
        logging.info("Entered the download_file method of Data_Ingestion class") 

        try:

            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} into {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            pref = "https://drive.google.com/uc?/export=download&id="
            gdown.download(pref+file_id,zip_download_dir,quiet=True)

            logging.info(f"Downloaded data from {dataset_url} into {zip_download_dir}")


        except Exception as e:
            raise RenelException(e,sys)
        

    def extract_zip_file(self):

        logging.info("Entered the extract_zip_file method of Data_Ingestion class")
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        try:

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logging.info(f"Extracted zip file into {unzip_path}")
        except Exception as e:
            raise RenelException(e,sys)
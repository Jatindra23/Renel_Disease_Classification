from Renel_Disease_Classifier.config.configuration import ConfigurationManager
from Renel_Disease_Classifier.components.data_ingestion import DataIngestion
from Renel_Disease_Classifier.exception import RenelException
from Renel_Disease_Classifier.logger import logging


import sys


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:

            logging.info("Entered in ingestion pipline main funcion")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logging.info("exited from ingestion pipline main funcion")

        except Exception as e:
            raise RenelException(e, sys)


if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> stage Data Ingestion started <<<<<<\n\nx==========x")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>> stage Data Ingestion completed <<<<<<\n\nx==========x")

    except Exception as e:
        logging.exception(e)
        raise RenelException(e, sys)

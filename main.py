from Renel_Disease_Classifier.logger import logging
from Renel_Disease_Classifier.exception import RenelException
import sys
from Renel_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<\n\nx==========x")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logging.exception(e)
    raise RenelException(e,sys)
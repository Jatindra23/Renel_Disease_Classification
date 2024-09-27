from Renel_Disease_Classifier.logger import logging
from Renel_Disease_Classifier.exception import RenelException
import sys
from Renel_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Renel_Disease_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Renel_Disease_Classifier.pipeline.stage_03_model_training import ModelTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<\n\nx==========x")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logging.exception(e)
    raise RenelException(e,sys)



STAGE_NAME = "Prepare base model stage"
try:

    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<\n\nx==========x")
    preparebase_model = PrepareBaseModelTrainingPipeline()
    preparebase_model.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logging.exception(e)
    raise RenelException(e,sys)



STAGE_NAME = "Model Training"
try:

    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<\n\nx==========x")
    model_trainer_pipeline = ModelTrainingPipeline()
    model_trainer_pipeline.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    raise RenelException(e,sys)
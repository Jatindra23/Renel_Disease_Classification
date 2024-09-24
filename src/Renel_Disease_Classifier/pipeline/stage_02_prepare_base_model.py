from Renel_Disease_Classifier.config.configuration import ConfigurationManager
from Renel_Disease_Classifier.components.prepare_base_model import PrepareBaseModel
from Renel_Disease_Classifier import logger
import sys
from Renel_Disease_Classifier.exception import RenelException
from Renel_Disease_Classifier.logger import logging


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise RenelException(e, sys)


STAGE_NAME = "Prepare base model stage"
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<\n\nx==========x")
        preparebase_model = PrepareBaseModelTrainingPipeline()
        preparebase_model.main()
        logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logging.exception(e)
        raise RenelException(e, sys)

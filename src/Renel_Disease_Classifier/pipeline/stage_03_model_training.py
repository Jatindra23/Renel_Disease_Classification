from Renel_Disease_Classifier.config.configuration import ConfigurationManager
from Renel_Disease_Classifier.components.model_training import Training
from Renel_Disease_Classifier.exception import RenelException
from Renel_Disease_Classifier.logger import logging
import sys


STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:

            config = ConfigurationManager()
            training_config = config.get_training_config()
            model_trainer = Training(config=training_config)
            model_trainer.get_base_model()
            model_trainer.train_valid_generator()
            model_trainer.train()

        except Exception as e:
            raise RenelException(e, sys)


if __name__ == "__main__":
    try:
        logging.info(f"**********************")
        logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<\n\nx==========x")
        model_trainer_pipeline = ModelTrainingPipeline()
        model_trainer_pipeline.main()
        logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise RenelException(e,sys)
 
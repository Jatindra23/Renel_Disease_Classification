import mlflow
import tensorflow as tf
from pathlib import Path
import mlflow.keras
from urllib.parse import urlparse
import dagshub
from mlflow.models.signature import infer_signature
from Renel_Disease_Classifier.entity.config_entity import EvaluationConfig
from Renel_Disease_Classifier.utils.common import save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):

        datagenerator_kwargs = dict(rescale=1.0 / 255, validation_split=0.30)

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(path=Path("artifacts/training/model.h5"))
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        dagshub.init(
            repo_owner="jatin9091",
            repo_name="Renel_Disease_Classification_Deep_Learning",
            mlflow=True,
        )

        # Get a batch of input data from the validation generator
        # Ensure that `self.valid_generator` has been initialized
        if not hasattr(self, "valid_generator"):
            self._valid_generator()

        # Fetch one batch of data
        input_data, _ = next(self.valid_generator)

        # Generate predictions
        predictions = self.model.predict(input_data)

        # Infer the model signature
        signature = infer_signature(input_data, predictions)

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(
                    self.model,
                    "model",
                    signature=signature,
                    registered_model_name="VGG16Model",
                )
            else:
                mlflow.keras.log_model(self.model, "model", signature=signature)

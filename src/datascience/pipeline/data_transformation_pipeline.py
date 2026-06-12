import sys
from pathlib import Path
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read()

            if "True" in status:
                logger.info("Data Validation Status: PASSED. Initializing Data Transformation...")
                
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
                
            else:
                logger.error("Data Validation Status: FAILED. Pipeline execution halted.")
                print("Your data scheme is not valid")
                
        except Exception as e:
            raise e
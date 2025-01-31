from wine_quality_end_to_end_Project.config.configuration import ConfigurationManager
from wine_quality_end_to_end_Project.components.data_validation import DataValidation
from wine_quality_end_to_end_Project import logger

STAGE_NAME = "Data Validation stage"

class DataVAlidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()

        
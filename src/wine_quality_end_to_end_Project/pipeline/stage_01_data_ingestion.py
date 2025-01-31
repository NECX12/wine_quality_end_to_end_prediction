from wine_quality_end_to_end_Project.config.configuration import ConfigurationManager
from wine_quality_end_to_end_Project.components.data_ingestion import DataIngestion
from wine_quality_end_to_end_Project import logger



STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:

    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
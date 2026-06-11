import os
import urllib.request as request
import zipfile
import ssl 
from src.datascience import logger
from src.datascience.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info("Attempting to download dataset...")
            
            # Set the unverified context globally for urllib in this session
            ssl._create_default_https_context = ssl._create_unverified_context
            
            
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download successfully with the following info:\n{headers}")
        else:
            logger.info(f"File already exists at: {self.config.local_data_file}")

    def extract_zip_file(self):
        """
        Extracts the zip file into the data ingestion directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Zip file extracted successfully to: {unzip_path}")
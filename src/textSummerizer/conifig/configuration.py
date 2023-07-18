import os
from textSummerizer.constants import *
from textSummerizer.utils.common import read_yaml,create_directory
from textSummerizer.entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self, config_filepath= CONFIG_FILE_PATH, param_filepath= PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(param_filepath)
        create_directory([self.config.artifact_root])
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config= self.config.data_ingestion
        create_directory([config.root_dir])
        data_ingestion_config= DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
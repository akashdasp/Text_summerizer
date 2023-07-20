from textSummerizer.pipeline.stage01_data_ingestion import DataIngestionTraningPipelining
from textSummerizer.pipeline.stage02_data_validation import DataValidationTraningPipelining
from textSummerizer.logging import logger

STAGE_NAME= "Data Ingestion Stage"
try :
    logger.info(f'{STAGE_NAME} Streaming Data Ingestion')
    data_ingestion= DataIngestionTraningPipelining()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} Streaming Data Ingestion Completed')
except Exception as e :
    # logger.exception(e)
    # raise e
    pass



STAGE_NAME= "Data Validation Stage"
try :
    logger.info(f'Streaming {STAGE_NAME} ')
    data_ingestion= DataIngestionTraningPipelining()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} Completed')
except Exception as e :
    logger.exception(e)
    raise e
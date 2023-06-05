from src.CNN_Classifier import logger
from src.CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} con=mpleted <<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e
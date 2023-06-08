from src.CNN_Classifier import logger
from src.CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CNN_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.CNN_Classifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.CNN_Classifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} con=mpleted <<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} con=mpleted <<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training Stage"

if __name__ == '__main__':
    try:
        logger.info("******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Evaluation Stage"

if __name__ == "__main__":
    try:
        logger.info("******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation = EvaluationPipeline()
        model_evaluation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    
    except Exception as e:
        logger.exception(e)
        raise e
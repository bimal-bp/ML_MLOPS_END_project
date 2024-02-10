from mlProject import logger
from mlProject.pipeline.stage_01_data_ingetion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME=" Data Ingestion stage"

try:
    logger.info(f">>>>>>>>stage{STAGE_NAME} started <<<<<<")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage{STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME=" Data Validation stage"

try:
    logger.info(f">>>>>stage {STAGE_NAME} started <<<<<<<")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation "

try:
    logger.info(f"stage>>>{STAGE_NAME} started<<<<<<")
    obj=DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"<<<<{STAGE_NAME}>>>completed ")
except Exception as e:
    raise e
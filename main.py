from TransactionMonitoring.components.data_ingestion import DataIngestion
from TransactionMonitoring.components.data_validation import DataValidation
from TransactionMonitoring.exception.exception import TransactionMonitoringException
from TransactionMonitoring.logging.logger import logging
from TransactionMonitoring.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig

if __name__=='__main__':
    try:
        trainingpuipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(trainingpuipeline_config)
        data_ingestion_obj=DataIngestion(data_ingestion_config)
        logging.info("Exporting collection as dataframe")
        dataingestionartifact = data_ingestion_obj.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(trainingpuipeline_config)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiating data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
    except TransactionMonitoringException as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)
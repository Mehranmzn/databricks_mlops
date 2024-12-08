from TransactionMonitoring.components.data_ingestion import DataIngestion
from TransactionMonitoring.exception.exception import TransactionMonitoringException
from TransactionMonitoring.logging.logger import logging
from TransactionMonitoring.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpuipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(trainingpuipeline_config)
        data_ingestion_obj=DataIngestion(data_ingestion_config)
        logging.info("Exporting collection as dataframe")
        dataingestionartifact = data_ingestion_obj.initiate_data_ingestion()
        print(dataingestionartifact)
    except TransactionMonitoringException as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)
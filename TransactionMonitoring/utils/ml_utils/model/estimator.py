import os
import sys

from TransactionMonitoring.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
from TransactionMonitoring.exception.exception import TransactionMonitoringException
from TransactionMonitoring.logging.logger import logging

class TransactionMonitoring:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise TransactionMonitoringException(e,sys)
    
    def predict(self,x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise TransactionMonitoringException(e,sys)
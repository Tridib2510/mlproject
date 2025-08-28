# Here the transformation of data takes place such as changing categorical
# features into numerical features and so on

import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
# Column Transformeter is used to create pipeline
from sklearn.impute import SimpleImputer
# SimpleImputer is used to handle missing 
# values (NaN) in your dataset by replacing them with some strategy.
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    #This function is  responsible for data transformation for different
    # types of data
    def get_data_transformer_object(self):
         try:
            numerical_columns=["writing_score","reading_score"]
            categorical_columans=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            # Creating a pipeline
            # This is a Scikit-learn Pipeline, which lets you chain 
            # multiple preprocessing steps together so you can 
            # apply them consistently to your dataset (train/test)
            #  without repeating code.
            num_pipeline=Pipeline(
            steps=[
                # We observe that in the EDA that there are a lot of
                # outliers so we are going to use median
                   ("imputer",SimpleImputer(strategy="median")),
# Missing values in your numeric features are handled here.
# SimpleImputer(strategy="median") replaces missing values 
# with the median of the column.
# Why median?
# From your comment: during EDA, you saw that the data had outliers.
# The mean can get skewed by outliers, but the median is robust and gives a better central tendency in such cases.                   

                   ("scaler",StandardScaler()),

               ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                    # Numeric features (dense) → StandardScaler(with_mean=True) (default)
                    # Categorical one-hot (sparse) → StandardScaler(with_mean=False)
                ]
            )
            logging.info("Numerical columns: {categorical_columns}")
            logging.info("Categorical columns encoding completed: {numerical_columns}")

            # Combining numerical and categorical pipelines
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipelines",cat_pipeline,categorical_columans)
                ]
            )

            return preprocessor



         except Exception as e:
             raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe"
            )
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            logging.info(f"Saved preprocessing object. ")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            # we have this save_object in utils

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e:
           raise CustomException(e,sys)



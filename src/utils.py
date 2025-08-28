# Any functionality that we are writing in a common
# way that are getting used in the entire application
# ex->saving our data to cloud

import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException



def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
# By default, makedirs throws an error if the directory already exists.
# If you pass exist_ok=True, it will ignore the error and continue.
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

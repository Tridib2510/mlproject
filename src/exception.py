from src.logger import logging

import sys 
# Any exception that is getting controlled the sys
# library will automatically have that info

# This error_details will be provided inside sys
def error_message_details(error,error_details:sys):
   _,_,exc_tb= error_details.exc_info()#This gives us 3 important info
#    we are not interested in the first 2.
# exc_tb will give us info on what file ,line the exception has occured

   file_name=exc_tb.tb_frame.f_code.co_filename#we get the file name
   error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
      file_name,
      exc_tb.tb_lineno,
      str(error) )#Whenever error raises we are going to call this function

   return error_message
  
   
class CustomException(Exception):
   def __init__(self,error_message,error_details:sys):
      super().__init__(error_message)
      self.error_message=error_message_details(error_message,error_details=error_details)

   def __str__(self):
      return self.error_message
   







      
        


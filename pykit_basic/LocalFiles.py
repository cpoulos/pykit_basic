import os
import sys
import numpy as np
import pandas as pd
import glob

class LocalFiles():
   def __init__(self):
      pass

   # Grab file names without .csv in any directory
   def list_files(self,directory):
      for root, dirs, files in os.walk(directory):
         files = [f for f in files if not f[0] == '.'] #ignore .DStore and hidden files
         file_names = []
         for filename in files:
            file_names.append(filename)
         return file_names

   # Grab list of files in any directory
   def list_files_as_tbl_names(self,directory):
      for root, dirs, files in os.walk(directory):
         files = [f for f in files if not f[0] == '.'] #ignore .DStore and hidden files
         tbl_names = []
         for filename in files:
            tbl_names.append(filename)
         tbls = pd.Series(tbl_names)
         tbls = tbls.str.split('.').str[0] #removes .csv from file name to create tbl name
         tbls = tbls.tolist()
         return tbls

   ## DATAFRAME METHODS ## --> Class?      
   def make_id_field(self,df,cols='N/A'): #Note: to pass 1 col value pass a string like 'col'; muliple pass a list
      if cols == 'N/A':
         cols = list(df)
      for col in cols:
         df[col].fillna(999999999, inplace=True)
         df[col] = df[col].astype(np.int64, errors='ignore')
      return df

   def removenullrows(self,df):
      df.dropna(axis=0,how='all',inplace=True)
      return df

   def removenullcols(self,df):
      df.dropna(axis=1, how='all',inplace=True)
      return df

   def renamecols(self,df,cols):
      df.columns = cols
      return df

   ## DATAFRAME DICTIONARY METHODS ## --> class?
   def create_df_dict(self,directory,list_files,delimiter=',',header='infer'): # need to account for non-file version of the thing
      #grab all csv files in specified directory
      all_files = glob.glob(directory + "/*.csv")
      dfs = []
      dicts = {}
      tbls = pd.Series(list_files)
      tbls = tbls.str.split('.').str[0] #removes .csv from file name to create tbl name
      tbls = tbls.tolist()
      # create dictionary from list of file names and list of dfs
      for file in all_files:
         dfs.append(pd.read_csv(file, header=header, delimiter=delimiter))
      # create dicts
      dicts = dict(zip(tbls,dfs))
      return dicts

   ## DATAFRAME DICTIONARY METHODS ## --> class?
   def create_df_dict_xls(self,directory,list_files,header='infer'): # need to account for non-file version of the thing
      #grab all csv files in specified directory
      all_files = glob.glob(directory + "/*.xlsx")
      dfs = []
      dicts = {}
      tbls = pd.Series(list_files)
      tbls = tbls.str.split('.').str[0] #removes .csv from file name to create tbl name
      tbls = tbls.tolist()
      # create dictionary from list of file names and list of dfs
      for file in all_files:
         dfs.append(pd.read_excel(file, header=header,encoding='utf-8'))
      # create dicts
      dicts = dict(zip(tbls,dfs))
      return dicts


   def clean_df_dict(self,df_dict,id_cols=[],clean_param='all'): #all, #rmv_null_cols, #rmv_null_rows, #make_id
      if clean_param == 'all':
         # remove any blank columns from df
         for value in df_dict.values():
            self.removenullcols(value)
         # remove all rows with all null values
         for value in df_dict.values():
            self.removenullrows(value)
         # make ID fields non-float
         for value in df_dict.values():
            self.make_id_field(value,id_cols) #id_cols takes a list
      #individual clean params
      elif clean_param == 'rmv_null_rows':
         for value in df_dict.values():
            self.removenullrows(value)
      elif clean_param == 'rmv_null_cols':
         for value in df_dict.values():
            self.removenullcols(value)
      elif clean_param == 'make_id':
         for value in df_dict.values():
            self.make_id_field(value,id_cols) #id_cols takes a list
      return df_dict

   def rename_df_dict_cols(self,df_dict,cols):
      for value in df_dict.values():
         self.renamecols(value,cols)
      return df_dict 

   def sf_load_dfs_from_dict(self,df_dict,tbl_prefix,sf_connector):
      for key, value in df_dict.items():
         sf_connector.load_data(value, tbl_prefix+key, from_file=False, config="create_table")
      pass

   def mv_input_to_processed_dir(self,input_dir,input_file,processed_dir):
      os.replace(input_dir + input_file, processed_dir + input_file)
      pass

   # changes carriage return to dos format for windows
   def unix2dos(self,input_file,output_file):
      infile = open(input_file,'r')
      outfile = open(output_file, 'w')
      for line in infile:
         line = line.rstrip() + '\r\n'
         outfile.write(line)
      infile.close()
      outfile.close()

def main():
   pass

if __name__ == '__main__':
   main()


### HELPFUL ARTICLES ###
# class inheritance? https://www.programiz.com/python-programming/inheritance
# https://stackoverflow.com/questions/30280856/populating-a-dictionary-using-for-loops-python/30280874
# https://realpython.com/iterate-through-dictionary-python/#iterating-through-items
# https://stackoverflow.com/questions/25656126/looping-through-df-dictionary-in-order-to-merge-dfs-in-pandas/25657468
# https://www.kite.com/python/answers/how-to-get-the-first-key-value-in-a-dictionary-in-python
# https://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders ##accounts for the .DStore hidden files
# https://www.geeksforgeeks.org/iterating-over-rows-and-columns-in-pandas-dataframe/
# https://stackoverflow.com/questions/62204221/snowflake-python-3-connection-closed-error #connection closed error pattern



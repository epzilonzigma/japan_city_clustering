import numpy as np
import pandas as pd
import glob

def load_data(path, skip = 8):
    '''
    load .csv path and clean unnecessary columns
    '''

    df = pd.read_csv(path, skiprows = skip)
    df.drop(columns = ['YEAR Code', 'YEAR', '/ITEMS'], inplace = True)
    df.rename(columns = {'AREA': 'City', 'AREA Code': 'city_code'}, inplace = True)

    col_names = list(df.columns[:2])
    new_col_names = [str(x)[str(x).find('_')+1:] for x in df.columns[2:]]
    col_names.extend(new_col_names)
    
    df.columns = col_names

    return df


def create_master_dataframe(folder_path):
    '''
    merge all .csv datasets and create master dataframe to be loaded into the app
    '''

    file_list = glob.glob(folder_path + '/*.csv')

    for file in file_list:
        if file == file_list[0]:
            df = load_data(file)
        else:
            df_temp = load_data(file)
            df = df.merge(df_temp, on = ['City', 'city_code'])

    return df
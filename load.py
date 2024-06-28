import pandas as pd
import csv

DATASET_PATH = './datasets/toprankedanime.csv'

def getData(path: str) -> pd.DataFrame:
    '''
    Load data from csv file.
    '''
    dataset = pd.read_csv(path)
    return dataset

def filterData(dataset: pd.DataFrame, columns: list = []) -> pd.DataFrame:
    '''
    Filter data by columns.
    '''
    if len(columns) == 0:
        return dataset
    return dataset[columns]

def getColumns(dataset: pd.DataFrame) -> list:
    '''
    Get column titles.
    '''
    return dataset.columns.tolist()
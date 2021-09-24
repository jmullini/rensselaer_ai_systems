import sqlite3
import configparser

def sqlite_connection():

    return sqlite3.connect('../data/database/ai_systems')

def get_api_key():

    config = configparser.ConfigParser()
    config.read('../config.ini')

    return config['DEFAULT']['APIKEY']

def get_symbol_list():

    df = pd.read_csv('../data/static/sandp100.csv')

    return df['Ticker'].tolist()

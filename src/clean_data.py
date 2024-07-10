import pandas as pd

def clean_data():
    df = pd.read_csv('dataset/airlines_final.csv')
    print(df.head(5))
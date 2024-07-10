from thefuzz import process
import pandas as pd

def munging_data():
    df = pd.read_csv("../dataset/banking_dirty.csv")
    print(df.head(5))

if __name__ == "__main__":
    munging_data()
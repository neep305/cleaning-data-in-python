import pandas as pd
import datetime as dt

def check_age_consistency():
    banking = pd.read_csv('../dataset/banking_dirty.csv')
    print(banking.head(5))

    # rename the column 'Age' to 'age'
    banking.rename(columns={'Age': 'age'}, inplace=True)

    # birth_date 날짜 타입으로 변경
    banking['birth_date'] = pd.to_datetime(banking['birth_date'])

    today = dt.date.today()
    ages_manual = today.year - banking['birth_date'].dt.year

    age_edu = banking['age'] == ages_manual

    # Store consistent and inconsistent data
    consistent_ages = banking[age_edu]
    inconsistent_ages = banking[~age_edu]

    print("Number of inconsistent ages: ", inconsistent_ages.shape[0])


if __name__ == "__main__":
    check_age_consistency()
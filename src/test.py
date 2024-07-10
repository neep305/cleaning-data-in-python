import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 예시 데이터프레임 생성
def show_data():
    data = {
        'A': np.random.rand(100),
        'B': np.random.rand(100)
    }
    df = pd.DataFrame(data)

    # 데이터 분석 및 시각화
    print(df.describe())

    sns.scatterplot(x='A', y='B', data=df)
    plt.show()
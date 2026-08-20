# 9.	Create a DataFrame with missing values and fill them with column means. 

import pandas as pd
import numpy as np

def MarvellousClassifier():

    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }

    df2 = pd.DataFrame(data2)

    print("DataFrame with missing values:")
    print(df2)

    # Fill missing values with column means
    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

    print("\nDataFrame after filling missing values:")
    print(df2)




def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
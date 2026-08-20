# 9.	Create a DataFrame with missing values and fill them with column means. 

import pandas as pd

def MarvellousClassifier():

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    print(df)

    # Drop the English column
    print("Drop the English column")
    df = df.drop('English', axis=1)

    print(df)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
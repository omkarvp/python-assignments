# 1.	Create a DataFrame for student marks and print basic information like shape, columns, and data types. 
import pandas as pd
def MarvellousClassifier():

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # Print the DataFrame
    print("Student DataFrame:")
    print(df)

    # Print basic information
    print("\nShape of DataFrame:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
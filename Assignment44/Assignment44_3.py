# 3.	Add a Total column as the sum of all subject marks. 
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

    # Add Total column
    print("\nAdd Total column :")

    df['Total'] = df['Math'] + df['Science'] + df['English']

    print(df)
def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
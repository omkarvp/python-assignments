# 5.	Replace Pooja with Puja in the Name column. 
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
    print("-"*65)
    # Replace Pooja with Puja
    print("Replace Pooja with Puja:")
    df['Name'] = df['Name'].replace('Pooja', 'Puja')

    print(df)


def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
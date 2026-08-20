# 2.	Create a Gender column and perform one-hot encoding. 
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

    print("-"*65)
    # Create Gender column
    df['Gender'] = ['Male', 'Male', 'Female']

    # Perform one-hot encoding
    print("one-hot encoding : ")
    df = pd.get_dummies(df, columns=['Gender'])

    print(df)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
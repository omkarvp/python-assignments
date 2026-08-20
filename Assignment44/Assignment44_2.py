# 2.	Use the DataFrame from Q1 and print descriptive statistics using .describe()
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

    # Descriptive statistics
    print("\nDescriptive statistics :")
    print(df.describe())

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
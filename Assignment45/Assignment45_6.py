# 6.	Count how many students passed. 
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
    # Calculate Total marks
    df['Total'] = df['Math'] + df['Science'] + df['English']

    # Add Status column
    df['Status'] = df['Total'].apply(
        lambda x: 'Pass' if x >= 250 else 'Fail'
    )

    # Count passed students
    passed_count = (df['Status'] == 'Pass').sum()

    print("Number of students passed:", passed_count)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
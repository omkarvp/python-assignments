# 7.	Export the final DataFrame to a CSV file.
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

    # Export DataFrame to CSV
    df.to_csv('final_student_data.csv', index=False)

    print("DataFrame exported successfully to final_student_data.csv")

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
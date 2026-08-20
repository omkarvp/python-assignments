# 3.	Group students by gender and calculate average marks. 
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

    # Group by Gender and calculate average marks
    print("Group by Gender and calculate average marks : ")
    average_marks = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

    print(average_marks)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
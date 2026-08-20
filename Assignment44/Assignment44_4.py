# 4.	Display students who scored more than 85 in Science. 
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
    # Display students who scored more than 85 in Science
    print("Students who scored more than 85 in Science:")
    result = df[df['Science'] > 85]

    print(result)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
# 6.	Sort the DataFrame by Total marks in descending order. 
import pandas as pd
import matplotlib.pyplot as plt
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
    # Add Total column
    df['Total'] = df['Math'] + df['Science'] + df['English']

    # Sort by Total marks in descending order
    print("Sort by Total marks in descending order:")
    df = df.sort_values(by='Total', ascending=False)

    print(df)



def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
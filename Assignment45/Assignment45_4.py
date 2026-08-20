#4.	Plot a pie chart of subject marks for Sagar.  
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
    print(df)

    print("-"*65)
    # Get Sagar's marks
    sagar = df[df['Name'] == 'Sagar'].iloc[0]

    # Subject marks
    subjects = ['Math', 'Science', 'English']
    marks = [sagar['Math'], sagar['Science'], sagar['English']]

    # Create pie chart
    plt.pie(marks, labels=subjects, autopct='%1.1f%%')

    plt.title("Sagar's Subject Marks")
    plt.legend()
    plt.show()

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
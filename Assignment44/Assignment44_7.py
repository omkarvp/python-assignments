# 7.	Create a bar plot of student names vs. total marks. 
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

    plt.bar(
        df['Name'], 
        df['Total'],
        width=0.6,              # width of bars
        edgecolor="black",      # border color of bars
        linewidth=1,            # width of bar border
        alpha=0.8,              # transperence from 0.0 to 1.0
        label="Students"        # legendtext
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel = "Name"
    plt.ylabel = "Total"
    plt.legend()
    plt.show()




def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
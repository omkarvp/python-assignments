# 8.	Plot a line chart of marks for Amit across all subjects. 
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

    # Get Amit's marks
    amit = df[df['Name'] == 'Amit'].iloc[0]

    # Create line chart
    subjects = ['Math', 'Science', 'English']
    marks = [amit['Math'], amit['Science'], amit['English']]

    plt.plot(
        subjects,                  #Values of X axis
        marks,
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Marvellous Line Plot")
    plt.xlabel = "Amit Subjects"
    plt.ylabel = "Marks"
    plt.grid(True)
    plt.legend()
    plt.show()




def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
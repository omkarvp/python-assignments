# 8.	Plot a histogram of Math marks.
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

    plt.hist(
        df['Math'],  # Continuous Data
        bins=5, # Number of group
        edgecolor= "black", # border color
        alpha = 0.8, # transperancy
        rwidth=0.9, # relative width of bars
    )

    plt.title("Marvellous Histogram Plot")
    plt.xlabel = "Marks"
    plt.ylabel = "Frequency"
    plt.show()

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
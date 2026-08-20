# 10.	Plot a boxplot for English marks to check distribution and outliers.
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
    
    # Create boxplot for English marks
    plt.boxplot(df['English'])

    plt.ylabel('English Marks')
    plt.title('Boxplot of English Marks')

    plt.show()

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
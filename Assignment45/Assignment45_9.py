# 9.	Rename the Math column to Mathematics. 
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
    
    # Rename Math column
    df = df.rename(columns={'Math': 'Mathematics'})

    print(df)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
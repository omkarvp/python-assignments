# 1. Normalize the Math scores using Min-Max scaling
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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
    # Create Min-Max scaler
    scaler = MinMaxScaler()

    # Normalize Math scores
    print("Normalize Math scores : ")
    df['Math_Normalized'] = scaler.fit_transform(df[['Math']])

    print(df)

def main():
    MarvellousClassifier()


if __name__ == "__main__":
    main()
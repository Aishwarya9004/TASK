import pandas as pd
if __name__ == "__main__":
    df = pd.read_csv(r"C:/Users/DELL/Downloads/wine.csv")
    print(df)
    red_df = df[df['color'] == "red"]
    print(red_df)
    red_df.to_csv('file1.csv')
    white_df = df[df['color'] == 'white']
    print(white_df)
    white_df.to_csv('file2.csv')



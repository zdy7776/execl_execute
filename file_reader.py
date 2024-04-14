import pandas as pd


def read_execl(file_path):
    df = pd.read_excel(file_path)
    # df = pd.read_excel(file_path, header=0, nrows=1)
    print(type(df))
    print(str(df))
    return str(df)


# read_execl("./caches/input.xlsx")
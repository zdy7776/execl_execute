import pandas as pd


def write_execl(data, save_path):
    df = pd.DataFrame(data)

    df.to_excel(save_path, index=False)


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
#
# write_execl(data=data, save_path="./caches/output.xlsx")

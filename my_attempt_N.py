import json
import pandas as pd


# Load JSON data from a file
def read_json():
    with open("../WORK/simple.json", 'r') as f_obj:
        data = json.load(f_obj)
    convert_json(data)


# convert JSON to excel using pandas
def convert_json(data): 
    df = pd.DataFrame(data)
    df.to_excel("../WORK/convertedJSON.xlsx", index=False)  # 'index' arg false to avoid extra col in excel file


def main():
    read_json()


if __name__ == "__main__":
    main()

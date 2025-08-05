import pandas as pd
from pathlib import Path
import json

def audit_to_df(audit=Path):
    df = pd.read_excel('data/audits/test_audit.xlsx', sheet_name='Report Data 1', skiprows=2)
    return df

def create_csv(df=pd.DataFrame, output_path=Path):
    df.to_csv(output_path)

def parse_json(df):
    df['parsed'] =  df['Event Data'].apply(json.loads)
    df_parsed = pd.json_normalize(df['parsed'])
    # result = pd.concat([df.drop(columns='parsed'), parsed_df], axis = 1)
    return df_parsed

def filter_df(df=pd.DataFrame, operation=list):
    pass

def main():
    # define folder for audits
    folder = Path('data/audits')
    output_path = Path('data/audits.csv')

    for file in folder.iterdir():
        if file.is_file():
            df = audit_to_df(file)
            df_parsed = parse_json(df)
    # load each audit in that folder
    # parse the json in each audit
    # export csv of file data / append to existing
    # export csv of search data / append to existing

if __name__ == "__main__":
    main()
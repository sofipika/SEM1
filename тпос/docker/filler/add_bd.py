import pandas as pd 
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
import time


if __name__ == "__main__":
    time.sleep(2)
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=5432, type=int)
    parser.add_argument('--ip', default='192.168.1.10', type=str)
    parser.add_argument('--ddir', required=True, type=str)
    args = parser.parse_args()

    ddir = Path(args.ddir)
    engine = create_engine(f'postgresql+psycopg2://postgres:postgres@{args.ip}:{args.port}/postgres')
    Session = sessionmaker(bind=engine) 

    with Session() as session:
        for f in ddir.glob("*.csv"):
            df = pd.read_csv(f)
            df.to_sql('hw5634246_' + f.stem, con=engine, if_exists='replace')
            result = engine.execute(f"SELECT * FROM hw5634246_{f.stem}").mappings().all()
            print(*df.columns)
            for r in result:  
                print(*[r[column] for column in df.columns])


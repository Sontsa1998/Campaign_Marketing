from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

def connection():
    engine = create_engine("mssql://Chris_Evan_Noah/Campaign_Marketing?driver=ODBC+DRIVER+17+FOR+SQL+SERVER")
    return engine.connect()

#Fonction d'execution de requetes
def run_query(query):
    con = connection()
    df = pd.read_sql_query(query, con)
    con.close()
    return df
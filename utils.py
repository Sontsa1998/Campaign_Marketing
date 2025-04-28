from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def connection():
    engine = create_engine("mssql://Chris_Evan_Noah/Campaign_Marketing?driver=ODBC+DRIVER+17+FOR+SQL+SERVER")
    return engine.connect()

#Fonction d'execution de requetes
def run_query(query):
    con = connection()
    df = pd.read_sql_query(query, con)
    con.close()
    return df

#Fonction de visualisation de nos données
def data_viz(df, xdata, ydata, xlabel, ylabel, title):
    df.plot(kind='bar', x=xdata, y=ydata, legend=None)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.show()

#fonction de visualisation interactive avec seaborn
def dynamic_Viz(df, xdata, ydata, title):
    fig = px.box(df, x=xdata, y=ydata, color=xdata, hover_name=xdata, title=title )
    fig.show()

def seaborn_graph(df):
    sns.pairplot(df)
    plt.show()
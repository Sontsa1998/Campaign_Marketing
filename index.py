from utils import run_query
import matplotlib.pyplot as plt

def get_all_data_from_database():    
    query = 'SELECT * FROM Clients'
    df = run_query(query)
    return df

#Proportion des clients par status matrimoniale
def proportion_client_statusMatrimoniale():
    query = '''
    SELECT marital_status, count(*) AS Population
    FROM Clients
    GROUP BY marital_status
    ORDER BY Population DESC
    '''
    df = run_query(query)
    return df

#Proportion des clients par education
def proportion_clients_byEducation ():
    query = '''
    SELECT education, count(*) AS Population
    FROM Clients
    GROUP BY education
    ORDER BY Population DESC
    '''
    df = run_query(query)
    return df

#pour chaque category de client par education, quels sont les plus fortunés ? 
def top_3_clients_by_Education():
    query = '''
    WITH cte AS (SELECT id, education, income, ROW_NUMBER() OVER (PARTITION BY education ORDER BY income DESC) AS rn
    FROM Clients
    GROUP BY education, id, income)
    SELECT * from cte 
    WHERE rn < 4
    '''
    df = run_query(query)
    return df

#pour chaque category de client par status matrimoniale, quels sont les plus fortunés ? 
def top_3_clients_by_statusMatrimoniale():
    query = '''
    WITH cte AS (SELECT id, marital_status, income, ROW_NUMBER() OVER (PARTITION BY education ORDER BY income DESC) AS rn
    FROM Clients
    GROUP BY marital_status, id, income)
    SELECT * from cte 
    WHERE rn < 4
    '''
    df = run_query(query)
    return df
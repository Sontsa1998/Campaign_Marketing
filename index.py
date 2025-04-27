from utils import run_query
import matplotlib.pyplot as plt

query = 'SELECT * FROM Clients'
df = run_query(query)
df.plot.bar()
print (df)

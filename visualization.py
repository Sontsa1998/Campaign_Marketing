from index import proportion_client_statusMatrimoniale
from index import proportion_clients_byEducation
from utils import data_viz
from utils import dynamic_Viz

#resultat requete 1 : proportion des clients par situation matrimoniale
###data_viz(df=proportion_client_statusMatrimoniale(), xdata='marital_status', ydata='Population', xlabel='Marital Status', ylabel='Population', title='Proportion des clients par status matrimoniale')

#requete 2 : proportion des clients par Education
###data_viz(df=proportion_clients_byEducation(), xdata='education', ydata='Population', xlabel='Education', ylabel='Population', title='Proportion des clients par Education ')

#requete 3 : proportion des clients par Education
dynamic_Viz(df=proportion_clients_byEducation(), xdata='education', ydata='Population', title='Proportion des clients par Education ')
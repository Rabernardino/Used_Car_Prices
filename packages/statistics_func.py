

import string
import matplotlib.pyplot as plt
import seaborn as sns

def plot_chart(chart_type, x_var, y_var = None, data_src = None, title = None):
    
    plt.subplots(figsize = (12,6))
    sns.set_style('whitegrid')

    if x_var != None:
        x_label = string.capwords(x_var.replace('_', ' '))
    
    else:
        x_label = ''
    
    if y_var != None:
        y_label = string.capwords(y_var.replace('_', ' '))

    else:
        y_label = ''


    if chart_type == 'histogram':

        fig = sns.histplot(x = x_var, data = data_src)
        fig.set_title(f'Histogram - {title}', fontsize = 16)

    elif chart_type == 'boxplot':

        fig = sns.boxplot(x = x_var, y = y_var, data = data_src)
        fig.set_title(f'Boxplot - {title}', fontsize = 16)

    
    fig.set_xlabel(x_label, fontsize = 14)
    fig.set_ylabel(y_label, fontsize = 14)
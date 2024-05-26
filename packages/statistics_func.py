


import matplotlib.pyplot as plt
import seaborn as sns

def histogram_chart(x_var, y_var_label, data_src):

    plt.subplots(figsize = (12,6))
    sns.set_style('whitegrid')

    fig = sns.histplot(x= x_var, data= data_src)
    fig.set_title(f'Distribution of - {data_src[x_var].name.capitalize()}', fontsize=16)
    fig.set_ylabel(f'{y_var_label.capitalize()}', fontsize=14)
    fig.set_xlabel(f'{data_src[x_var].name.capitalize()}')

    return
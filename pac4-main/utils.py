import csv
import matplotlib.pyplot as plt
import pandas as pd
import re
import xlrd

def count_sponsor(sponsor):
    """ Funcio que troba una cadena a la columna 'sponsor' del csv 'covid_approval_polls.csv'.
        L'arxiu es carrega a un dataframe.

    :param sponsor: string
    :return: (n_sponsor, n_url): tupla
    """
    with open('data/covid_approval_polls.csv') as csvf:
        df = pd.read_csv(csvf)
        #print(df.columns)
        n_sponsor = df.groupby('sponsor').size()[sponsor]
        n_url = len(df[df['url'].str.count('https?:\/\/.*\.pdf')>0])
        return n_sponsor, n_url

def count_sponsor_lbl(sponsor):
    """ Funcio que troba una cadena a la columna 'sponsor' del csv 'covid_approval_polls.csv'.
        L'arxiu es llegeix linia a linia.

        :param sponsor: string
        :return: n_sponsor: int
        """
    csvf = csv.reader(open('data/covid_approval_polls.csv'))
    n_sponsor = sum(1 for row in csvf if row[3] == sponsor)
    #n_url = [re.findall(r'Huffington Post', csvf[12]) for row in csvf]
    return n_sponsor
    #print(n_url)

def create_df_from_csv(csvfile):
    """ Funcio que crea un dataframe des de un arxiu csv.

        :param csvfile: arxiu csv
        :return: df: dataframe
        """
    df = pd.read_csv(csvfile)
    return df

def create_df_from_xlxs(xlxsfile):
    """Funcio que crea un dataframe des de un arxiu xlsx.

    :param xlxsfile: arxiu xlsx
    :return: df: dataframe
    """
    df = pd.read_excel(xlxsfile, engine='openpyxl', usecols=['Pollster', 'Banned by 538',
                                                             'Predictive    Plus-Minus', '538 Grade'])
    df.columns = ['pollster', 'Banned by 538', 'Predictive Plus-Minus', '538 Grade']
    return df

def preparacio_ex2(df1, df2):
    """Funcio que fa un join de dos dataframes en la columna 'pollster'.

    :param df1: dataframe
    :param df2: dataframe
    :return: df: merged dataframe
    """
    df = df1.merge(df2, on = ['pollster'])
    df = df[df['Banned by 538']== 'no']
    df = df[df['tracking'] == False]
    return df

def grafica_ex3(df):
    """Funcio que guarda i mostra una grafica de 'df.groupby'.

    :param df: dataframe
    :return: df1: dataframe
    """
    df = df[df['text'].str.count('Trump')>0]
    df = df[df['text'].str.count('coronavirus')>0]
    df['approve'] = (df['approve']/100)*df['sample_size']
    df['disapprove'] = (df['disapprove'] / 100) * df['sample_size']
    plotex3 = df.groupby(['party'])['approve', 'disapprove'].sum().plot(kind = 'bar')
    #plt.xticks(rotation='horizontal')
    df = df.groupby(['party'])['approve', 'disapprove'].sum()
    df1 = pd.DataFrame(df)
    plt.savefig('plotex3.png')
    plt.show(plotex3)
    return df1

def arreglar_notes(df):
    """Funcio que substitueix valors de la columna '538 Grade' per la nota entera o mes baixa.

    :param df: dataframe
    :return: df: dataframe
    """
    df['538 Grade'].replace({'C-':'C', 'A/B':'B', 'D-':'D', 'B-':'B', 'B/C':'C'}, inplace = True)
    return df

def preocupacio_economia(df):
    """Funcio que guarda i mostra una grafica de 'df.groupby'.

    :param df: dataframe
    :return: (very, not_at_all): tupla
    """
    df = df[df['subject'] == 'concern-economy']
    df['very'] = df['very']/100*df['sample_size']
    df['not_at_all'] = df['not_at_all'] / 100 * df['sample_size']
    very = df['very'].sum()
    not_at_all = df['not_at_all'].sum()
    plotex42 = df.groupby(['subject'])['very', 'not_at_all'].sum().plot(kind='bar')
    #plt.xticks(rotation = 'horizontal')
    plt.savefig('plotex42.png')
    plt.show()
    return very, not_at_all

def preocupacio_infeccio(df):
    """Funcio que guarda i mostra una grafica de 'df.groupby'.

    :param df: dataframe
    :return: (very, not_at_all): tupla
    """
    df = df[df['subject'] == 'concern-infected']
    df['very'] = df['very']/100*df['sample_size']
    df['not_at_all'] = df['not_at_all'] / 100 * df['sample_size']
    very = df['very'].sum()/df['sample_size'].sum()*100
    not_at_all = df['not_at_all'].sum()/df['sample_size'].sum()*100
    concern = ['very', 'not at all']
    nconcern = [very, not_at_all]
    plotex43 = plt.bar(concern, nconcern)
    plotex43[1].set_color('orange')
    plt.savefig('plotex43.png')
    plt.show()
    return very, not_at_all

def entrevistes_per_nota(df):
    """Funcio que guarda i mostra una grafica de 'df.groupby'.

    :param df: dataframe
    :return: df: dataframe
    """
    df_per_grade = df.groupby(['538 Grade'])['sample_size'].sum()
    df1 = pd.DataFrame(df_per_grade)
    plotex44 = df.groupby(['538 Grade'])['sample_size'].sum().plot(kind='bar')
    #plt.xticks(rotation='horizontal')
    plt.savefig('plotex44.png')
    plt.show()
    return df1

def nota_numerica(df):
    """Funcio que crea una nova columna i substitueix valors de la columna '538 Grade' per un equivalent
       numeric.

    :param df: dataframe
    :return: df: dataframe
    """
    columna = df['538 Grade'].copy()
    columna.replace({'A':1, 'B':0.5, 'C':0, 'D':-0.5, 'F':-1}, inplace = True)
    df['nota numerica']= columna
    return df

def puntuacio(df):
    """Funcio que crea una nova columna resultant de dues altres columnes del mateix dataframe

    :param df: dataframe
    :return: df: dataframe
    """
    df['puntuacio']=df['nota numerica']+df['Predictive Plus-Minus']
    return df

def puntuacio_mes_gran_que(df):
    """Funcio que aplica un filtre a un dataframe.

    :param df: dataframe
    :return: df: dataframe
    """
    df = df[df['puntuacio']>= 1.5]
    return df

def columna_abans_o_despres(df):
    """Funcio que guarda i mostra una grafica de 'df.groupby' i retorna un dataframe amb resultats agregats.

    :param df: dataframe
    :return: df: dataframe
    """
    df['very'] = df['very'] / 100 * df['sample_size']
    df['somewhat'] = df['somewhat'] / 100 * df['sample_size']
    df['not_very'] = df['not_very'] / 100 * df['sample_size']
    df['not_at_all'] = df['not_at_all'] / 100 * df['sample_size']
    df = df.groupby([df['end_date'] >= '2020-09-01'])['very', 'somewhat', 'not_very', 'not_at_all'].sum()
    df1 = pd.DataFrame(df)
    plotex51a = df.groupby(['end_date'])['very', 'somewhat', 'not_very', 'not_at_all'].sum().plot(kind='bar')
    #plt.xticks(rotation='horizontal')
    plt.savefig('plotex51a.png')
    plt.show()
    return df1

def columna_percentatge_abans_o_despres(df):
    """Funcio que guarda i mostra una grafica de 'df.groupby' i retorna un dataframe amb resultats agregats.

    :param df: dataframe
    :return: df: dataframe
    """
    df['very'] = df['very'] / 100 * df['sample_size']
    df['somewhat'] = df['somewhat'] / 100 * df['sample_size']
    df['not_very'] = df['not_very'] / 100 * df['sample_size']
    df['not_at_all'] = df['not_at_all'] / 100 * df['sample_size']
    df2 = df.groupby([df['end_date'] >= '2020-09-01'])['sample_size','very', 'somewhat', 'not_very', 'not_at_all'].sum()
    df3 = pd.DataFrame(df2)
    df3['not_at_all'] = df3['not_at_all']/df3['sample_size']*100
    df3['very'] = df3['very']/df3['sample_size']*100
    df3['not_very'] = df3['not_very']/df3['sample_size']*100
    df3['somewhat'] = df3['somewhat']/df3['sample_size']*100
    plotex51b = df3.groupby(['end_date'])['very', 'somewhat', 'not_very', 'not_at_all'].sum().plot(kind='bar')
    plt.savefig('plotex51b.png')
    plt.show()
    return df3

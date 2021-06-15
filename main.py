import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=SettingWithCopyWarning)
warnings.filterwarnings(action='ignore', category=UserWarning)


from utils import count_sponsor
from utils import count_sponsor_lbl
from utils import create_df_from_csv
from utils import create_df_from_xlxs
from utils import preparacio_ex2
from utils import grafica_ex3
from utils import arreglar_notes
from utils import preocupacio_economia
from utils import preocupacio_infeccio
from utils import entrevistes_per_nota
from utils import nota_numerica
from utils import puntuacio
from utils import puntuacio_mes_gran_que
from utils import columna_abans_o_despres
from utils import columna_percentatge_abans_o_despres

###Exercici 1

##1.1
print("\nExercici 1:\n___________\n")
print("\t1.1")
recompte_sponsor = count_sponsor('Huffington Post')
print("\tEl patró 'Huffington Post' apareix %s vegades. Mentre que hi ha un total de %s urls en format pfd.\n" %
      (recompte_sponsor))

##1.2
print("\t1.2")
recompte_sponsor_lbl = count_sponsor_lbl('Huffington Post')
print("\tEl patró 'Huffington Post' apareix %s vegades\n" % (recompte_sponsor_lbl))

##1.3
print("\t1.3")
print("\tLa resosta a l'apartat 1.3 es troba a l'arxiu README")


###Exercici 2.

#Creació approval_polls i concern_polls

print("\nExercici 2:\n___________\n")

df = create_df_from_xlxs('data\pollster_ratings.xlsx')
df1 = create_df_from_csv('data\covid_approval_polls.csv')
df2 = create_df_from_csv('data\covid_concern_polls.csv')

approval_polls = preparacio_ex2(df,df1)
print("\tapproval_polls té una llargada de %s files\n" % (len(approval_polls)))

concern_polls = preparacio_ex2(df, df2)
print("\tconcern_polls té una llargada de %s files\n" % (len(concern_polls)))


###Exercici 3.

##3.1

print("\nExercici 3:\n___________\n")
print("\t3.1")

print("\tLa gràfica també s'ha guardat a la carpeta directori amb el nom 'plotex3'. Quan es tanqui la finestra de la\n"
      "\tgràfica, seguirà l'execució del programa i apareixerà la taula amb els valors exactes de la imatge.\n")
#graf_approval = grafica_ex3(approval_polls)
#print(graf_approval)


###Exercici 4.

##4.1

print("\nExercici 4:\n___________\n")


print("\tPer preparar l'exercici, fem els canvis demanats a la columna '538 Grade' de l'arxiu 'concern_polls'\n")
ex_41 = arreglar_notes(concern_polls)
print("\t%s" % (set(ex_41['538 Grade'])))

print("\t4.1")

print("\tHan participat a les entrevistes de 'concern_polls' un total de %s persones.\n" %
      (concern_polls['sample_size'].sum()))

##4.2

print("\t4.2")
print("\tLa gràfica també s'ha guardat a la carpeta directori amb el nom 'plotex42'. Quan es tanqui la finestra de la\n"
      "\tgràfica, seguirà l'execució del programa i apareixern els valors exactes.\n")
#ex42 = preocupacio_economia(concern_polls)
#print("\tVeiem que %s persones estan molt preocupades per l'economia, mentre que %s persones no ho estan gens.\n" %
      #(ex42))

##4.3

print("\t4.3\n")
print("\tLa gràfica també s'ha guardat a la carpeta directori amb el nom 'plotex43'. Quan es tanqui la finestra de la\n"
      "\tgràfica, seguirà l'execució del programa i apareixern els valors exactes.\n")
#ex43 = preocupacio_infeccio(concern_polls)
#print("\tVeiem que un %s per cent dels entrevistats estan molt preocupats per les infeccions, mentre que un %s \n"
      #"\tper cent dels entrevistats no ho estan gens." % (ex43))

##4.4

print("\t4.4\n")
print("\tLa gràfica també s'ha guardat a la carpeta directori amb el nom 'plotex44'. Quan es tanqui la finestra de la\n"
      "\tgràfica, seguirà l'execució del programa i apareixern els valors exactes de l'exercici.\n")
#ex44 = entrevistes_per_nota(ex_41)
print("\t Entrevistes fetes per nota dels entrevistadors:\n")
#print(ex44)
print("\n")


###Exercici 5.

print("\nExercici 5:\n___________\n")

print("\tPer preparar l'exercici, fem els canvis demanats i afegim la variable 'puntuacio' a l'arxiu 'concern_polls'\n"
      "i guardant aquells registres amb una puntuació >= 1.5.\n")
ex5prep = nota_numerica(ex_41)
columna = puntuacio(ex5prep)
mes_gran = puntuacio_mes_gran_que(columna)
print("\nLa nova llista de columnes per l'arxiiu 'concern_polls' és la següent:\n")
print(concern_polls.columns)

##5.1

print("\t5.1\n")
print("\tLa gràfica també s'ha guardat a la carpeta directori amb el nom 'plotex51'. Quan es tanqui la finestra de la\n"
      "\tgràfica (on False és abans i True és després), seguirà l'execució del programa i apareixern els valors exactes\n"
      "de l'exercici.\n")
abans_o_despres = columna_abans_o_despres(mes_gran)
print("\t Nombre de persones entrevistades per nivell de preocupació i en funció de la data:\n")
print("\t False = Abans / True = Després:\n")

print(abans_o_despres)
print("\n")

##5.2

print("\t5.2\n")
print("\tLa gràfica també s'ha guardat a la carpeta directori amb el nom 'plotex52'. Quan es tanqui la finestra de la\n"
      "\tgràfica (on False és abans i True és després), seguirà l'execució del programa i apareixern els valors exactes\n"
      "\tde l'exercici.\n")
perc_abans_o_despres = columna_percentatge_abans_o_despres(mes_gran)
print("\t Percentatge de persones entrevistades per nivell de preocupació i en funció de la data:\n")
print("\t False = Abans / True = Després:\n")

print(perc_abans_o_despres)
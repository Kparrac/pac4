
*NOTA*: 
Per poder fer anar el programa sense incidències s'ha d'utilitzat la comanda 'python3 main.py', si no s'especifica python3
molts errors.

*Exercici 1.

1.1 Obrim el arxiu amb pandas i comptem les vegades que apareix 'Huffington Post' a la columna 'sponsor'. Ho fem així
perquè en un arxiu d'aquesta mida no hi ha massa diferència en carregar un dataframe o no.

1.2 En cas de tenir un arxiu d'1GB, si només hem de fer aquesta operació, és més eficient llegir l'arxiu línia a línia
i programar un sumador cada cop que a una certa columna (la tercera en el nostre cas) compleixi una condició.
* No he pogut programar el regex per la url per que funcionés correctament.

1.3 Si trobem que tenim molts arxius grans, i podem preveure una sobrecàrrega per la nostra cpu, podem implementar un
sistema de multiprocessos. D'aquesta manera repartim el pes dels còmputs.


*Exercici 2.

2.1 Llegim els arxius amb pandas, carregant directament els datasets, ja que per a aconsegir les taules de l'exercici
farem servir la funció merge. Fem servir dues funcions diferents, ja que necessitem una llibreria externa per poder
obrir l'arxiu xlsx.


*Exercici 3.

3.1 En aquest exercici entenc que volem trobar els textos que continguin tant 'Trump' com 'coronavirus', per això aplico
dos filtres un després de l'altre, els dos modificant el dataframe rebut per la funció.


*Exercici 4.

4.1, 4.2 i 4.3 Els resultats es troben a l'arxiu main.


*Exercici 5.

Creem la nova variable que ens demana amb la creació d'una tercera variable (nota numerica).

5.1.a i 5.1.b Es troben a l'arxiu main.

5.2 A les gràfiques podem veure

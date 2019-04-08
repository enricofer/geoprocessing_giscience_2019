# PYTHON

Python è un linguaggio di programmazione potente e divertente, che trova utilizzo sia nello sviluppo di applicazioni web che di software desktop. E' possibile ritrovarlo come interfaccia di programmazione di librerie tipo GDAL/OGR, JTS e GEOS. Le caratteristiche principali sono:

* chiarezza e leggibilità della sintassi
* è orientato alla programmazione ad oggetti ma anche alla programmazione funzionale
* gestione degli errori in fase di esecuzione
* tipi dato dinamici e di alto livello
* codice modulare e riusabile
* disponibilità sterminata di librerie immediatamente disponibili (https://pypi.python.org/pypi)

---

# RISORSE

## Libri

* [Imparare Python, Roberto Allegra](https://www.dropbox.com/s/w35tl07jz9g47xo/Libro_ioProgrammo_122_Imparare_pyton_OK%281%29.pdf?dl=0)
* [Dive into python3](https://www.dropbox.com/s/cwgj1z3lj80qs3g/dive-into-python3.pdf?dl=0)

--

## Tutorial

* [Il tutorial ufficiale di Python](http://docs.python.it/html/tut/tut.html)
* [Pensare da informatico. Versione Python](http://www.python.it/doc/Howtothink/Howtothink-html-it/index.htm)
* [Dive into Python - Python per programmatori esperti](http://it.diveintopython.net/toc/index.html)
* [Google Python Course](https://developers.google.com/edu/python/)

--

## Riferimenti

* [Cheatsheet - riferimento rapido python 3.5](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)
* [Python per esempi](https://github-production-release-asset-2e65be.s3.amazonaws.com/29447438/1da4d7ca-6837-11e6-8ab3-ae7821a7032a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20170615%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20170615T063202Z&X-Amz-Expires=300&X-Amz-Signature=504b5df4c21540c43f13c9fe6bd01a866031acbffff1f6827bf9fb8d6dbf49a7&X-Amz-SignedHeaders=host&actor_id=7544963&response-content-disposition=attachment%3B%20filename%3Dbeginners_python_cheat_sheet_pcc_all.pdf&response-content-type=application%2Foctet-stream )

---

## VERSIONI DEL LINGUAGGIO

Python nel corso della sua evoluzione è arrivato ormai alla sesta release della versione 3 (3.7.3) e la versione 2 non sarà a breve più supportata.
Questo è il motivo principale per la migrazione da QGIS2 a QGIS3.

* QGIS2 > Python 2.7 > librerie Qt4
* QGIS3 > Pyhton 3.6 > librerie Qt5
* [informazioni sulla Migrazione](https://docs.python.org/3/howto/pyporting.html)

---

## DOVE E' PYTHON



Contrariamente ai linguaggi [compilati](https://it.wikipedia.org/wiki/Linguaggio_compilato), che servono a produrre per mezzo di un compilatore un programma in linguaggio macchina, direttamente eseguibile da un microprocessore, Python è un linguaggio [interpretato](https://it.wikipedia.org/wiki/Linguaggio_di_programmazione#Interpretazione), ovvero che deve essere eseguito da un programma interprete.

I programmi in Python sono constituiti da file di testo con estensione .py che contengono le istruzioni da eseguire dall'interprete Python che è un eseguibile che valida il codice per evidenziare errori di sintassi, ovvero difformità dallo standard del linguaggio, ed appunto "interpreta" le istruzioni riga per riga svolgendo le funzionalità richieste con delle procedure interne all'interprete.

Un'altra modalità di funzionamento è quello da console, cioè digitando riga per riga i comandi da eseguire, una modalità utile per testare i comandi o gli ambienti in cui vengono eseguiti i programmi python

--

## LA RIGA DI COMANDO

Ai fini del corso viene utilizzato l'interprete di python  installato assieme a QGIS. Nei sistemi Linux e Macos, che hanno una migliore gestione dei pacchetti di installazione, python è installato come parte del sistema operativo, mentre nei sistemi Windows è installato come applicativo assieme a QGIS, come applicazione e non come parte del sistema operativo. Questo significa che potrebbero coesistere anche molte versioni di Python all'interno della macchina, causando la necessità di configurare opportunamente l'ambiente di esecuzione per evitare conflitti ed errori.

* In Linux e Macos, basta aprire il terminale e digitare `python`  per entrare nell'interprete a riga di comando (oppure `python2` o `python3`)

* In windows bisogna tralasciare la console di sistema, ma andare sul menu di installazione di QGIS e cliccare su *OSGeo4W Shell* e digitare i comandi `py2_env.bat`  o `py3_env.bat`a seconda che si desideri usare la versione 2 o 3 ed a questo punto digitare `python`

--

## CONSOLE

![console](doc\console.png)

QGIS integra python al suo interno, ed oltre ad esporre tutte le funzioni del programma, mette a disposizione una console alternativa, dove può essere eseguito codice python.

La console in QGIS può essere usato anche da riga di comando. L'importante è che alcune "variabili d'ambiente" siano opportunamente configurate. La distribuzione di QGIS contiene una riga di comando opportunamente configurata per l'utilizzo delle librerie OSGEO utilizzate dal programma

---

## PRIMO CODICE

```python
>>> print ("CIAO DA QGIS!") <invio>
```

print è una funzione i cui parametri sono contenuti dalle parentesi ()
Nel nostro caso il parametro è unico ed è costituito da una stringa di testo da stampare sulla console.

---

# Il linguaggio PYTHON

* I tipi di dati

* le variabili

* i tipi strutturati

* il controllo del flusso di esecuzione

* funzioni, moduli e namespaces

* programmazione ad oggetti

---

# I TIPI DI DATI

--

## Numeri

```python
10     #integer (numero intero)
25.45    #float (numero decimale)

# Per trasformare una stringa in numero
# o troncare un float
int("10")
int(34.354)

# L'aritmetica ha una notazione convenzionale
10 + 1
10 * 5
10*(45/3)+8*17

# Divisione tra interi in python 2
5 / 2 #2

# se uno dei numeri è float il risultato è float
10 / 3.0

# questo è equivalente a sopra
10 / float(3)

# in python 3 il risultato è implicito
```

--

## Stringhe

```python
"Ciao da QGIS!"

# Concatenare le stringhe
"Ciao" + " " + "da QGIS!"

# Formattazione di stringhe
"Ciao da %s" % "QGIS!"

# Il testo è racchiuso da virgolette singole o doppie
'Python è "divertente"'

# Stringhe multi-linea
print """Questa stringa
è suddivisa in
varie righe"""

# Caratteri speciale come a capo, la tabulazione o la barra inversa,
# possono essere inseriti per mezzo di una sequenza di escape che inizia
# con una barra inversa "\"

print "Questa stringa\nviene stampata\nin tre righe"
print "C:\\Users\\enrico"

# Si può usare una stringa grezza tralasciando le sequenze di escape
print r"C:\\Users\\enrico"

#Uso del set di caratteri esteso (unicode - UTF8) (Python 2)
print (u"questo è qgis")
```

--

## formattazione delle stringhe

il linguaggio dispone di [funzioni molto potenti](https://pyformat.info/) per assemblare tra loro le stringhe e formattare tipi non stringa (numeri, date)

```python
a = 'Paolo'
b = "Verdi"
c = 172
d = 8.5676776

# concatenazione
print ("il mio cognome è " + b)
print ("mi chiamo "+a+" "+b+" alto "+str(c)" cm ed ho percorso "+str(d)+" km")

# metodo "vecchio"
print ("il mio cognome è %s" % b)
print ("mi chiamo %s %s alto %d cm ed ho percorso %.1f km" % (a,b,c,d))

#metodo "nuovo"
print ("mi chiamo {0} {1} alto {:d} cm ed ho percorso {:.1f} km".format(a,b,c,d))
```

--

## TIPO *Boolean*

```python
True

False (None, [], {})

# operatori
not True # False
True and True # True
True and False # False
False and False # False
False or True # True
not (True or False) and True #False

1 == 1 operatore di uguaglianza
1 != 1 operatore di diversità
2 > 1  maggiore
2 >= 1  maggiore o uguale
1 < 2  minore
1 <= 2  minore o uguale
```

---

# VARIABILI

--

## Variabili

```python

anno = "2017"

anno = 2017

print (anno)

anno_scorso = anno - 1

print (anno_scorso)
```

Le variabili in python hanno non sono "staticamente tipizzate", non devono essere dichiarate prima di usarle ne deve essere dichiarato il tipo. Sono dei contenitori che puntano a oggetti che potenzialmente possono essere di qualunque tipo. per conoscere il tipo dell'oggetto assegnato ad una variabile si usa type

```python
type(anno)

<type 'int'>
```

---

# I TIPI *STRUTTURATI*

--

## Liste

una lista (list) e' un elenco ordinato di elementi

```python
l = [3, 5, 4, 2, 1]
m = [[[0,3],[4,6],[5,7]],[[4,5],[6,8]]]

# Accesso agli elementi per posizione
# il primo elemento è 0, gli indici negativi partono dalla fine

l[0]       #3
l[0:3]     #[3, 5, 4]
l[-1]      #1
l[2:-2]    #[4, 2]
l[3:]      #[2, 1]
l[:-2]     #[3, 5, 4, 2]
m[0][2][0] #5
m[1][1]    #[6,8]
```

la stessa notazione è valida per ricavare sottostringhe

```python
"abcdefghijklmnopqrstuvwxyz"[-5:] # "vwxyz"
```

--

## Dizionari

un dizionario (dict) è un insieme strutturato di dati

```python
d = {
    "chiave1": 10,
    "chiave2": 234.56,
    "chiave2": "contenuto",
    "chiave3": {
        "chiave3_1": "abcdef",
        "chiave3_2": "xyz"
    }
}

d["chiave2"]               # 234.56
d["chiave3"]["chiave3_2"]  # "xyz"
```

--

## Manipolazione dei dati strutturati

```python
l0 = [] # lista vuota
l1 = [1, 2]
l2 = [3, 5, 6]

d0 = {} # dizionario vuoto
d1 = {"nome":"giuseppe", "anni": 50}

l1 + l2         # [1, 2, 3, 5, 6]
l1 + 4 + l3     # TypeError
l1.append(10)   # [1, 2, 3, 5, 6, 10]
l1.append(l2)   # [1, 2, [3, 5, 6]]
3 in l2         # True
3 in l1         # False
len(l1 + l2)    # 5

d1["cognome"] = 'verdi'
d1["anni"] = 60 # {"nome":"giuseppe","anni":60,"cognome":"verdi"}
d1.keys()       # ["cognome", "anni", "nome"]
d1.values()     # ["verdi", 60, "giuseppe"]
len(d1)         # 3
```

---

# Controllo del flusso

--

## IF THEN ELSE

```python
latitude = 51.5
if latitude >= 0:
   zone_letter = 'N'
else:
   zone_letter = 'S'

print zone_letter
```

* l'indentazione è il sistema con cui Python raggruppa le istruzioni
* L'indentazione viene realizzata con spazi o tabulazioni
* ogni riga all'interno di un blocco base dev'essere indentata in ugual misura
* Usare un buon editor di testo per programmatori!

--

## Cicli

```python
for carattere in "abcdefg":
    print (carattere)

for numero in [3, 5, 4, 2, 1]:
    print (numero)

testo = "abcdefg"
while testo:
    testo = testo[:-1]
    print (testo)
```

--

## Gestione delle eccezioni

```python
try:
    print (100/0) #provoca ZeroDivisionError: integer division or modulo by zero
except:
    print ("il codice contenuto in try provoca un errore")

try:
    print (100/0)
except Exception as e:
    print ("il codice contenuto in try provoca l'errore" + str(e))
```

---

# Funzioni, moduli e namespaces

--

## Funzioni esistenti (o predefinite)

```python
# Funzioni esistenti (o predefinite)
print("stampa il numero",4)
sorted([3, 5, 4, 2, 1])
len(l1 + l2)
type(a)

...
```

--

## Definizione della propria funzione

```python
def ZonaUtm(longitudine, latitudine):
    numero_zona = ((longitudine + 180) / 6) % 60 + 1
    if latitude >= 0:
        lettera_zona = 'N'
    else:
        lettera_zona = 'S'
    return '%d%s' % (int(numero_zona), lettera_zona)
```

### Uso della funzione

```python
ZonaUtm(11.55,45)   # 32
```

--

## Namespaces

```python

def funzione1():
    var = 100
    print (var)

var = 50
print (var)
funzione1()
```

output:

```python
50
100
```

verifica dei namespaces:

```python
globals() #simboli accessibili globalmente
locals() #simboli accessibili localmente (all'interno di una funzionec)
```

--

## test sui namespaces

```python
global a
a = 0
test1()

def test1():

    def test2():
        c = 2
        print ('a',a)
        print ('b',b)
        print ('c',c)

    b = 1

    print ('b',b)
    test2()
```

--

## Moduli

```python
# Importa un modulo con chiamata ad una funzione contenuta
import math
math.floor(10.6)

# Importa singoli elementi da un modulo
from os import path
path.join(r'C:\Users', 'Matt')
```

l'organizzazione modulare è una delle caratteristiche del linguaggio. I moduli possono essere:

* predefiniti, già compresi nella [dotazione di base del linguaggio](https://docs.python.org/3/library/index.html)
* esterni, contenuti nei path di sistema di Python (PATH, PYTHONPATH). Possono essere preimportati o [importati da internet](https://pypi.python.org/pypi?%3Aaction=browse) tramite pip/setuptools
* definiti dall'utente in sottocartelle

--

## Uso dei moduli esterni

E' possibile usare moduli esterni configurando opportunamente la variabile d'ambiente PYTHONPATH in modo che essa punti ad una cartella contente il codice del modulo

Oppure si può depositare manualmente la cartella contente il modulo python dentro la cartella "site-packages"

A sua volta il modulo può dipendere da altri moduli python.

La comunità Python ha organizzato un repository dei moduli correntemente utilizzabili da python: https://pypi.python.org/pypi Il repository è utilizzabile tramite il comando [pip](https://pip.pypa.io/en/stable/installing/)

```
pip install [nome pacchetto]
```

Il comando provvede ad installare il pacchetto desiderato insieme alle sue dipendenze nella versione stabilita dai *"requirements"* del modulo, aiutando il programmatore a superare i conflitti tra versioni diverse dei pacchetti installati.

---

# Programmazione ad oggetti

--

# Classi ed istanze

* Classe
  * tipo di dato composto definito dall'utente in metodi ad attributi.
* Istanziare
  * creare un'oggetto di una determinata classe.
* Istanza
  * un'oggetto creato che appartiene ad una classe.
* Membri di una classe
  * Metodi
    * funzioni che costituisce un comportamento dell'istanza
  * Attributi
    * valori attribuiti ad un'istanza.
* Costruttore
  * metodo usato per definire nuovi oggetti.

--

## definizione di classe e membri

```python
class rettangolo:

   l = 0
   h = 0

   def __init__(self, l, h):
      self.l = l
      self.h = h

   def area(self)
      return self.l*self.h

   def perimetro(self)
      return(self.l+self.h)*2

   def scala(self, scala)
      self.l = self.l*scala
      self.h = self.h*scala
```

--

## instanziare una classe

Una volta definita una classe è possibile .....

```python
 r = rettangolo(10,5) #istanziazione di un oggetto rettangolo
 r.area()             #50
 r.scala(2)
 r.perimetro()        #60
 r.l                  #20
 r.h                  #10
```

--

## Ereditarietà

è la capacità di definire una nuova classe come versione modificata di una classe già esistente

```python
class stanza:
    def __init__(self, lung, larg)
        self.lung = lung
        self.larg = larg
        self.nome = "stanza"

    def nome(self):
        return self.nome

    def area(self):
        return self.lung * self.larg

class cucina(stanza):
    def __init__(self, lung, larg)
        super().__init__(lung, larg)
        self.nome = "cucina"

class camera(stanza):
    def __init__(self, lung, larg, abitante)
        super().__init__(lung, larg)
        self.nome = "bagno"
        self.abitante = abitante

class edificio:
    def __init__(self, stanze)
        self.stanze = stanze

    def area_tot(self):
        area = 0
        for stanza in self.stanze:
            area += stanza.area()
        return area

    def abitanti(self):
        ab = 0
        for stanza in stanze:
            if hasattr(stanza,'abitante')
                ab += 1
        return ab
```

--

## ispezione degli oggetti

individuazione del tipo di oggetto

```python
type(oggetto)
```

lista dei membri di un' oggetto

```python
dir(oggetto)
```

restituzione di un attributo di un oggetto con il suo nome

```python
getattr(oggetto,'membro')
```

test se un attributo è presente nell'oggetto

```python
hasattr(oggetto,'membro')
```

---

# PyQGIS

--

## QgisInterface

QGIS è programmato in modo modulare in C++ ed espone classi e metodi di funzionamento in PyQGIS

```python
# iface è l'oggetto principale di QGIS da cui derivano
# tutti gli altri oggetti che ne permettono il funzionamento
# è un "singleton" un oggetto con unica istanza
# della classe QgisInterface, istanziato come oggetto iface
iface.activeLayer().name()

# la maggior parte dei metodi richiamano altri oggetti
iface.activeLayer()

# quali metodi o attributi per un'oggetto:
dir(iface.activeLayer())
```

https://qgis.org/api/classQgisInterface.html

---

# Esercitazione 1

calcolo delle abbreviazioni del nome e del cognome del codice fiscale italiano:

* scomposizione di una stringa in vocali e consonanti
* uso delle consonanti in successione, e se non sufficienti uso delle vocali in successione

--

```python
# -*- coding: utf-8 -*-
'''
CORSO DI GEOPROCESSING - MASTER IN GISSCIENCE
calcolo delle abbreviazioni del nome e cognome del codice fiscale
'''

import string

VOCALI = [ 'A', 'E', 'I', 'O', 'U' ]
CONSONANTI = list(set(list(string.ascii_uppercase)).difference(VOCALI))

def scomposizione(stringa):
    '''
    scomposizione nelle liste di consonanti e vocali che compongono la stringa in input
    '''
    stringa = stringa.upper().replace(' ', '')

    consonanti = []
    for car in stringa:
        if car in CONSONANTI:
            consonanti.append(car)

    vocali = [ car for car in stringa if car in VOCALI ]
    return consonanti, vocali

def abbreviazione(stringa):
    scomposizione_in_consonanti, scomposizione_in_vocali  = scomposizione(stringa)
    sequenza = scomposizione_in_consonanti
    while len(sequenza) < 3: #se la lunghezza è meno di 3 significa che le consonanti non bastano e servono le vocali
        try: # pop toglie alla lista il primo elemento e lo restituisce
            sequenza.append(scomposizione_in_vocali.pop(0))
        except: # appende X per stringhe brevi
            sequenza.append('X')
    return ''.join(sequenza[:3]) # trasformazione della lista risultante in stringa


nomi_da_abbreviare = ['Paolo', 'Riccarco', 'Alessia', 'Luisa', 'Ada', 'Liu', 'Bo']

for nome in nomi_da_abbreviare:
    print (nome, abbreviazione(nome))
```

[esercitazione1.py](py/esercitazione1.py)

---

# Esercitazione 2 e 3

scrittura e lettura di un file di testo

--

## Scrittura

```python
'''
CORSO DI GEOPROCESSING - MASTER IN GISSCIENCE
salvataggio di una stringa ad un file di testo
'''

import os

testo = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Ut laoreet sem pellentesque ipsum rutrum consequat. Nunc iaculis tempor aliquet.
Fusce imperdiet pharetra tellus, ut commodo lacus gravida et.
'''

destinazione = r"C:\Users\ferregutie\Downloads"

text_file = open(os.path.join(destinazione, 'mio_file.txt'), 'w')
text_file.write(testo)
text_file.close()
```

[esercitazione2.py](py/esercitazione2.py)

```python



--

## Lettura

```python
'''
CORSO DI GEOPROCESSING - MASTER IN GISSCIENCE
lettura di una stringa da un file di testo
'''

import os
#from esercitazione2 import destinazione
destinazione = r"C:\Users\ferregutie\Downloads"


text_file = open(os.path.join(destinazione, 'mio_file.txt'), 'r')
testo = text_file.read()
text_file.close()

print (testo
```

[esercitazione3.py](py/esercitazione3.py)

---

# Esercitazione 4

stampare un'albero di files e directory. uso delle funzioni os:

* [os.path()](https://docs.python.org/3.6/library/os.path.html)
* [os.walk()](https://docs.python.org/3.6/library/os.html#os.walk)
* [os.listdir()](https://docs.python.org/3.6/library/os.html#os.listdir)

--

```python
'''
CORSO DI GEOPROCESSING - MASTER IN GISSCIENCE
procedura per stampare l'albero di files e directory
'''

import os

dir_sorgente = r"inserire un path"

print ("\nmetodo1")
for root, dirs, files in os.walk(dir_sorgente):
    for file in files:
        print(os.path.join(root,file))

print ("\nmetodo2")
def attraversa_dir(path, livello=0):
    file_e_dir = os.listdir(path)
    for elem in file_e_dir:
        spaziatura =' '*livello*4
        if os.path.isdir(os.path.join(path,elem)):
            print (spaziatura + '['+elem+']')
            attraversa_dir(os.path.join(path,elem), livello=livello + 1)
            print ()
        else:
            print (spaziatura+elem)

attraversa_dir(dir_sorgente)
```

[esercitazione4.py](py/esercitazione4.py)

---

# Esercitazione 5

calcolo della lunghezza di un segmento espresso come lista di punti con metodi diversi:

--

```python
'''
CORSO DI GEOPROCESSING - MASTER IN GISSCIENCE
calcolo della lunghezza di un segmento espresso come lista di punti
'''
import math

def lunghezza(segmento):
    lunghezza_tot = 0
    for indice in range(0, len(segmento)):
        if indice == 0:
            pass
        else:
            x2 = segmento[indice][0]
            x1 = segmento[indice-1][0]
            y2 = segmento[indice][1]
            y1 = segmento[indice-1][1]
            lunghezza_tot += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return lunghezza_tot

def lunghezza_elegante(segmento):
    lunghezza_tot = 0
    for indice, p2 in enumerate(segmento):
        if indice == 0:
            pass
        else:
            lunghezza_tot += math.hypot(p2[0]-p1[0], p2[1]-p1[1])
        p1 = p2
    return lunghezza_tot

def lunghezza_pitonica(segmento):
    diffpt = lambda p: (p[0][0]-p[1][0], p[0][1]-p[1][1])
    lista_diff = map (diffpt, zip(segmento[:-1],segmento[1:]))
    lunghezza_tot = sum(math.hypot(*d) for d in lista_diff)
    return lunghezza_tot

polilinea = [[1.3,3.6],[4.5,6.7],[5.7,6.1],[2.9,0.6],[3.4,2.1],[9.5,2.7]]

print ("lunghezza",lunghezza(polilinea))
print ("lunghezza_elegante",lunghezza_elegante(polilinea))
print ("lunghezza_pitonica",lunghezza_pitonica(polilinea))

for nome_funzione in ['lunghezza', "lunghezza_elegante", "lunghezza_pitonica"]:
    print (nome_funzione, globals()[nome_funzione](polilinea))
```

[esercitazione5.py](py/esercitazione5.py)

# PyQt e PyQGIS

QGIS è un'applicazione open source multipiattaforma (è disponibile per tutti i principali sistemi operativi) costruita per mezzo del framework di programmazione Qt
QGIS espone per mezzo di un'interfaccia di programmazione (API) le classi ed i metodi di funzionamento,
Qt e QGIS dispongono di librerie di collegamento a PYTHON (*bindings*) denominate PyQt e PyQGIS che consentono il controllo e la propgrammazione dell'applicazione per mezzo di codice interpretato in python

* QGIS2
  * Python 2.7/Qt 4
* QGIS3
  * Python 3.5/Qt 5

--

## Qt

Qt è un framework applicativo open-source sviluppato da Nokia per costruire interfacce utente grafiche (GUI) e sviluppare software. Qt è utilizzato in programmi come Google Earth, Virtual Box, Skype, Autodesk e Android. QGIS stesso è costruito con Qt. L'utilizzo di un framework applicativo come Qt velocizza il ciclo di sviluppo di un'applicazione e consente di sviluppare applicazioni multi-piattaforma.

### PyQt

il modulo di collegamento (*bindings*) si chiama PyQt e può essere importato in un programma Python per controllare i widget dell'interfaccia utente
[moduli di Qt](http://doc.qt.io/qt-4.8/modules.html)
[API di PyQt](http://pyqt.sourceforge.net/Docs/PyQt4/modules.html)

--

## PyQgis

![diagramma delle classi](doc/diagramme_principal_low.png)

[diagramma](https://raw.githubusercontent.com/webgeodatavore/qgis-class-diagram/master/diagramme_principal.png)

---

## PyQGIS - classi fondamentali

[documentazione API in C++](https://qgis.org/api)
[documentazione API in python](http://python.qgis.org/api)

* [QgisInterface](https://qgis.org/api/classQgisInterface.html): riferimenti dell'interfaccia utente:
* [QgsProject.instance()](https://qgis.org/api/classQgisInterface.html): è un oggetto singolare (singleton) e gestisce l'oggetto progetto corrente. incorpora [QgsMapLayerRegistry](https://qgis.org/api/2.18/classQgsMapLayerRegistry.html) di QGIS2
* [QgsMapCanvas()](https://qgis.org/api/classQgsMapCanvas.html): è accessibile da QgisInterface().mapCanvas() e gestisce la visualizzazione dei layer: sistemi di riferimento, zoom/pan, mapTools etc...
* [QgsLayerInterface()](http://qgis.org/api/2.18/classQgsLegendInterface.html): accessibile da QgisInterface().layerInterface() gestisce la legenda dei layers
* [QgsMapLayer()](https://qgis.org/api/classQgsMapLayer.html): si articola in QgsVectorLayer() e QgsRasterLayer() e gestisce la manipolazione dei layers
* [QgsFeature()](https://qgis.org/api/classQgsFeature.html): gestione delle singole entità in geometria e attributi
* [QgsGeometry()](https://qgis.org/api/classQgsGeometry.html): permette la manipolazione delle geometrie

---

# PyQgis in pratica

--

## Caricamento di Progetti e Layers

* [caricamento di un progetto](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadproject.html)
* [caricamento di un layer vettoriale](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html#vector-layers)
* [caricamento di un layer raster](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html#raster-layers)
* [inserimento di un layer nel progetto corrente](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html#qgsproject-instance)

```python
project = QgsProject.instance() # l'oggetto è instanziato, viene usata l'istanza creata da QGIS
project.clear() #equivale a nuovo progetto
project.read('path ad un progetto')

vectorLayer = QgsVectorLayer('data_source', 'layer_name', 'provider_name') #provider_name = 'ogr' per sorgenti dati convenzionali
rasterLayer = QgsRasterLayer('data_source', 'layer_name', 'provider_name') #provider_name = 'gdal' per sorgenti dati convenzionali

QgsProject.instance().addMapLayer(vectorLayer) #QgsMapLayerRegistry
```

--

## Layers Vettoriali - acceso alle features

[Uso dei layers vettoriali](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html#)

```python
#CARICAMENTO
layer = QgsVectorLayer('data_source', 'layer_name', 'provider_name') #caricamento
layer = iface.activeLayer() #layer correntemente attivo sulla legenda

#PROPRIETA' DEL LAYER
print (layer.extent()) #estensioni del layer

for field in layer.pendingFields():
    print (field.name(), field.typeName()) #stampa dei campi del layer

#ITERAZIONE
for feature in layer.getFeatures(): #tutte le feature del layer
    #qualinque azione da iterare per ogni feature

for feature in layer.selectedFeatures(): #tutte le features attualmente selezionate
    #qualinque azione da iterare per ogni feature

exp = QgsExpression("toponimo ILIKE '%lago%'")
request = QgsFeatureRequest(exp)
for feature in layer.getFeatures(request): #solo le feature che corrispondono all'espressione
    #qualinque azione da iterare per ogni feature
```

--

## Layers Vettoriali - oggetto QgsFeature

```python
#PROPRIETA'
feature.geometry() # la geometria legata alla feature (QgsGeometry)
feature['toponimo'] # accesso al campo "toponimo"
feature[3] # accesso al terzo campo
feature.id() #identificativo interno univoco ($id in espressioni)

#CREAZIONE
feature = QgsFeature() #creazione di una feature vuota senza definizioni dei campi #bisogna crearli ex novo
feature = QgsFeature(layer.pendingFields()) #creazione di una feature contente i campi del layer

#MODIFICA
feature.setAttribute('area', 100.0) #settaggio del campo 'area' con il valore 100.0
feature.setAttribute(4, 100.0) #settaggio del quarto campo con il valore 100.0
feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(123, 456)))
```

--

## Layers Vettoriali - modifica

```python
#PREPARAZIONE ALLE MODIFICHE
layer.startEditing() #preparazione dell'edit buffer per la registrazione delle modifiche

#NUOVE FEATURES
layer.addFeature(feature)

#CANCELLAZIONE FEATURES
layer.deleteFeature(feature.id())

#MODIFICA FEATURES ESISTENTI
layer.changeGeometry(fid, geometry)
layer.changeAttributeValue(fid, fieldIndex, value)
oppure una volta ottenuta la feature desiderata
feature.setAttribute('area', 100.0)
feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(123, 456)))

#AGGIUNTA ATTRIBUTI
layer.addAttribute(QgsField("mytext", QVariant.String))

#CANCELLAZIONE ATTRIBUTI
layer.deleteAttribute(indice_campo)

#FINE DELLE MODIFICHE
layer.commitCHanges() #scrittura sulla sorgente dati delle modifiche effettuate
layer.rollbackChanges() #cancellazione delle modifiche effettuate
```

--

## layers vettoriali - oggetto geometria

[geometria WKT - Well-Known Text](https://it.wikipedia.org/wiki/Well-Known_Text)

[geometria geojson](http://geojson.org/)

```python
#METODI COSTRUTTORI
geom = QgsGeometry()
geom = QgsGeometry.    fromPointXY (QgsPointXY(12,45))

geom = QgsGeometry.fromWKT('POINT(12 45)')
geom = QgsGeometry.fromWKT('POLYGON((1 1,5 1,5 5,1 5,1 1),(2 2, 3 2, 3 3, 2 3,2 2))')

#MANIPOLAZIONE
geom2 = geom1.simplify(2.0)
geom3 = geom1.buffer(5)
geom4 = geom1.centroid()
geom5 = geom1.clipped(QgsRectangle(1,1,4,6))
geom6 = intersection(geom1)

#INTERROGAZIONE
geom1.isGeosValid() #verifica correttezza geometrica
geom1.intersects(geom2) #boolean True or False
geom1.contains(geom2)
geom1.within(geom2)
geom1.length() # Double lunghezza di un segmento
geom.distance(geom2) #double distanza minima tra due geometrie

#TRASFORMAZIONE
geom1.asWkt() trasformazione in WKT
geom1.asJson() trasformazione in oggetto geometria di geojson
```

---

# esercitazioni di personalizzazione con python

* script
* funzioni personalizzate nel calcolatore di espressioni
* script di processing

[Dataset di esempio](doc/dataset.zip)

---

## scripts

![console](doc/console-script.png)

--

### funzione per variare la trasparenza di un layer

```python
#versione per QGIS2
def trasp(t=50):
    layer = iface.mapCanvas().currentLayer()
    if layer.layerTransparency() == t:
        layer.setLayerTransparency(0)  # int tra 0 e 100
    else:
        layer.setLayerTransparency(t)
    iface.mapCanvas().refresh()
```

```python
#versione per QGIS3
def trasp(t=0.5):
    layer = iface.activeLayer()
    if layer.opacity() == t:
        layer.setOpacity(1)  # double tra 0 e 1
    else:
        layer.setOpacity(t)
    iface.mapCanvas().refresh()
```

--

### procedura per stampare i dettagli di un layer

```python
#versione per QGIS2
from qgis.core import QGis, QgsPoint
#layer = iface.addVectorLayer("/path.shp", "nome", "ogr")
layer = iface.activeLayer() #caricamento
if not layer or not layer.isValid():
  print "Layer non valido!"
else:
    #QgsMapLayerRegistry.instance().addMapLayer(layer) #registrazione
    informazioni=[]
    for feature in layer.getFeatures(): #accesso alle features
        info = [feature.id()]
        geom = feature.geometry()
        if geom.type() == QGis.Point:
            info.append("distanza")
            info.append(geom.distance(QgsGeometry.fromPoint(QgsPoint(0.0,0.0))))
        elif geom.type() == QGis.Line:
            info.append("Lunghezza")
            info.append(geom.length())
        elif geom.type() == QGis.Polygon:
            info.append("Area")
            info.append(geom.area)
        info += feature.attributes()
        informazioni.append(info)
    print informazioni
```

```python
#versione per QGIS3
from qgis.core import  QgsWkbTypes, QgsPoint
layer = iface.activeLayer() #caricamento
if not layer or not layer.isValid():
  print ("Layer non valido!")
QgsProject.instance().addMapLayer(layer) #registrazione
informazioni=[]
for feature in layer.getFeatures(): #accesso alle features
    info = [feature.id()]
    geom = feature.geometry()
    if geom.type() ==  QgsWkbTypes.Point:
        info.append("distanza")
        info.append(geom.distance(QgsPoint(0,0)))
    elif geom.type() ==  QgsWkbTypes.LineString:
        info.append("Lunghezza")
        info.append(geom.length())
    elif geom.type() ==  QgsWkbTypes.Polygon:
        info.append("Area")
        info.append(geom.area)
    info += feature.attributes()
    informazioni.append(info)
print (informazioni)
```

---

## funzioni personalizzate

[Documentazione ufficiale](https://docs.qgis.org/2.18/en/docs/user_manual/working_with_vector/expression.html#function-editor)
![expressions](doc/expressions.png)

--

## funzione booleana vera per feature selezionate

```python
from qgis.utils import iface

@qgsfunction(args=0, group='Custom', usesgeometry=False)
def isSelected(value1,feature, parent):
    selected_ids = []
    for f in iface.activeLayer().selectedFeatures():
        selected_ids = f.id()
    return feature.id() in selected_ids
```

--

## funzione che restituisce le coordinate del centro dello schermo

```python
from qgis.utils import iface
from qgis.core import QgsGeometry, QgsPoint

@qgsfunction(args=0, group='Custom')
def mapCenter(value1,feature, parent):
  x = iface.mapCanvas().extent().center().x()
  y = iface.mapCanvas().extent().center().y()
  return QgsGeometry.fromPointXY(QgsPointXY(x,y))
```

---

## script di processing

[documentazione ufficiale](https://docs.qgis.org/2.8/en/docs/user_manual/processing/scripts.html#writing-new-processing-algorithms-as-python-scripts)
[tutorial per QGIS2](http://www.qgistutorials.com/it/docs/processing_python_scripts.html)

![processing](doc/processing.png)

--

## Dai Modelli agli script di Processing

i modelli di processing possono venire esportati come script in python soccessivamente modificabili:

```python
##Points2Polygon=name
##TABLEFIELD_GROUPBY=fieldVECTORLAYER_POINTSLAYER
##TABLEFIELD_ORDERBY=fieldVECTORLAYER_POINTSLAYER
##VECTORLAYER_POINTSLAYER=vector
##mypolygons=output vector
outputs_QGISPOINTSTOPATH_1=processing.runalg('qgis:pointstopath', VECTORLAYER_POINTSLAYER,TABLEFIELD_GROUPBY,TABLEFIELD_ORDERBY,None,None,None)
outputs_QGISLINESTOPOLYGONS_1=processing.runalg('qgis:linestopolygons', outputs_QGISPOINTSTOPATH_1['OUTPUT_LINES'],mypolygons)
```

Modelli e Script di Processing possono essere importati dal repository di QGIS

--

## creazione di un nuovo layer dalle feature selezionate

In QGIS3 il framework è stato completamente riscritto in C++ per esigenze prestazionali e per consentire l'esecuzione in background. Però l'API è completamente cambiata, più complessa, poco documentata e soggetta a futuri cambiamenti. Quindi facciamo riferimento per processing ancora al framework di QGIS2

```python
##Vector=group
##input=vector
##output=output vector

from qgis.core import *
from processing.tools.vector import VectorWriter

vectorLayer = processing.getObject(input)

provider = vectorLayer.dataProvider()

writer = VectorWriter(output, None, vectorLayer.pendingFields(),
                      provider.geometryType(), vectorLayer.crs())

features = processing.features(vectorLayer)
for feat in features:
    writer.addFeature(feat)

del writer
```

--

[dtm](py/antelao.tif)
[06-rasterProcessing.py](doc/06-rasterProcessing.py)

```python
##dtm=raster
##input=vector
##output=output vector

from PyQt4.QtCore import QVariant
from qgis.core import *
from processing.tools.vector import VectorWriter

vectorLayer = processing.getObject(input)
dtmLayer = processing.getObject(dtm)

fields=QgsFields()
fields.append(QgsField('elevation', QVariant.Double))
fields.append(QgsField('id_poly', QVariant.Int))

pointSamplewriter = VectorWriter(output, None, fields,
                      QgsWKBTypes.Point, vectorLayer.crs())

features = processing.features(vectorLayer)
for feat in features:
    for point in feat.geometry().asPolyline():
        elevFeat = QgsFeature(fields)
        elevValue = dtmLayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue).results()[1]
        elevFeat['elevation'] = elevValue
        elevFeat['id_poly'] = feat.id()
        elevGeom = QgsGeometry.fromPoint(point)
        elevFeat.setGeometry(elevGeom)
        pointSamplewriter.addFeature(elevFeat)

del pointSamplewriter
```

--

script di processing modificato nella lezione 3 per misurare i punti lungo le polilineee. attenti a non definire misure <= 0
[07_raster_proc_QGIS3.py](doc/08_raster_proc_QGIS3.py)

```python
##dtm=raster
##input=vector
##measure=number 50
##output=output vector

from PyQt4.QtCore import QVariant
from qgis.core import *
from processing.tools.vector import VectorWriter

vectorLayer = processing.getObject(input)
dtmLayer = processing.getObject(dtm)
measureStep = measure

fields=QgsFields()
fields.append(QgsField('id_poly', QVariant.Int))
fields.append(QgsField('elevation', QVariant.Double))
fields.append(QgsField('step', QVariant.Double))

pointSamplewriter = VectorWriter(output, None, fields,
                      QgsWKBTypes.Point, vectorLayer.crs())

features = processing.features(vectorLayer)
for feat in features:
    currentLen = 0
    while currentLen < feat.geometry().length():
        point = feat.geometry().interpolate(currentLen).asPoint()
        elevFeat = QgsFeature(fields)
        elevValue = dtmLayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue).results()[1]
        elevFeat['elevation'] = elevValue
        elevFeat['step'] = currentLen
        elevFeat['id_poly'] = feat.id()
        elevGeom = QgsGeometry.fromPoint(point)
        elevFeat.setGeometry(elevGeom)
        pointSamplewriter.addFeature(elevFeat)
        currentLen += measureStep

del pointSamplewriter
```

--

script di processing precedente modificato per il funzionamento in QGIS3
[08_raster_proc_QGIS3.py](doc/08_raster_proc_QGIS3.py)

```python
from PyQt5.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterFeatureSink,
                       QgsFields,QgsField,QgsFeature,QgsGeometry, QgsWkbTypes, QgsRaster)


class DTMProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT_LAYER = 'OUTPUT_LAYER'
    INPUT_LAYER = 'INPUT_LAYER'
    DTM_LAYER = 'DTM_LAYER'
    MEASURE_VALUE = 'MEASURE'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return DTMProcessingAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'measure_elev_on_dtm'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Measure elevation on dtm')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Example scripts')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'examplescripts'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.addParameter(QgsProcessingParameterRasterLayer(
            self.DTM_LAYER,
            self.tr("DTM layer")))
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.INPUT_LAYER,
            self.tr("Input layer"),[QgsProcessing.TypeVectorLine]))
        self.addParameter(QgsProcessingParameterNumber(
            self.MEASURE_VALUE,
            self.tr("Measure step size"),
            QgsProcessingParameterNumber.Integer,50))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT_LAYER,
            self.tr("Output point layer"),
            QgsProcessing.TypeVectorPoint))

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """


        vectorLayer = self.parameterAsSource(parameters, self.INPUT_LAYER, context)
        dtmLayer = self.parameterAsRasterLayer(parameters, self.DTM_LAYER, context)
        measureStep = self.parameterAsInt (parameters, self.MEASURE_VALUE, context)


        fields=QgsFields()
        fields.append(QgsField('id_poly', QVariant.Int))
        fields.append(QgsField('elevation', QVariant.Double))
        fields.append(QgsField('step', QVariant.Double))


        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT_LAYER, context, fields, QgsWkbTypes.Point, vectorLayer.sourceCrs())


        features = vectorLayer.getFeatures() #QgsProcessingUtils.getFeatures(vectorLayer, context)
        for feat in features:
            currentLen = 0
            while currentLen < feat.geometry().length():
                point = feat.geometry().interpolate(currentLen).asPoint()
                elevFeat = QgsFeature(fields)
                elevValue = dtmLayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue).results()[1]
                elevFeat['elevation'] = elevValue
                elevFeat['step'] = currentLen
                elevFeat['id_poly'] = feat.id()
                elevGeom = QgsGeometry.fromPointXY(point)
                elevFeat.setGeometry(elevGeom)
                sink.addFeature(elevFeat, QgsFeatureSink.FastInsert)
                currentLen += measureStep

        return {self.OUTPUT_LAYER: dest_id}
```

--

## creazione di un grafo origine/destinazione in QGIS2

```python
##Linee=vector line
##nodi=output vector
##grafo=output vector

from qgis.core import QgsGeometry, QgsField, QgsFeature, QGis
from PyQt4.QtCore import QVariant
from processing.tools.vector import VectorWriter

def aggiungi_nodo(nuovo_nodo):
    for i,nodo in enumerate(lista_nodi):
        if nodo.compare(nuovo_nodo):
            return i
    lista_nodi.append(nuovo_nodo)
    return len(lista_nodi)-1

linee_layer = processing.getObject(Linee)

grafo_fields = [
    QgsField("rif_id", QVariant.Int),
    QgsField("in_id", QVariant.Int),
    QgsField("out_id", QVariant.Int)
]
grafo_writer = VectorWriter(grafo, None, grafo_fields, QGis.WKBMultiLineString, linee_layer.crs())

nodi_fields = [QgsField("nodo_id", QVariant.Int)]
nodi_writer = VectorWriter(nodi, None, nodi_fields, QGis.WKBMultiPoint, linee_layer.crs())

i = 0
n = linee_layer.featureCount()
lista_nodi = []
progress.setText("Individuazione dei vertici degli archi del grafo ...")

for k,feature in enumerate(processing.features(linee_layer)):
    progress.setPercentage(int(100*i/n))
    i += 1
    lista_vertici = feature.geometry().asPolyline()
    grafo_feature = QgsFeature()
    attributi =[feature.id()]
    grafo_feature.setGeometry(feature.geometry())
    for campo, estremo in ({1:lista_vertici[0],2:lista_vertici[-1]}).items():
        id_nodo = aggiungi_nodo(estremo)
        attributi.append(id_nodo)
    grafo_feature.setAttributes(attributi)
    grafo_writer.addFeature(grafo_feature)

i = 0
n = len(lista_nodi)
progress.setText("Creazione dei nodi ...")

for i, nodo in enumerate(lista_nodi):
    progress.setPercentage(int(100*i/n))
    nodo_feature = QgsFeature()
    nodo_feature.setAttributes([i])
    nodo_feature.setGeometry(QgsGeometry.fromPoint(nodo))
    nodi_writer.addFeature(nodo_feature)

del nodi_writer
del grafo_writer

`
```

--

## uso del framework processing

[documentazione ufficiale] (https://docs.qgis.org/2.18/en/docs/user_manual/processing/console.html)

```python
>>> import processing
# eseguire un algoritmo
>>> processing.runalg('nome algoritmo', par1, par2, ..., parN)

# lista degli algoritmi disponibili
>>> processing.alglist()

# lista dei parametri necessari per runalg
>>> processing.alghelp('nome algoritmo')
```

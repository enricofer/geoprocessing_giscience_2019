'''
CORSO DI GEOPROCESSIGN - MASTER IN GISSCIENCE
salvataggio di una stringa ad un file di testo
'''

import os

testo = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Ut laoreet sem pellentesque ipsum rutrum consequat. Nunc iaculis tempor aliquet. 
Fusce imperdiet pharetra tellus, ut commodo lacus gravida et.
'''

destinazione = r"C:\Users\paolo\Documenti"

text_file = open(os.path.join(destinazione, 'mio_file.txt'), 'w')
text_file.write(testo)
text_file.close()

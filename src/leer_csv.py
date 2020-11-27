import csv

def leer_csv_dictionary():
    ruta_archivo = 'data/empleados.csv'

    with open(ruta_archivo, 'r') as archivo_csv:
        lector_dict = csv.DictReader(archivo_csv)

        for mapa in lector_dict:
            print(mapa)

def leer_csv():
    ruta_archivo = 'data/empleados.csv'

    with open(ruta_archivo, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)

        for linea in lector:
            print(linea)

if __name__ == '__main__':
    leer_csv()
    leer_csv_dictionary()
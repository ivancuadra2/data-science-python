# import csv





# class Persona:
#     def __init__(self, nombre, apellido, fecha_nacimiento, sexo, altura):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.fecha_nacimiento = fecha_nacimiento
#         self.sexo = sexo
#         self.altura = altura

#     def __str__(self):
#         return f"{self.nombre} {self.apellido}, nacido el {self.fecha_nacimiento}, sexo: {self.sexo}, altura: {self.altura}m"
    
    


# def main():
#     print("Hola, mundo!")



#     # Ejemplo de uso de la clase Persona
#     persona = Persona("Juan", "Pérez", "01/01/1990", "M", 1.75)
#     print(persona)

#     # numero = int(input("Ingrese un número: "))
#     # print(f"El número ingresado es: {numero}")

#     read_csv()

#     # for i in range(numero):
#     #     print(f"Iteration {i}")

#     #     my_array = [1, 2, 3, 4, 5]
#     #     print("Array:", my_array)
#     #     j = 0
#     #     while j < len(my_array):
#     #         print(f"While iteration {j}, value: {my_array[j]}")
#     #         j += 1
#             # Abrir el archivo CSV y leer sus datos

# def read_csv():
#     with open("data.csv",  'w', newline='') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)


# if __name__ == "__main__":
#     main()

import pandas as pd
import os

def leer_excel(archivo):
    """
    Lee un archivo Excel usando pandas y retorna un DataFrame
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(archivo):
            print(f"El archivo '{archivo}' no existe")
            return None
            
        # Verificar si el archivo está vacío
        if os.path.getsize(archivo) == 0:
            print(f"El archivo '{archivo}' está vacío")
            return None
            
        # Leer el archivo Excel
        df = pd.read_excel(archivo)
        
        # Verificar si hay datos
        if df.empty:
            print("El archivo no contiene datos")
            return None
            
        return df
        
    except Exception as e:
        print(f"Error al leer el archivo Excel: {str(e)}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo Excel: ")
    if not nombre_archivo.endswith('.xlsx'):
        nombre_archivo += '.xlsx'

    
    print(f"Intentando leer el archivo: {nombre_archivo}")
    print(f"Ruta absoluta: {os.path.abspath(nombre_archivo)}")
    
    # Leer el archivo Excel
    print("\nLeyendo archivo Excel:")
    df = leer_excel(nombre_archivo)
    if df is not None:
        print("\nPrimeras 5 filas del archivo:")
        print(df.head())
        print("\nTodas las filas del archivo:")
        print(df)
        primera_columna = df.iloc[:, 0].to_numpy()
        print("\nValores de la primera columna en un array:")
        print(primera_columna)
        # for i in range(len(df)):
        #     print(df.iloc[i])
        
        print("\nInformación del DataFrame:")
        print(df.info())
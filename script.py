import os
import sys

def contar_lin_y_palab(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            num_lineas = len(lineas)
            num_palabras = sum(len(linea.split()) for linea in lineas)
            num_python = sum(linea.lower().count('python') for linea in lineas)
            return num_lineas, num_palabras, num_python
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error al procesar el archivo {archivo}: {e}")
        return None

def g_informe(directorio):
    archivos_txt = [f for f in os.listdir(directorio) if f.endswith('.txt')]
    if not archivos_txt:
        return "No se encontraron archivos de texto"

    informe_lineas = []
    for archivo in archivos_txt:
        ruta_archivo = os.path.join(directorio, archivo)
        resultados = contar_lin_y_palab(ruta_archivo)

        if resultados is not None:
            num_lineas, num_palabras, num_python = resultados
            informe_lineas.append(f"Nombre del archivo: {archivo}\n"
                                 f"Número de líneas: {num_lineas}\n"
                                 f"Número total de palabras: {num_palabras}\n"
                                 f"Número de veces que aparece 'Python': {num_python}\n"
                                 "-----------------------------------\n")
    
    return ''.join(informe_lineas)

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]

    if not os.path.isdir(directorio):
        print("Error: El directorio no existe.")
        sys.exit(1)

    informe = g_informe(directorio)

    with open(os.path.join(directorio, 'informe.txt'), 'w', encoding='utf-8') as f:
        f.write(informe)

    print("Informe generado exitosamente en 'informe.txt'.")

if __name__ == "__main__":
    main()

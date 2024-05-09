import os

# Función para realizar XOR bit a bit entre dos cadenas binarias
def xor_binario(binario1, binario2):
    resultado = ""
    for bit1, bit2 in zip(binario1, binario2):
        if bit1 == bit2:
            resultado += "0"
        else:
            resultado += "1"
    return resultado

# Función para encriptar un archivo
def encriptar_archivo(nombre_archivo):
    try:
        # Leer el contenido del archivo
        with open(nombre_archivo, 'rb') as archivo:
            contenido = archivo.read()

        # Convertir contenido a binario
        contenido_binario = bin(int.from_bytes(contenido, 'big'))[2:]

        # Obtener la longitud del contenido en binario
        longitud_contenido = len(contenido_binario)

        # Generar clave aleatoria del mismo tamaño que el contenido binario
        clave_aleatoria = os.urandom(longitud_contenido // 8)

        # Convertir clave a binario
        clave_binario = bin(int.from_bytes(clave_aleatoria, 'big'))[2:].zfill(longitud_contenido)

        # Realizar XOR entre el contenido binario y la clave binaria
        contenido_encriptado = xor_binario(contenido_binario, clave_binario)

        # Escribir el contenido encriptado en un nuevo archivo
        with open(nombre_archivo + ".encrypted", 'w') as archivo_encriptado:
            archivo_encriptado.write(contenido_encriptado)
        
        # Guardar la clave de encriptación en un archivo
        with open(nombre_archivo + ".key", 'wb') as archivo_clave:
            archivo_clave.write(clave_aleatoria)
        
        print("¡Archivo encriptado exitosamente!")

    except Exception as e:
        print("Error al encriptar el archivo:", e)

# Función para desencriptar un archivo
def desencriptar_archivo(nombre_archivo):
    try:
        # Leer el contenido del archivo encriptado
        with open(nombre_archivo, 'r') as archivo_encriptado:
            contenido_encriptado = archivo_encriptado.read()

        # Solicitar al usuario la ruta del archivo .key
        ruta_clave = input("Ingrese la ruta del archivo .key (incluyendo la extensión): ")

        # Leer la clave de encriptación desde el archivo .key
        with open(ruta_clave, 'rb') as archivo_clave:
            clave_aleatoria = archivo_clave.read()

        # Obtener la longitud del contenido encriptado
        longitud_contenido = len(contenido_encriptado)

        # Convertir clave a binario
        clave_binario = bin(int.from_bytes(clave_aleatoria, 'big'))[2:].zfill(longitud_contenido)

        # Realizar XOR entre el contenido encriptado y la clave binaria
        contenido_desencriptado = xor_binario(contenido_encriptado, clave_binario)

        # Convertir contenido desencriptado de binario a bytes
        contenido_bytes = int(contenido_desencriptado, 2).to_bytes((len(contenido_desencriptado) + 7) // 8, byteorder='big')

        # Escribir el contenido desencriptado en un nuevo archivo
        with open(nombre_archivo.replace(".encrypted", "") + ".decrypted", 'wb') as archivo_desencriptado:
            archivo_desencriptado.write(contenido_bytes)

        print("¡Archivo desencriptado exitosamente!")

    except Exception as e:
        print("Error al desencriptar el archivo:", e)

# Función para mostrar el menú y realizar la acción seleccionada
def menu():
    while True:
        print("\nMenú:")
        print("1. Encriptar archivo")
        print("2. Desencriptar archivo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_archivo = input("Ingrese la ruta del archivo a encriptar (incluyendo la extensión): ")
            encriptar_archivo(nombre_archivo)
        elif opcion == "2":
            nombre_archivo = input("Ingrese la ruta del archivo encriptado (incluyendo la extensión): ")
            desencriptar_archivo(nombre_archivo)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor seleccione una opción válida.")


# Ejecutar el menú
menu()

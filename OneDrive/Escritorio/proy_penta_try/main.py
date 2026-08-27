#!/usr/bin/env -S uv run --env-file .env
import datetime
import sys
import os
import requests
import json
import csv

API_BASE_URL = os.getenv("URL_BASE")   # Reemplaza con tu URL real
TOKEN = os.getenv("TOKEN")   # Reemplaza con tu URL real

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + TOKEN
}


def consultar_usuario():
    
    user_id = input("Ingrese el username del usuario a consultar:")
    url = API_BASE_URL + f"/getUserXByUsername?resellerID=2&username={user_id}"

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def cargar_nuevo_usuario(username=None,password=None):
    if username is None or password is None:
        username = input("Ingrese el username del usuario a crear:")
        password = input("Ingrese el pass del usuario a crear:")
    
    url= API_BASE_URL + "/createUserX"
    
    payload = json.dumps({
        "member_id": 2,
        "username": username,
        "password": password,
        "bouquet": "[1]"
    })

    try:
        response = requests.request("POST", url, headers=headers, data=payload)

        data = response.json()

        if response.status_code == 200 or response.status_code == 201:
            print(f"✅ Usuario '{username}' creado correctamente con ID: {data}")
            return("OK")
        else:
            print(f"❌ Error al crear usuario '{username}'")
            return("ERROR")
    except Exception as e:
        print(f"⚠️ Error al crear usuario '{username}': {str(e)}")
        return("ERROR")


def actualizar_usuario():
    def getIdByCedula(cedula):
        #busca en el csv usuarios.csv el registro donde el campo usuario contenga la cedula
        with open('usuarios.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if cedula in row['username']:
                    return row['id']
        return None
        pass


    user_id = input("Ingrese la cedula del usuario a actualizar: ")
    new_password = input("Ingrese la nueva contraseña: ")

    url= API_BASE_URL + "/updateUserX"

    j=getIdByCedula(user_id)
    if j is not None:
        user_id = j
    else:
        print(f"❌ Usuario con cedula '{user_id}' no encontrado.")
        return ("ERROR"
                )

    payload = json.dumps({
    "id": int(user_id),
    "password": new_password,
    "bouquet": "[1]"
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()

    if (response.status_code == 200 or response.status_code == 201):
        print(f"\n✅ Cambio realizado en  '{user_id}'")
    else:
        print(f"❌ Error al actualizar usuario '{user_id}': {data.get('error', 'Error desconocido')}")
        return

def eliminar_usuario():
    def getIdByCedula(cedula):
        #busca en el csv usuarios.csv el registro donde el campo usuario contenga la cedula
        with open('usuarios.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if cedula in row['username']:
                    return row['id']
        return None
        pass

    user_id = input("Ingrese la cedula del usuario a actualizar: ")

    url= API_BASE_URL + "/deleteUserX"

    j=getIdByCedula(user_id)
    if j is not None:
        user_id = j
    else:
        print(f"❌ Usuario con cedula '{user_id}' no encontrado.")
        return ("ERROR"
                )

    payload = json.dumps({
    "id": int(user_id),
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()

    if (response.status_code == 200 or response.status_code == 201):
        print(f"\n✅ Usuario eliminado en  '{user_id}'")
    else:
        print(f"❌ Error al eliminar usuario '{user_id}': {data.get('error', 'Error desconocido')}")
        return


def toggle_conexion_usuario():
    user_id = input("Ingrese el ID del usuario: ")
    estado = input("¿Desea conectar o desconectar? (conectar/desconectar): ").lower()
    data = {"accion": estado}
    response = requests.post(f"{API_BASE_URL}/{user_id}/conexion", json=data)
    print_response(response)


def print_response(response):
    try:
        response.raise_for_status()
        print("✅ Respuesta:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except requests.exceptions.HTTPError as err:
        print(f"❌ Error: {err}")
        if response.content:
            print(response.text)

def menu():
    opciones = {
        "1": consultar_usuario,
        "2": cargar_nuevo_usuario,
        "3": actualizar_usuario,
        "4": eliminar_usuario,
        "5": toggle_conexion_usuario,

    }

    while True:
        print("\n📋 Menú de opciones:")
        print("1. Consultar usuario por cedula")
        print("2. Cargar nuevo usuario")
        print("3. Actualizar usuario (solo contraseña)")
        print("4. Eliminar usuario")
        print("5. Conectar/Desconectar usuario")


        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("👋 Saliendo del programa.")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("⚠️ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()







# def main():
#     print(sys.executable)


# if __name__ == "__main__":
#     main()





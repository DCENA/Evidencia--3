

from gestion_parcelas import menu_gestion_parcelas
from gestion_sensores import menu_gestion_sensores
from registro_mediciones import registrar_medicion
from consulta_datos import consultar_datos

def main():
    print("SISTEMA DE MONITOREO AGROTECH COOP")

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Gestión de Parcelas")
        print("2. Gestión de Sensores")
        print("3. Registro de Mediciones")
        print("4. Consulta de Datos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_gestion_parcelas()
        elif opcion == "2":
            menu_gestion_sensores()
        elif opcion == "3":
            registrar_medicion()
        elif opcion == "4":
            consultar_datos()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
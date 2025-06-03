
# Este diccionario estará disponible para otros módulos
parcelas = {}

def menu_gestion_parcelas():
    while True:
        print("\nGESTIÓN DE PARCELAS")
        print("1. Agregar Parcela")
        print("2. Modificar Parcela")
        print("3. Eliminar Parcela")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_parcela()
        elif opcion == "2":
            modificar_parcela()
        elif opcion == "3":
            eliminar_parcela()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def agregar_parcela():
    id_parcela = input("Ingrese ID de la parcela: ")
    if id_parcela in parcelas:
        print("Ya existe una parcela con ese ID.")
        return
    localidad = input("Ingrese localidad: ")
    try:
        superficie = float(input("Ingrese superficie (ha): "))
    except ValueError:
        print("Superficie inválida.")
        return
    cultivo = input("Ingrese cultivo: ")
    sensor = input("¿Activar sensor? (SI/NO): ").strip().upper()
    sensor_activo = "SI" if sensor == "SI" else "NO"

    parcelas[id_parcela] = {
        "localidad": localidad,
        "superficie": superficie,
        "cultivo": cultivo,
        "sensor_activo": sensor_activo
    }
    print("✅ Parcela agregada correctamente.")

def modificar_parcela():
    id_parcela = input("Ingrese ID de la parcela a modificar: ")
    if id_parcela not in parcelas:
        print("No existe una parcela con ese ID.")
        return
    localidad = input("Nueva localidad: ")
    try:
        superficie = float(input("Nueva superficie (ha): "))
    except ValueError:
        print("Superficie inválida.")
        return
    cultivo = input("Nuevo cultivo: ")
    sensor = input("¿Activar sensor? (SI/NO): ").strip().upper()
    sensor_activo = "SI" if sensor == "SI" else "NO"

    parcelas[id_parcela] = {
        "localidad": localidad,
        "superficie": superficie,
        "cultivo": cultivo,
        "sensor_activo": sensor_activo
    }
    print("✅ Parcela modificada correctamente.")

def eliminar_parcela():
    id_parcela = input("Ingrese ID de la parcela a eliminar: ")
    if id_parcela in parcelas:
        del parcelas[id_parcela]
        print("🗑️ Parcela eliminada.")
    else:
        print("❌ Parcela no encontrada.")

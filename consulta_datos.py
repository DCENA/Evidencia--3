
import gestion_parcelas  # IMPORTAMOS EL MÓDULO COMPLETO

def consultar_datos():
    print("\n--- Consulta de Datos ---")
    if not gestion_parcelas.parcelas:
        print("No hay parcelas registradas.")
        return

    print("📋 Parcelas registradas:")
    for id_parcela, info in gestion_parcelas.parcelas.items():
        print(f"\n🆔 ID: {id_parcela}")
        print(f"   Localidad: {info['localidad']}")
        print(f"   Superficie: {info['superficie']} ha")
        print(f"   Cultivo: {info['cultivo']}")
        print(f"   Sensor activo: {info['sensor_activo']}")
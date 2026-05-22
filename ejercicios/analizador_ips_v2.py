import os
from collections import Counter

def analizar_ips():
    # Ruta del archivo ips.txt en el mismo directorio del script
    ruta_archivo = os.path.join(os.path.dirname(__file__), "ips.txt")
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return

    # Definir los prefijos de IPs privadas usando comprensión de listas
    # Clase A: 10.0.0.0/8
    # Clase B: 172.16.0.0/12
    # Clase C: 192.168.0.0/16
    prefijos_privados = ["10.", "192.168."] + [f"172.{i}." for i in range(16, 32)]
    
    todas_las_ips = []
    ips_privadas = set()
    ips_publicas = set()
    
    # Detalle de conexiones agrupadas por categoría
    detalle_conexiones = {
        "192.168.1.x": 0,
        "10.0.0.x": 0,
        "172.16.x.x": 0,
        "Públicas": 0
    }
    
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            
            # Extraer la IP (parte izquierda antes del guion ' - ')
            partes = linea.split(" - ")
            ip = partes[0].strip()
            todas_las_ips.append(ip)
            
            # Determinar si es privada o pública usando any()
            es_privada = any(ip.startswith(prefijo) for prefijo in prefijos_privados)
            
            if es_privada:
                ips_privadas.add(ip)
                # Clasificar en el detalle
                if ip.startswith("192.168.1."):
                    detalle_conexiones["192.168.1.x"] += 1
                elif ip.startswith("10.0.0."):
                    detalle_conexiones["10.0.0.x"] += 1
                elif ip.startswith("172.16."):
                    detalle_conexiones["172.16.x.x"] += 1
            else:
                ips_publicas.add(ip)
                detalle_conexiones["Públicas"] += 1
                
    # Calcular la IP más frecuente usando Counter del módulo collections
    contador_ips = Counter(todas_las_ips)
    ip_mas_frecuente, veces = contador_ips.most_common(1)[0]
    
    # Imprimir los resultados principales
    print(f"IPs privadas encontradas: {len(ips_privadas)}")
    print(f"IPs públicas encontradas: {len(ips_publicas)}")
    
    palabra_veces = "vez" if veces == 1 else "veces"
    print(f"IP más frecuente: {ip_mas_frecuente} ({veces} {palabra_veces})")
    
    print("\nDetalle:")
    for categoria, conexiones in detalle_conexiones.items():
        palabra_conexion = "conexión" if conexiones == 1 else "conexiones"
        print(f"- {categoria}: {conexiones} {palabra_conexion}")

if __name__ == "__main__":
    analizar_ips()

def analizar_contraseña(contraseña):
    """
    Analiza la fortaleza de una contraseña.
    Devuelve: (puntuacion, mensaje, detalles)
    """
    if not contraseña:
        return 0, "❌ La contraseña no puede estar vacía", []
    
    # Comprobaciones con any()
    checks = {
        "Número": any(c.isdigit() for c in contraseña),
        "Mayúscula": any(c.isupper() for c in contraseña),
        "Minúscula": any(c.islower() for c in contraseña),
        "Carácter especial": any(not c.isalnum() for c in contraseña),
        "Longitud > 8": len(contraseña) > 8
    }
    
    # Contar cuántas reglas cumple
    puntuacion = sum(checks.values())
    
    # Detalles de lo que falta
    faltan = [regla for regla, cumple in checks.items() if not cumple]
    
    # Determinar fortaleza
    if puntuacion == 5:
        mensaje = "🔒 Tu contraseña es FUERTE"
    elif puntuacion >= 3:
        mensaje = "🟡 Tu contraseña es MEDIA"
    else:
        mensaje = "🔴 Tu contraseña es DÉBIL"
    
    return puntuacion, mensaje, faltan


# --- Programa principal ---
if __name__ == "__main__":
    contraseña = input("Introduce tu contraseña: ").strip()
    
    puntuacion, mensaje, faltan = analizar_contraseña(contraseña)
    
    print(f"\n{mensaje}")
    print(f"Puntuación: {puntuacion}/5")
    
    if faltan:
        print(f"\nTe falta: {', '.join(faltan)}")

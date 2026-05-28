from datetime import datetime
import json
import os
from typing import List, Optional
from collections import Counter


class Nota:
    def __init__(self, contenido: str, categoria: str = "general"):
        self.contenido = contenido
        self.categoria = categoria
        self.fecha = datetime.now().isoformat()
        self.id = hash(self.fecha + contenido)
    
    def __str__(self):
        fecha_corta = self.fecha[:10]
        return f"[{fecha_corta}] ({self.categoria}) {self.contenido[:50]}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "contenido": self.contenido,
            "categoria": self.categoria,
            "fecha": self.fecha
        }


class GestorNotas:
    ARCHIVO = "notas.json"
    
    def __init__(self):
        self.notas: List[Nota] = []
        self._cargar()
    
    def _cargar(self):
        if not os.path.exists(self.ARCHIVO):
            return
        with open(self.ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
            for item in datos:
                nota = Nota(item["contenido"], item["categoria"])
                nota.fecha = item["fecha"]
                self.notas.append(nota)
    
    def _guardar(self):
        with open(self.ARCHIVO, "w", encoding="utf-8") as f:
            json.dump([n.to_dict() for n in self.notas], f, indent=2, ensure_ascii=False)
    
    def agregar(self, contenido: str, categoria: str = "general") -> Nota:
        nota = Nota(contenido, categoria)
        self.notas.append(nota)
        self._guardar()
        return nota
    
    def listar(self, categoria: Optional[str] = None) -> List[Nota]:
        if categoria:
            return [n for n in self.notas if n.categoria == categoria]
        return self.notas
    
    def buscar(self, texto: str) -> List[Nota]:
        return [n for n in self.notas if texto.lower() in n.contenido.lower()]
    
    def eliminar(self, id_nota: int) -> bool:
        for i, nota in enumerate(self.notas):
            if nota.id == id_nota:
                self.notas.pop(i)
                self._guardar()
                return True
        return False
    
    def estadisticas(self) -> dict:
        categorias = Counter(n.categoria for n in self.notas)
        return {
            "total": len(self.notas),
            "categorias": dict(categorias),
            "ultima_nota": self.notas[-1].fecha if self.notas else None
        }


def mostrar_menu():
    print("\n" + "="*40)
    print("  📒 GESTOR DE NOTAS v2.0")
    print("="*40)
    print("1. Ver todas las notas")
    print("2. Ver por categoría")
    print("3. Buscar nota")
    print("4. Agregar nota")
    print("5. Eliminar nota")
    print("6. Estadísticas")
    print("7. Salir")
    print("="*40)


def main():
    gestor = GestorNotas()
    
    while True:
        mostrar_menu()
        opcion = input("Elige: ").strip()
        
        if opcion == "1":
            notas = gestor.listar()
            if not notas:
                print("📭 No hay notas.")
            for n in notas:
                print(f"  {n}")
                
        elif opcion == "2":
            cat = input("Categoría: ").strip()
            notas = gestor.listar(cat)
            for n in notas:
                print(f"  {n}")
                
        elif opcion == "3":
            texto = input("Buscar: ").strip()
            resultados = gestor.buscar(texto)
            print(f"🔍 {len(resultados)} encontradas:")
            for n in resultados:
                print(f"  {n}")
                
        elif opcion == "4":
            contenido = input("Contenido: ").strip()
            categoria = input("Categoría [general]: ").strip() or "general"
            nota = gestor.agregar(contenido, categoria)
            print(f"✅ Guardada: {nota}")
            
        elif opcion == "5":
            try:
                id_nota = int(input("ID a eliminar: "))
                if gestor.eliminar(id_nota):
                    print("🗑️ Eliminada.")
                else:
                    print("❌ ID no encontrado.")
            except ValueError:
                print("❌ ID debe ser número.")
                
        elif opcion == "6":
            stats = gestor.estadisticas()
            print(f"\n📊 Total: {stats['total']}")
            print(f"📁 Categorías: {stats['categorias']}")
            print(f"🕐 Última: {stats['ultima_nota']}")
            
        elif opcion == "7":
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    main()
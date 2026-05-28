from datetime import datetime
import json
import os
from typing import List, Optional
from collections import Counter  # Para estadisticas

# clase tarea 

estado = [ "pendiente", "en progreso", "completada" ]

class Tarea:
    def __init__(self, id_tarea: int, texto: str, categoria: str = "General", estado: str = "pendiente"):
        self.id = id_tarea
        self.texto = texto
        self.categoria = categoria
        self.estado = estado
        self.fecha = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
            "categoria": self.categoria,
            "estado": self.estado,
            "fecha": self.fecha
        }

    def __str__(self):
        return f"ID {self.id} | [{self.fecha[:19]}] ({self.estado}) {self.categoria} - {self.texto}"

#clase gestor
class GestorTareas:
    ARCHIVO = "tareas.json"

    def __init__(self):
        self.tareas: List[Tarea] = []
        self._cargar()

    def _cargar(self):
        if not os.path.exists(self.ARCHIVO):
            return
        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                if not contenido:
                    return
                datos = json.loads(contenido)
                for i, item in enumerate(datos):
                    id_tarea = item.get("id", i + 1)
                    tarea = Tarea(id_tarea, item["texto"], item.get("categoria", "General"), item.get("estado", "pendiente"))
                    tarea.fecha = item.get("fecha", datetime.now().isoformat())
                    self.tareas.append(tarea)
        except Exception as e:
            print(f"Error al cargar las tareas: {e}")

    def _guardar(self):
        with open(self.ARCHIVO, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tareas], f, indent=2, ensure_ascii=False)

    def agregar(self, texto: str, categoria: str = "General") -> Tarea:
        nuevo_id = max([t.id for t in self.tareas], default=0) + 1
        tarea = Tarea(nuevo_id, texto, categoria)
        self.tareas.append(tarea)
        self._guardar()
        return tarea

    def listar(self, categoria: Optional[str] = None) -> List[Tarea]:
        if categoria:
            return [t for t in self.tareas if t.categoria == categoria]
        return self.tareas

    def buscar(self, texto:str) -> List[Tarea]:
        return [t for t in self.tareas if texto.lower() in t.texto.lower()]
    
    def eliminar(self, id_tarea:int) -> bool:
        for i, tarea in enumerate(self.tareas):
            if tarea.id == id_tarea:
                self.tareas.pop(i)
                self._guardar()
                return True
        return False

    def actualizar(self, id_tarea:int, texto:Optional[str] = None, categoria:Optional[str] = None, estado:Optional[str] = None) -> bool:
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                if texto is not None:
                    tarea.texto = texto
                if categoria is not None:
                    tarea.categoria = categoria
                if estado is not None:
                    tarea.estado = estado
                self._guardar()
                return True
        return False
    
    def estadisticas(self) -> dict:
        categorias = Counter(t.categoria for t in self.tareas)
        return {
            "total": len(self.tareas),
            "categorias": dict(categorias),
            "ultima_tarea": self.tareas[-1].fecha if self.tareas else None
        }

#interfaz de texto

def mostrar_menu():
    print("\n" + "=" * 40)
    print("  GESTOR DE TAREAS v2.0")
    print("=" * 40)
    print("1. Ver todas las tareas")
    print("2. Ver por categoria")
    print("3. Buscar tarea")
    print("4. Agregar tarea")
    print("5. Eliminar tarea")
    print("6. Actualizar tarea")
    print("7. Estadisticas")
    print("8. Salir")
    print("=" * 40)


def main():
    gestor = GestorTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Elige: ").strip()
        
        if opcion == "1":
            tareas = gestor.listar()
            if not tareas:
                print("No hay tareas pendientes.")
            for t in tareas:
                print(f"  {t}")
        elif opcion == "2":
            cat = input("Categoria: ").strip()
            tareas = gestor.listar(cat)
            for t in tareas:
                print(f"  {t}")
        elif opcion == "3":
            texto = input("Buscar: ").strip()
            resultados = gestor.buscar(texto)
            print(f"{len(resultados)} encontradas:")
            for t in resultados:
                print(f"  {t}")
        elif opcion == "4":
            contenido = input("Contenido: ").strip()
            categoria = input("Categoria [General]: ").strip() or "General"
            tarea = gestor.agregar(contenido, categoria)
            print(f"Guardada: {tarea}")
        elif opcion == "5":
            try:
                id_tarea = int(input("ID a eliminar: "))
                if gestor.eliminar(id_tarea):
                    print("Eliminada.")
                else:
                    print("ID no encontrado.")
            except ValueError:
                print("ID debe ser numero.")
        elif opcion == "6":
            try:
                id_tarea = int(input("ID a actualizar: "))
                texto = input("Nuevo contenido [dejar vacio para no cambiar]: ").strip() or None
                categoria = input("Nueva categoria [dejar vacio para no cambiar]: ").strip() or None
                estado = input("Nuevo estado [pendiente/progreso/completada][dejar vacio para no cambiar]: ").strip() or None
                if gestor.actualizar(id_tarea, texto, categoria, estado):
                    print("Actualizada.")
                else:
                    print("ID no encontrado.")
            except ValueError:
                print("ID debe ser numero.")
        elif opcion == "7":
            stats = gestor.estadisticas()
            print(f"\nTotal: {stats['total']}")
            print(f"Categorias: {stats['categorias']}")
            print(f"Ultima: {stats['ultima_tarea']}")
        elif opcion == "8":
            print("Hasta luego, que tenga un buen dia caballero.")
            break
        else:
            print("Opcion no valida.")
if __name__ == "__main__":
    main()



    

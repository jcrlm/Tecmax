#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime

PREGUNTAS_FILE = "preguntas.json"
REPORTES_DIR = "reportes"

# ---------- UTILIDADES ----------

def limpiar_pantalla():
    os.system("clear")

def pausar():
    input("\nPresiona ENTER para continuar...")

# ---------- PREGUNTAS ----------

def cargar_preguntas():
    if not os.path.exists(PREGUNTAS_FILE):
        preguntas_default = {
            "cliente": [
                "Nombre del cliente",
                "Teléfono",
                "Dirección"
            ],
            "equipo": [
                "Marca",
                "Modelo",
                "Número de serie"
            ],
            "servicio": [
                "¿Desea cotización? (si/no)",
                "Falla reportada",
                "Observaciones"
            ]
        }
        with open(PREGUNTAS_FILE, "w", encoding="utf-8") as f:
            json.dump(preguntas_default, f, indent=4, ensure_ascii=False)

    with open(PREGUNTAS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def editar_preguntas():
    os.system(f"nano {PREGUNTAS_FILE}")

# ---------- REPORTES ----------

def crear_reporte():
    limpiar_pantalla()
    preguntas = cargar_preguntas()
    respuestas = {}

    print("📝 CREAR REPORTE DE SERVICIO TÉCNICO")

    for seccion, lista in preguntas.items():
        print(f"\n--- {seccion.upper()} ---")
        respuestas[seccion] = {}
        for pregunta in lista:
            respuesta = input(f"{pregunta}: ")
            respuestas[seccion][pregunta] = respuesta

    guardar_reporte(respuestas)
    pausar()

def guardar_reporte(respuestas):
    if not os.path.exists(REPORTES_DIR):
        os.makedirs(REPORTES_DIR)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_archivo = datetime.now().strftime("reporte_%Y%m%d_%H%M%S.txt")
    ruta = os.path.join(REPORTES_DIR, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("REPORTE DE SERVICIO TÉCNICO\n")
        f.write("=" * 35 + "\n")
        f.write(f"Fecha: {fecha}\n")

        for seccion, datos in respuestas.items():
            f.write(f"\n[{seccion.upper()}]\n")
            for pregunta, respuesta in datos.items():
                f.write(f"{pregunta}: {respuesta}\n")

    print(f"\n✅ Reporte guardado en: {ruta}")

# ---------- MENÚ ----------

def menu():
    limpiar_pantalla()
    print("================================")
    print("      TECMAX - SERVICIO TÉCNICO ")
    print("================================")
    print("1. Crear reporte")
    print("2. Editar preguntas del reporte")
    print("3. Salir")
    print("================================")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_reporte()
        elif opcion == "2":
            editar_preguntas()
        elif opcion == "3":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("\n❌ Opción inválida")
            pausar()

# ---------- EJECUCIÓN ----------

if __name__ == "__main__":
    main()

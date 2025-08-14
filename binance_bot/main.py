# main.py

import os
import time

# Importar funciones de ambos backtests
try:
    from modules.backtest_semanal import ejecutar_backtest as backtest_v2
    from modules.backtest_semanal_v1 import ejecutar_backtest as backtest_v1
except ImportError as e:
    print(f"❌ Error al importar los módulos: {e}")
    exit(1)

def ejecutar_ambos_backtests():
    print("📊 Iniciando comparación de versiones...\n")

    print("▶ Ejecutando versión actual (V2: con ATR/ADX)...")
    start_v2 = time.time()
    backtest_v2()
    print(f"⏱️ V2 completado en {round(time.time() - start_v2, 2)} segundos.\n")

    print("▶ Ejecutando versión anterior (V1: sin ATR/ADX)...")
    start_v1 = time.time()
    backtest_v1()
    print(f"⏱️ V1 completado en {round(time.time() - start_v1, 2)} segundos.\n")

    # Verificación de archivos
    archivos = ["resultados_semanales.csv", "resultados_semanales_v1.csv"]
    for archivo in archivos:
        if os.path.exists(archivo):
            print(f"✅ Archivo generado: {archivo}")
        else:
            print(f"⚠️ Archivo no encontrado: {archivo}")

    print("\n📈 Listo para comparar resultados.")

if __name__ == '__main__':
    ejecutar_ambos_backtests()
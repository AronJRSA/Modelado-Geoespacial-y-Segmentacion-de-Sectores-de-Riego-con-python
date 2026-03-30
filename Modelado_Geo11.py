# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:14:53 2026

@author: asron
"""
from modules import ingestion, geo, modeling, visualization
from reports import export
from config.settings import PATHS


def main():
    # 1. Datos
    df = ingestion.load_kml_to_dataframe(PATHS["kml"])
    
    # 2. Zonas (MOVER AQUÍ ARRIBA)
    df, _ = modeling.generar_zonas_riego(df)
    ingestion.save_dataframe(df, PATHS["csv"])
    c_y, c_x = ingestion.get_center_coordinates(df)

# 3. Mapa
    visualization.crear_mapa(df, c_y, c_x, PATHS["map_html"])
    visualization.capturar_mapa(PATHS["map_html"], PATHS["map_png"])

    # 4. Geoespacial (Usa los nombres de settings.py)
    geo.generar_modelo_3d(df, PATHS["3d"])
    geo.generar_curvas_nivel(df, PATHS["curvas"])
    geo.generar_curvas_zonas(df, PATHS["curvas_zona"]) 

    # 5. Reporte
    export.generar_reporte(
    output_path=PATHS["reporte"], # Cambia PATHS= por output_path=
    imagen_mapa=PATHS["map_png"],
    imagen_3d=PATHS["3d"],
    imagen_curvas=PATHS["curvas"],
    imagen_zonas=PATHS["curvas_zona"]
    )


if __name__ == "__main__":
    main()
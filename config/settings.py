import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

PATHS = {
    "kml": os.path.join(BASE_PATH, "data", "input", "Huerta.kml"),
    "csv": os.path.join(BASE_PATH, "data", "output", "datos.csv"),
    "3d": os.path.join(BASE_PATH, "data", "output", "3d.png"),
    "curvas": os.path.join(BASE_PATH, "data", "output", "curvas.png"),
    "curvas_zona": os.path.join(BASE_PATH, "data", "output", "curvas_zona.png"),
    "map_html": os.path.join(BASE_PATH, "data", "output", "mapa.html"),
    "map_png": os.path.join(BASE_PATH, "data", "output", "mapa.png"),
    "reporte": os.path.join(BASE_PATH, "data", "output", "reporte.docx"),
}
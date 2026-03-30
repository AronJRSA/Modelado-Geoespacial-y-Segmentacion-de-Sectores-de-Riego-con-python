# Archivo: ingestion.py
import xml.etree.ElementTree as ET
import pandas as pd


def load_kml_to_dataframe(kml_path: str) -> pd.DataFrame:

    tree = ET.parse(kml_path)
    root = tree.getroot()

    ns = {'kml': 'http://www.opengis.net/kml/2.2'}
    data = []

    for pm in root.findall('.//kml:Placemark', ns):

        nombre = pm.find('kml:name', ns)
        nombre = nombre.text if nombre is not None else "Sin_ID"

        coords = pm.find('.//kml:coordinates', ns)

        if coords is not None:
            c_list = coords.text.strip().split(',')

            data.append({
                'ID_Arbol': nombre,
                'Longitud_X': float(c_list[0]),
                'Latitud_Y': float(c_list[1]),
                'Elevacion_Z': float(c_list[2])
            })

    return pd.DataFrame(data)


def save_dataframe(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, index=False, encoding='utf-8')


def get_center_coordinates(df: pd.DataFrame):
    centro_x = df['Longitud_X'].mean()
    centro_y = df['Latitud_Y'].mean()
    return centro_y, centro_x
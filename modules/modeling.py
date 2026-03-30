# Archivo: modeling.py
from sklearn.cluster import KMeans
import pandas as pd


def generar_zonas_riego(df: pd.DataFrame, k: int = 4):

    X = df[['Longitud_X', 'Latitud_Y', 'Elevacion_Z']]

    kmeans = KMeans(n_clusters=k, random_state=42)

    df['Zona'] = kmeans.fit_predict(X)

    centros = kmeans.cluster_centers_

    return df, centros
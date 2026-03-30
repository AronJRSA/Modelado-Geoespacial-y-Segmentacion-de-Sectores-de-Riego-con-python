# Archivo: geo.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def generar_modelo_3d(df, output_path):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(
        df['Longitud_X'], df['Latitud_Y'], df['Elevacion_Z'],
        c=df['Elevacion_Z'], cmap='terrain', s=60, edgecolors='k', alpha=0.8
    )

    ax.set_title('Modelo 3D de la Huerta', fontsize=15)
    ax.set_xlabel('Longitud (X)')
    ax.set_ylabel('Latitud (Y)')
    ax.set_zlabel('Elevación (msnm)')
    fig.colorbar(sc, ax=ax, label='Altura (msnm)', shrink=0.5, aspect=5)
    ax.view_init(elev=30, azim=45)

    plt.savefig(output_path, dpi=300)
    plt.close()

def generar_curvas_nivel(df, output_path):
    x, y, z = df['Longitud_X'].values, df['Latitud_Y'].values, df['Elevacion_Z'].values
    xi = np.linspace(x.min(), x.max(), 100)
    yi = np.linspace(y.min(), y.max(), 100)
    xi, yi = np.meshgrid(xi, yi)
    zi = griddata((x, y), z, (xi, yi), method='cubic')

    plt.figure(figsize=(10, 8))
    contour = plt.contour(xi, yi, zi, levels=15)
    plt.clabel(contour, inline=True, fontsize=8)
    plt.scatter(x, y, c='red', s=10)

    plt.title('Curvas de nivel - Huerta')
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')

    plt.savefig(output_path, dpi=300)
    plt.close()

def generar_curvas_zonas(df, output_path):
    # Reutilizamos la lógica de interpolación
    x, y, z = df['Longitud_X'].values, df['Latitud_Y'].values, df['Elevacion_Z'].values
    xi = np.linspace(x.min(), x.max(), 100)
    yi = np.linspace(y.min(), y.max(), 100)
    xi, yi = np.meshgrid(xi, yi)
    zi = griddata((x, y), z, (xi, yi), method='cubic')

    plt.figure(figsize=(10, 8))
    plt.contourf(xi, yi, zi, levels=15, cmap='terrain')
    plt.contour(xi, yi, zi, levels=15, colors='black', linewidths=0.5)

    if 'Zona' in df.columns:
        plt.scatter(df['Longitud_X'], df['Latitud_Y'], c=df['Zona'], cmap='tab10', s=40, edgecolors='white')

    plt.title('Curvas + Zonas de Riego')
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.colorbar(label='Elevación')

    plt.savefig(output_path, dpi=300)
    plt.close()
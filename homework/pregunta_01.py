"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output/solicitudes_de_credito.csv"

    if not os.path.exists("files/output"):
        os.makedirs("files/output")


    df = pd.read_csv(input_file, sep=";", index_col=0)

    df["sexo"] = df["sexo"].str.strip().str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip().str.lower()
    df["idea_negocio"] = (
        df["idea_negocio"]
        .str.strip().str.lower()
        .str.replace("á", "a").str.replace("é", "e").str.replace("í", "i")
        .str.replace("ó", "o").str.replace("ú", "u")
        .str.replace(" ", "")
        .str.translate(str.maketrans("", "", "-._"))
    )
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")
    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.strip().str.strip("$")
        .str.replace(".00", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(int)
    )

    df["línea_credito"] = (
        df["línea_credito"]
        .str.strip()
        .str.lower()
        .str.replace(" ", "")
        .str.translate(str.maketrans("", "", "-._"))
    )

    df = df.dropna().drop_duplicates()
    df.to_csv(output_file, index=False, sep=";")



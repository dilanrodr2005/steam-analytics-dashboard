import pyodbc
import pandas as pd
import streamlit as st

def get_connection():
    # Carga las credenciales desde los Secrets de Streamlit
    server = st.secrets["db_credentials"]["server"]
    database = st.secrets["db_credentials"]["database"]
    username = st.secrets["db_credentials"]["username"]
    password = st.secrets["db_credentials"]["password"]
    
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )
    return pyodbc.connect(connection_string)

# El resto de tus funciones (get_games, get_top10_by_rating, etc.) quedan exactamente igual.


def get_games():
    conn = get_connection()
    query = "SELECT * FROM games"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def get_top10_by_rating():
    conn = get_connection()
    query = """
        SELECT TOP 10
            name,
            rating
        FROM games
        ORDER BY rating DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_avg_playtime_by_genre():
    conn = get_connection()
    query = """
        SELECT
            genres,
            AVG(playtime_forever) AS horas_promedio
        FROM games
        GROUP BY genres
        ORDER BY horas_promedio DESC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_games_filtered(genre=None, min_rating=0, max_price=1000):
    conn = get_connection()

    query = """
        SELECT
            name,
            genre,
            rating,
            price,
            playtime_forever
        FROM games
        WHERE rating >= ?
          AND price <= ?
    """

    params = [min_rating, max_price]

    if genre and genre != "Todos":
        query += " AND genre = ?"
        params.append(genre)

    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df



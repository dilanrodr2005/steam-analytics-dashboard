import pyodbc
import pandas as pd


def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=steam_analytics;"
        "Trusted_Connection=yes;"
    )


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



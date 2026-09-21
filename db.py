import pandas as pd


def get_games():
    # Lee los datos directamente del CSV subido a tu repositorio de GitHub
    return pd.read_csv("steam_games.csv")


def get_top10_by_rating():
    df = get_games()
    return df.sort_values(by="rating", ascending=False).head(10)[["name", "rating"]]


def get_avg_playtime_by_genre():
    df = get_games()
    return (
        df.groupby("genres")["playtime_forever"]
        .mean()
        .reset_index(name="horas_promedio")
        .sort_values(by="horas_promedio", ascending=False)
    )


def get_games_filtered(genre=None, min_rating=0, max_price=1000):
    df = get_games()

    # Filtrar por rating y precio
    df_filtered = df[(df["rating"] >= min_rating) & (df["price"] <= max_price)]

    # Filtrar por género si es distinto de "Todos"
    if genre and genre != "Todos":
        df_filtered = df_filtered[df_filtered["genre"] == genre]

    return df_filtered[["name", "genre", "rating", "price", "playtime_forever"]]

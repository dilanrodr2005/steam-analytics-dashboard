import pandas as pd

# 1. Cargar dataset original
df = pd.read_csv("steam.csv")

# 2. Eliminar juegos sin nombre
df = df.dropna(subset=["name"])

# 3. Calcular rating (0–10)
df["rating"] = (
    df["positive_ratings"] /
    (df["positive_ratings"] + df["negative_ratings"])
) * 10

# 4. Seleccionar columnas finales
df_clean = df[[
    "name",
    "price",
    "rating",
    "genres",
    "average_playtime"
]]

# 5. Renombrar columnas para SQL
df_clean = df_clean.rename(columns={
    "average_playtime": "playtime_forever"
})

# 6. Limpiar valores inválidos
df_clean = df_clean.dropna()
df_clean = df_clean[df_clean["rating"] > 0]

# 7. Guardar CSV limpio
df_clean.to_csv("steam_clean.csv", index=False)

print("steam_clean.csv creado")
print("Total juegos:", len(df_clean))

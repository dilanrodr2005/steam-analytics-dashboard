import streamlit as st
import db

st.title("Steam Analytics Dashboard")
st.markdown(
    "Explora y analiza datos de juegos de Steam usando filtros interactivos, métricas clave y visualizaciones."
)


# DATOS BASE

df_games = db.get_games()


# SIDEBAR - FILTROS


st.sidebar.markdown("### Filtros de búsqueda")

st.sidebar.title("Filtros")

genres = ["Todos"] + sorted(df_games["genres"].dropna().unique().tolist())
selected_genre = st.sidebar.selectbox(
    "Selecciona un género",
    genres
)

min_rating = st.sidebar.slider(
    "Rating mínimo",
    0.0, 10.0, 7.0, 0.5
)

max_price = st.sidebar.slider(
    "Precio máximo",
    float(df_games["price"].min()),
    float(df_games["price"].max()),
    float(df_games["price"].max())
)


# APLICAR FILTROS

df_filtered = df_games.copy()

if selected_genre != "Todos":
    df_filtered = df_filtered[df_filtered["genres"] == selected_genre]

df_filtered = df_filtered[
    (df_filtered["rating"] >= min_rating) &
    (df_filtered["price"] <= max_price)
]


# TABLA FILTRADA

st.subheader("Juegos filtrados")
st.dataframe(df_filtered)

st.download_button(
    label="📥 Descargar resultados en CSV",
    data=df_filtered.to_csv(index=False).encode("utf-8"),
    file_name="steam_filtered.csv",
    mime="text/csv"
)



# GRÁFICO TOP 10 POR RATING

st.markdown("**Top 10 juegos con mejor calificación según el rating promedio.**")

st.subheader("Top 10 juegos por rating")

df_top10 = db.get_top10_by_rating()

st.bar_chart(
    data=df_top10,
    x="name",
    y="rating"
)


# PROMEDIO DE HORAS POR GÉNERO

st.markdown("**Promedio de horas jugadas por género para analizar el engagement.**")

st.subheader("Promedio de horas jugadas por género")

df_playtime = db.get_avg_playtime_by_genre()

st.bar_chart(
    data=df_playtime,
    x="genres",
    y="horas_promedio"
)


# MÉTRICAS

st.subheader("Métricas clave")

total_games = len(df_filtered)
avg_rating = round(df_filtered["rating"].mean(), 2)
avg_playtime = round(df_filtered["playtime_forever"].mean(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("Total de juegos", total_games)
col2.metric("Rating promedio", avg_rating)
col3.metric("Horas promedio jugadas", avg_playtime)

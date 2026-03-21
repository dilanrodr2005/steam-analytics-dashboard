-- Crear base de datos
IF NOT EXISTS (
    SELECT name FROM sys.databases WHERE name = 'steam_analytics'
)
BEGIN
    CREATE DATABASE steam_analytics;
END
GO

-- Usar la base de datos
USE steam_analytics;
GO

-- Crear tabla
CREATE TABLE games (
    game_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(6,2),
    rating FLOAT,
    genres NVARCHAR(255),
    playtime_forever INT
);

-- Verificar datos
SELECT * FROM games;
-- ===================================================================
-- Script de Creacion de Esquema y Semillas para VideoRent (SQL Server)
-- ===================================================================
USE master;
GO

IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'VideoRentDB')
BEGIN
    CREATE DATABASE VideoRentDB;
END
GO

USE VideoRentDB;
GO

-- 1. Tabla Genero
IF OBJECT_ID('dbo.Genero', 'U') IS NOT NULL DROP TABLE dbo.Genero;
CREATE TABLE Genero (
    genero_id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- 2. Tabla Actor
IF OBJECT_ID('dbo.Actor', 'U') IS NOT NULL DROP TABLE dbo.Actor;
CREATE TABLE Actor (
    actor_id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL
);

-- 3. Tabla Pelicula
IF OBJECT_ID('dbo.Pelicula', 'U') IS NOT NULL DROP TABLE dbo.Pelicula;
CREATE TABLE Pelicula (
    pelicula_id INT IDENTITY(1,1) PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    subtitulada BIT NOT NULL,
    estreno BIT NOT NULL,
    genero_id INT NOT NULL,
    fecha_creacion DATETIME NULL,
    fecha_modificacion DATETIME NULL,
    CONSTRAINT FK_Pelicula_Genero FOREIGN KEY (genero_id) 
        REFERENCES Genero(genero_id)
);

-- 4. Tabla de Relacion Muchos a Muchos: PeliculaActor
IF OBJECT_ID('dbo.PeliculaActor', 'U') IS NOT NULL DROP TABLE dbo.PeliculaActor;
CREATE TABLE PeliculaActor (
    pelicula_id INT NOT NULL,
    actor_id INT NOT NULL,
    PRIMARY KEY (pelicula_id, actor_id),
    CONSTRAINT FK_PA_Pelicula FOREIGN KEY (pelicula_id) 
        REFERENCES Pelicula(pelicula_id) ON DELETE CASCADE,
    CONSTRAINT FK_PA_Actor FOREIGN KEY (actor_id) 
        REFERENCES Actor(actor_id) ON DELETE CASCADE
);

-- 5. Tabla Review (Reseñas)
IF OBJECT_ID('dbo.Review', 'U') IS NOT NULL DROP TABLE dbo.Review;
CREATE TABLE Review (
    review_id INT IDENTITY(1,1) PRIMARY KEY,
    comentario VARCHAR(500) NOT NULL,
    calificacion INT NOT NULL,
    pelicula_id INT NOT NULL,
    fecha_creacion DATETIME NULL,
    fecha_modificacion DATETIME NULL,
    CONSTRAINT FK_Review_Pelicula FOREIGN KEY (pelicula_id) 
        REFERENCES Pelicula(pelicula_id) ON DELETE CASCADE
);

-- 6. Tabla Alquiler
IF OBJECT_ID('dbo.Alquiler', 'U') IS NOT NULL DROP TABLE dbo.Alquiler;
CREATE TABLE Alquiler (
    alquiler_id INT IDENTITY(1,1) PRIMARY KEY,
    cliente_nombre VARCHAR(100) NOT NULL,
    pelicula_id INT NOT NULL,
    fecha_alquiler DATETIME NOT NULL,
    fecha_devolucion DATETIME NULL,
    monto_diario DECIMAL(10,2) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    CONSTRAINT FK_Alquiler_Pelicula FOREIGN KEY (pelicula_id) 
        REFERENCES Pelicula(pelicula_id)
);
GO

-- ===================================================================
-- Semillas de Datos Iniciales (Seeders)
-- ===================================================================
INSERT INTO Genero (nombre) VALUES ('Accion'), ('Sci-Fi'), ('Drama'), ('Comedia');

INSERT INTO Actor (nombre, apellidos) VALUES 
('Keanu', 'Reeves'), 
('Laurence', 'Fishburne'), 
('Leonardo', 'DiCaprio');

INSERT INTO Pelicula (titulo, subtitulada, estreno, genero_id, fecha_creacion, fecha_modificacion) 
VALUES 
('The Matrix', 1, 0, 2, GETDATE(), GETDATE()),
('Inception', 1, 0, 2, GETDATE(), GETDATE());

INSERT INTO PeliculaActor (pelicula_id, actor_id) VALUES (1, 1), (1, 2), (2, 3);

INSERT INTO Review (comentario, calificacion, pelicula_id, fecha_creacion, fecha_modificacion)
VALUES 
('Excelente pelicula, clasico del cine.', 5, 1, GETDATE(), GETDATE()),
('Efectos visuales revolucionarios.', 4, 1, GETDATE(), GETDATE()),
('Trama compleja e intrigante.', 5, 2, GETDATE(), GETDATE());

INSERT INTO Alquiler (cliente_nombre, pelicula_id, fecha_alquiler, fecha_devolucion, monto_diario, estado)
VALUES 
('Maria Rodriguez', 1, GETDATE(), NULL, 1500.00, 'ACTIVO'),
('Carlos Gomez', 2, GETDATE()-5, GETDATE()-1, 1200.00, 'DEVUELTO');
GO

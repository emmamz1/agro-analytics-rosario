CREATE DATABASE AgroIndustria_Rosario;
GO

USE AgroIndustria_Rosario;
GO

CREATE TABLE EstimacionesAgro (
    campaña VARCHAR(20),
    provincia_nombre VARCHAR(100),
    departamento_nombre VARCHAR(100),
    cultivo_nombre VARCHAR(100),
    superficie_sembrada_hectareas FLOAT,
    superficie_cosechada_hectareas FLOAT,
    produccion_toneladas FLOAT,
    rendimiento_kg_x_hectarea FLOAT
);
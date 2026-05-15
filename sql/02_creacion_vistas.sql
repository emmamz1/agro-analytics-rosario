USE AgroIndustria_Rosario;
GO

CREATE VIEW vw_Consumo_PowerBI AS
SELECT 
    campaña,
    departamento_nombre,
    cultivo_nombre,
    produccion_toneladas,
    superficie_sembrada_hectareas,
    superficie_cosechada_hectareas,
    -- Calculamos la superficie perdida (Brecha Siembra vs Cosecha)
    (superficie_sembrada_hectareas - superficie_cosechada_hectareas) AS superficie_perdida_ha,
    rendimiento_kg_x_hectarea
FROM EstimacionesAgro;
GO
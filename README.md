# Monitor de Inteligencia Productiva - Hinterland Rosario

![Dashboard Preview]()

## Descripción del Proyecto
Este proyecto desarrolla un flujo de datos integral (**Pipeline ETL**) para el análisis de la salud productiva del **Hinterland del Gran Rosario**. Se enfoca en los departamentos de "flete corto" (Rosario, San Lorenzo, Constitución y Caseros), cuya producción es el motor logístico de las terminales portuarias que concentran el ~80% de las exportaciones agroindustriales de Argentina.

A través del procesamiento de series históricas oficiales (1969-2024), el monitor permite identificar ciclos de rendimiento, volúmenes de producción y el impacto crítico de las mermas por contingencias climáticas en la región.

## Stack Tecnológico
* **Python (Pandas & SQLAlchemy):** Extracción, limpieza de datos e ingesta automatizada.
* **SQL Server:** Almacenamiento relacional y creación de vistas de negocio optimizadas.
* **Power BI:** Dashboard interactivo con análisis avanzado mediante DAX.

## Arquitectura de Datos
El proyecto sigue una arquitectura de pipeline profesional:
1.  **Extracción:** Obtención de datasets crudos del portal de Datos Abiertos de la Secretaría de Agricultura, Ganadería y Pesca (MagyP).
2.  **Transformación (ETL):** Procesamiento en Python para normalizar caracteres Unicode, corregir errores de encoding y filtrar el recorte geográfico específico del Hinterland.
3.  **Carga:** Ingesta de datos persistentes a SQL Server mediante **SQLAlchemy**, asegurando la integridad del modelo y la escalabilidad del proceso.
4.  **Visualización:** Creación de una capa de consumo mediante **Vistas SQL** para alimentar el reporte dinámico en Power BI.

## Insights y Análisis de Negocio
* **Análisis de Resiliencia:** Visualización de la brecha entre superficie sembrada y cosechada para medir la siniestralidad climática histórica.
* **Eficiencia del Hinterland:** Comparativa de rendimientos (Kg/Ha) por departamento para identificar los núcleos productivos más eficientes que alimentan el nodo exportador.
* **Ciclos de Producción:** Identificación de tendencias interanuales y el impacto de fenómenos climáticos en la disponibilidad de carga para exportación.

## Estructura del Repositorio
* `etl_limpieza.py`: Script de Python para la limpieza y normalización de datos.
* `sql_ingesta.py`: Script de automatización de carga a base de datos.
* `01_creacion_tablas.sql`: Script SQL para la creación de tablas y estructura.
* `02_creacion_vistas.sql`: Definición de vistas para el consumo de Power BI.
* `dashboard_agro_industria.pbix`: Dashboard final de Power BI.

---
**Autor:** Emmanuel Mendoza  
**Contexto:** Proyecto desarrollado como parte de la Tecnicatura Universitaria en Inteligencia Artificial (TUIA) - UNR.

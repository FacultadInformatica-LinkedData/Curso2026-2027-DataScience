# Autoevaluación del Hands-on 3

Grupo 05 · Paseo Verde Madrid

Importamos los dos CSV del Hands-on 1 en proyectos separados de OpenRefine.

- **Parques y jardines.** Completamos 11 códigos de distrito a partir de la correspondencia entre nombres y códigos de los dos CSV. Dejamos vacíos los tres registros cuyo nombre era el marcador genérico `DISTRITO` y que carecían de código. Eliminamos `PLANTA`, `ESCALERAS` y `FAX` porque estaban completamente vacías. El CSV final conserva 208 filas y tiene 29 columnas. El historial registra cinco operaciones.
- **Áreas caninas.** Convertimos `TOTAL_ELEM`, `COORD_GIS_X` y `COORD_GIS_Y` a valores numéricos en OpenRefine para preparar su uso en RDF. Comprobamos que los valores se conservan, incluidos los ceros de `TOTAL_ELEM`. Dejamos sin rellenar las latitudes y longitudes ausentes porque queda por confirmar la proyección exacta de las coordenadas X/Y. El CSV final conserva 113 filas y 23 columnas. El historial registra tres operaciones.

Exportamos los CSV actualizados a `csv/` y los historiales de operaciones a `openrefine/`. Comprobamos los recuentos de filas y operaciones de ambos conjuntos.

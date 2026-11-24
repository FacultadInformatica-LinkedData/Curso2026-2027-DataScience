# Hands-On 3 - Self-Assessment (Group 10)

## Dataset e Historial

* **Dataset original:** `csv/relacion-monumentos.csv`
* **Dataset limpio:** `csv/relacion-monumentos-updated.csv`
* **Historial de operaciones:** `openrefine/operations.json`

## Resumen de transformaciones

Se han realizado las siguientes operaciones usando transformaciones estándar en OpenRefine y transformaciones personalizadas:

1. **Eliminación de columnas redundantes:** Se borraron `pto_geolocalizado`, `coordenadas` y `poblacion` porque su información ya aparecía desglosada en las columnas de coordenadas y población.

2. **Códigos postales (`codigoPostal`):** Se añadió el cero inicial a los códigos de 4 dígitos para dejarlos en formato de texto de 5 dígitos.

3. **Limpieza de `Descripcion`:** Se eliminaron las etiquetas HTML y se limpiaron los espacios en blanco sobrantes.

4. **Formato numérico de coordenadas:** Se convirtieron `coordenadas_latitud` y `coordenadas_longitud` a tipo de dato numérico decimal.

5. **Separación de valores múltiples:** Se unificó el uso del separador `|` en las columnas multivaluadas (reemplazando comas en `tipoConstruccion` y `periodoHistorico`, y puntos y coma en `identificadorBienInteresCultural`).

6. **Estandarización de calles:** Se normalizó el formato de "sin número" a `, s/n` y se expandieron las abreviaturas principales (`Pza.`, `C/`, `Avda.`, `Ctra.`).

7. **Normalización de municipios y localidades:** En `poblacion_municipio` y `poblacion_localidad` se movieron los artículos entre paréntesis al principio del nombre (por ejemplo, `Burgo de Osma (El)` → `El Burgo de Osma`).

8. **Limpieza general de espacios:** Se eliminaron espacios iniciales, finales y dobles en las columnas de texto principales (`nombre`, `tipoMonumento`, `calle`, `clasificacion`, `periodoHistorico` y nombres de población).

## Lista de comprobación

- [x] Historial de operaciones exportado en `openrefine/operations.json`.
- [x] Dataset limpio exportado en `csv/relacion-monumentos-updated.csv`.
- [x] Dataset original conservado en `csv/relacion-monumentos.csv`.
- [x] Autoevaluación completada en `selfAssessmentHandsOn3.md`.
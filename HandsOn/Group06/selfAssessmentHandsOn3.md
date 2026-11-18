## Checklist de Tareas y Transformaciones

- **Importación del Dataset:** Sí. Se ha importado correctamente el dataset original de puntos de recarga de vehículos eléctricos en Madrid en OpenRefine asegurando la codificación UTF-8 y el delimitador adecuado.
- **Análisis y Limpieza de Datos:** Sí. Se han revisado los hallazgos previos, aplicando facetas de texto y numéricas para detectar inconsistencias, eliminar espacios sobrantes y corregir valores erróneos o vacíos.
- **Normalización y Transformación:** Sí. Se han utilizado algoritmos de agrupación (*clustering*) y transformaciones para unificar variantes tipográficas en campos clave (como operadores y distritos) y preparar los datos para la generación de RDF.
- **Exportación de Operaciones:** Sí. Se ha extraído y guardado el historial completo de las operaciones aplicadas en OpenRefine en formato JSON.

## Entregables en GitHub
- [x] Fichero JSON con las operaciones de OpenRefine (`openrefine/*.json` bajo el directorio `openrefine/`).
- [x] Fichero CSV con la versión actualizada y limpia del dataset (`csv/*-updated.csv` bajo el directorio `csv/`).
- [x] Autoevaluación (`selfAssessmentHandsOn3.md` en la raíz del directorio del grupo).

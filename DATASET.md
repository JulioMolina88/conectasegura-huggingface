# Dataset de reportes ConectaSegura

## Origen y propósito

El conjunto fue creado para fines académicos como apoyo al prototipo de la Actividad 4. Contiene ejemplos ficticios en español de reportes y opiniones de usuarios relacionados con llamadas potencialmente sospechosas. No contiene números telefónicos, nombres, ubicaciones ni datos personales reales.

Se usa para evaluar modelos preentrenados de análisis de sentimiento. La etiqueta expresa el tono del reporte, no confirma ni descarta que una llamada sea fraudulenta.

## Estructura del archivo

| Campo | Tipo | Descripción |
|---|---|---|
| `id_reporte` | Texto | Identificador único con formato `CS-001`. |
| `texto` | Texto | Reporte u opinión ficticia del usuario. |
| `etiqueta_sentimiento` | Categoría | `NEG`, `NEU` o `POS`. |
| `origen` | Texto | Indica que el dato es sintético académico. |
| `uso` | Texto | Partición prevista del registro: evaluación. |

## Distribución

El archivo contiene 30 registros balanceados: 10 negativos, 10 neutrales y 10 positivos. El equilibrio permite calcular métricas macro sin que una clase mayoritaria domine el resultado.

## Reproducibilidad

Desde la raíz del proyecto, ejecutar:

```bash
python src/generar_dataset.py
```

El script recrea exactamente `data/reportes_conectasegura.csv`. Para volver a correr la evaluación en Google Colab, se debe cargar este CSV en un DataFrame y usar `texto` como entrada y `etiqueta_sentimiento` como referencia.

## Limitaciones y uso responsable

El tamaño del conjunto es apropiado para comparar el comportamiento inicial de modelos, pero no para afirmar desempeño real de producción. Antes de cualquier implementación se deben usar reportes anonimizados, muestreo representativo, revisión legal y validación humana de etiquetas.

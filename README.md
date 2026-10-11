# ConectaSegura análisis de reportes de llamadas sospechosas

## Descripción del proyecto

Este repositorio contiene un prototipo académico de procesamiento de lenguaje natural para comparar modelos preentrenados de Hugging Face en el análisis de sentimiento de reportes en español relacionados con llamadas sospechosas.

El propósito es apoyar la priorización de atención de reportes. El resultado de sentimiento no confirma que una llamada sea fraudulenta y no debe activar bloqueos automáticos.

## Objetivo

Comparar RoBERTuito, XLM-RoBERTa y DistilBERT multilingüe con métricas de accuracy, precision macro, recall macro, F1 macro y latencia de inferencia.

## Resultado principal

XLM-RoBERTa obtuvo el mejor desempeño global en el conjunto de evaluación:

| Modelo | Accuracy | Precision macro | Recall macro | F1 macro | Latencia promedio |
|---|---:|---:|---:|---:|---:|
| XLM-RoBERTa | 0.633 | 0.700 | 0.633 | 0.644 | 136.71 ms |
| DistilBERT multilingüe | 0.600 | 0.700 | 0.600 | 0.576 | 29.96 ms |
| RoBERTuito | 0.567 | 0.712 | 0.567 | 0.570 | 78.19 ms |

XLM-RoBERTa se recomienda como línea base por su mayor F1 macro. Sin embargo, el desempeño actual no alcanza el umbral de F1 macro de 0.80 definido para una posible operación, por lo que debe ampliarse el conjunto de evaluación y considerar fine-tuning solo si se valida esa necesidad.

## Estructura

```text
conectasegura-huggingface/
├── data/
│   └── reportes_conectasegura.csv
├── notebooks/
│   └── Actividad_4_Punto_1_Colab_ConectaSegura.ipynb
├── results/
│   ├── resultados_modelos.csv
│   └── Actividad_4_Punto_2_Reporte_Comparativo_ConectaSegura.docx
├── src/
│   └── generar_dataset.py
├── DATASET.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Entorno de ejecución

El cuaderno fue diseñado para Google Colab. Se recomienda habilitar GPU en **Entorno de ejecución → Cambiar tipo de entorno de ejecución → GPU**.

Para una ejecución local:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows, activar el entorno con `.venv\Scripts\activate`.

## Ejecución

1. Genere o verifique el dataset:

   ```bash
   python src/generar_dataset.py
   ```

2. Abra el notebook de la carpeta `notebooks` en Google Colab.
3. Active GPU y ejecute las celdas en orden.
4. Conserve la tabla de métricas, las matrices de confusión y la gráfica de trade-offs.

## Datos y uso responsable

El dataset es sintético y académico; no contiene datos personales reales. La etiqueta representa sentimiento, no fraude confirmado. Antes de usar datos reales se requiere anonimización, controles de acceso, validación legal, muestreo representativo y revisión humana.

## Reproducibilidad

Las versiones de dependencias se documentan en `requirements.txt`. El script de `src` genera el CSV de manera determinista. Para replicar el experimento se debe usar el mismo dataset y los mismos identificadores de modelo incluidos en el notebook.

## Licencia académica

Este material se elaboró con fines académicos. Antes de una reutilización comercial se deben revisar las licencias de cada modelo en Hugging Face y las políticas aplicables al uso de datos.

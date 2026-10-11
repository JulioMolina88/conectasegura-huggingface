"""Genera de forma reproducible el dataset de evaluación de ConectaSegura.

El archivo resultante contiene reportes ficticios, sin datos personales reales,
y reproduce el conjunto usado para evaluar los modelos del Punto 1.
"""

from pathlib import Path
import csv

REGISTROS = [
    ("Me llamaron para pedirme mi contraseña y datos de mi tarjeta.", "NEG"),
    ("Recibí varias llamadas con amenazas para depositar dinero.", "NEG"),
    ("El número insistió en que compartiera el código de verificación.", "NEG"),
    ("La persona fingió ser del banco y solicitó información privada.", "NEG"),
    ("Me ofrecieron un premio, pero querían que hiciera una transferencia.", "NEG"),
    ("La llamada fue agresiva y me presionaron para pagar de inmediato.", "NEG"),
    ("Reporto una llamada sospechosa que intentó obtener mis datos.", "NEG"),
    ("Usaron mi nombre y dijeron que mi cuenta estaba comprometida.", "NEG"),
    ("Me marcaron desde números distintos con el mismo engaño.", "NEG"),
    ("La llamada parecía fraude porque pidieron acceso a mi aplicación.", "NEG"),
    ("Recibí una llamada desconocida y deseo verificar el número.", "NEU"),
    ("El teléfono marcó dos veces, pero no dejaron mensaje.", "NEU"),
    ("Quiero saber cómo reportar un número que no reconozco.", "NEU"),
    ("La llamada se cortó antes de que pudiera contestar.", "NEU"),
    ("Tengo una llamada perdida de un número sin identificar.", "NEU"),
    ("¿Pueden revisar si este número tiene reportes?", "NEU"),
    ("Me contactaron para una encuesta y no di información.", "NEU"),
    ("Deseo consultar las opciones de seguridad para llamadas.", "NEU"),
    ("El número no estaba en mis contactos y quiero información.", "NEU"),
    ("Solicito orientación sobre una llamada recibida hoy.", "NEU"),
    ("Gracias por avisarme que el número tenía reportes de fraude.", "POS"),
    ("La alerta de ConectaSegura me ayudó a evitar una estafa.", "POS"),
    ("El proceso para reportar la llamada fue claro y rápido.", "POS"),
    ("Me atendieron bien y resolvieron mi reporte.", "POS"),
    ("La aplicación identificó el riesgo antes de que respondiera.", "POS"),
    ("Agradezco la protección y las recomendaciones recibidas.", "POS"),
    ("La notificación fue útil para reconocer el intento de engaño.", "POS"),
    ("El canal de soporte respondió correctamente a mi consulta.", "POS"),
    ("Me siento más seguro con las alertas de llamadas sospechosas.", "POS"),
    ("La información de prevención fue muy útil.", "POS"),
]


def generar_dataset() -> Path:
    raiz = Path(__file__).resolve().parents[1]
    salida = raiz / "data" / "reportes_conectasegura.csv"
    salida.parent.mkdir(parents=True, exist_ok=True)

    with salida.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=["id_reporte", "texto", "etiqueta_sentimiento", "origen", "uso"],
        )
        escritor.writeheader()
        for indice, (texto, etiqueta) in enumerate(REGISTROS, start=1):
            escritor.writerow(
                {
                    "id_reporte": f"CS-{indice:03d}",
                    "texto": texto,
                    "etiqueta_sentimiento": etiqueta,
                    "origen": "sintético académico",
                    "uso": "evaluación",
                }
            )
    return salida


if __name__ == "__main__":
    archivo = generar_dataset()
    print(f"Dataset generado: {archivo}")
    print(f"Registros: {len(REGISTROS)}")

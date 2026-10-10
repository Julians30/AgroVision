# Ficha de modelo: clasificador de racimos de palma

**Modelo:** YOLO11m de clasificación, semilla 2026 (`palma_yolo11m_s2026.pt`, 19,9 MB, 10,4 millones de parámetros).
**Versión de la ficha:** 1.0, octubre de 2026.

## Uso previsto

Enseñanza e investigación: ilustrar el entrenamiento, la evaluación y los límites de un clasificador de imágenes con pocos datos.

## Usos no previstos

- Calificar fruta para liquidar pagos o descuentos.
- Decidir la cosecha sin revisión de una persona.
- Clasificar fotografías tomadas en condiciones distintas de las del conjunto de entrenamiento sin una validación propia.

## Datos de entrenamiento

*Outdoor Tenera Oil Palm Fruit Image: FFB Dataset* (MunirahRosbi, 2024), CC BY 4.0. 452 imágenes tras eliminar copias exactas: 312 de entrenamiento, 70 de validación y 70 de prueba, con partición por grupos de imágenes casi idénticas. Cinco clases: inmaduro (157), maduro (197), sobremaduro (72), dañado (15) y vacío (11). El criterio de las etiquetas no está documentado.

## Entrada y salida

Recibe el cuadrado central de la fotografía, reducido a 384 × 384 píxeles: en promedio queda fuera una cuarta parte de la imagen. Devuelve cinco probabilidades que suman 1. No tiene una respuesta para «esto no es un racimo».

## Resultados

Sobre las 70 imágenes de prueba:

| Medida | Valor |
|---|---|
| Exactitud | 0,943 (66 de 70) |
| F1 macro | 0,867 |
| F1 macro de las tres semillas del mismo tamaño | de 0,810 a 0,867; media de 0,846 |
| Tiempo por imagen | 18 ms en GPU L4; 60 ms en CPU |

Las clases dañado y vacío tienen 3 y 2 imágenes de prueba: su F1 depende de fotografías concretas.

## Condiciones en las que se sabe que falla

- **Desenfoque.** Con un desenfoque gaussiano de 2,5 píxeles, el F1 macro baja a 0,506. Los errores tienen dirección: los racimos se clasifican como más maduros de lo que son. La confianza apenas baja.
- **Pérdida de resolución, de contraste y ruido intenso.** Mismo efecto, en menor grado.
- **Imágenes ajenas.** Un fotograma de un galpón de pollos se clasifica como racimo inmaduro con una probabilidad de 0,96.
- **Fondo.** En al menos una imagen de prueba, la clase dañado se reconoce por la hierba sobre la que está el racimo, y no por el racimo.
- **Racimos en transición.** Dos racimos etiquetados como inmaduros, con frutos ya anaranjados, se clasifican como maduros.

## Recomendaciones de uso

- Fotografiar un solo racimo, centrado, sobre una superficie uniforme.
- Comprobar la nitidez de la fotografía antes de clasificar, y repetirla si es baja.
- Mostrar siempre las cinco probabilidades.
- Enviar a revisión las predicciones dudosas y, además, una muestra al azar de las claras. Con este modelo, la regla de revisión por confianza detiene 1 de 4 errores.

## Lo que no se ha probado

Otra plantación, otro material de siembra, otra cámara, un teléfono, el modelo convertido a otro formato. Ninguna interpretación agronómica se ha validado en campo.

## Referencia

Capítulos 7, 10 y 11 del libro.

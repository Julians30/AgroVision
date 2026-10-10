# AgroVisión: del píxel a la decisión

**Material complementario y paquete de reproducibilidad** del libro *AgroVisión: del píxel a la decisión. Procesamiento digital de imágenes y visión artificial aplicada a la producción agropecuaria*.

[![Licencia: AGPL v3](https://img.shields.io/badge/c%C3%B3digo-AGPL--3.0-blue.svg)](LICENSE)
[![Textos y figuras: CC BY 4.0](https://img.shields.io/badge/textos%20y%20figuras-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/deed.es)

---

## Resumen

Este repositorio reúne el código, los resultados numéricos y la documentación que sustentan el libro. La obra examina la cadena completa que separa una imagen de una decisión de manejo (adquisición, preprocesamiento, datos, modelo, indicador y decisión) mediante dos casos de estudio desarrollados con conjuntos de datos abiertos: la clasificación del estado de racimos de palma aceitera (*Elaeis guineensis* Jacq.) en cinco categorías, y la detección, el conteo y el seguimiento de pollos de engorde en galpón. El énfasis metodológico no recae en maximizar una métrica, sino en establecer cuánta confianza merece cada resultado: se cuantifican la variabilidad entre entrenamientos, la sensibilidad a la calidad de la imagen, la dependencia del protocolo de evaluación y la distancia entre la salida de un modelo y un indicador utilizable. Todas las cifras citadas en el texto pueden regenerarse con los notebooks aquí publicados, y los valores obtenidos por los autores se incluyen en formato legible por máquina.

## Abstract

This repository contains the code, numerical results and documentation supporting the book *AgroVisión: del píxel a la decisión* (in Spanish). The book follows the full chain from image to management decision through two case studies built on open datasets: five-class classification of oil palm fresh fruit bunches, and detection, counting and tracking of broiler chickens. The methodological focus is on how much each result can be trusted rather than on maximizing a metric: seed-to-seed variability, robustness to image degradation, dependence on the evaluation protocol, and the gap between model output and a usable indicator are all measured. Every figure reported in the text can be regenerated with the notebooks provided, and the authors' values are included in machine-readable form.

**Palabras clave:** visión por computador; aprendizaje profundo; agricultura de precisión; ganadería de precisión; palma aceitera; pollos de engorde; clasificación de imágenes; detección de objetos; seguimiento de múltiples objetos; reproducibilidad; robustez; interpretabilidad.

---

## 1. Propósito y alcance

El material tiene tres destinatarios: quien estudia con el libro y desea ejecutar cada análisis; quien enseña y necesita ejercicios con datos reales; y quien investiga y quiere verificar, reutilizar o refutar los resultados.

El repositorio **contiene**:

- los notebooks que generan cada figura, tabla y cifra del libro (publicados sin salidas);
- los archivos de valores y las tablas de resultados de cada experimento;
- la guía de ejecución, la descripción de los datos y las fichas de los modelos.

El repositorio **no contiene** imágenes, videos ni pesos de modelos. Los datos pertenecen a sus autores y se descargan de su fuente original; los pesos pueden regenerarse con los notebooks.

## 2. Casos de estudio y datos

| | Palma aceitera | Pollos de engorde |
|---|---|---|
| Tarea | Clasificación de imagen (5 clases) | Detección, conteo y seguimiento (1 clase) |
| Conjunto de datos | *Outdoor Tenera Oil Palm Fruit Image: FFB Dataset* (MunirahRosbi, 2024) | PIO (Boniche et al., 2026) |
| Tamaño | 466 imágenes; 452 tras eliminar copias exactas | 1 487 imágenes, 327 289 cajas anotadas, y videos |
| Partición usada | 312 / 70 / 70 (entrenamiento, validación, prueba), estratificada y por grupos de casi duplicados | 1 035 / 452 (entrenamiento, validación), la de los autores |
| Captura | Exteriores, luz natural; protocolo no documentado | Cámara cenital fija, 1 920 × 1 080 px, dos galpones de Panamá |
| Licencia | CC BY 4.0 | CC BY 4.0 |
| Identificador | [10.5281/zenodo.11114885](https://doi.org/10.5281/zenodo.11114885) | [10.1038/s41597-026-07114-5](https://doi.org/10.1038/s41597-026-07114-5) |

Las características y limitaciones de cada conjunto se describen en [docs/DATOS_Y_LICENCIAS.md](docs/DATOS_Y_LICENCIAS.md).

## 3. Diseño metodológico

Los análisis siguen un conjunto de reglas comunes, que el libro justifica en los capítulos 5, 6 y 10:

1. **Datos originales inalterados.** Todo dato procesado se obtiene por código a partir de los archivos descargados, con trazabilidad de cada imagen.
2. **Auditoría previa.** Inventario, detección de copias exactas (SHA-256) y de casi duplicados (huella perceptual), y verificación de anotaciones antes de entrenar.
3. **Partición sin fuga de información.** Los grupos de imágenes casi idénticas se asignan completos a un mismo subconjunto.
4. **Varias semillas.** Los clasificadores se entrenan con las semillas 2026, 2027 y 2028; se informa la media y el intervalo, no el mejor valor.
5. **Selección por validación.** El conjunto de prueba se usa una sola vez y no interviene en la elección de modelos ni de umbrales.
6. **Comparaciones pareadas.** Prueba de McNemar con corrección de Holm, intervalos por remuestreo y pruebas de permutación de signos.
7. **Protocolo explícito.** Cada métrica se informa con su procedimiento de cálculo; la precisión media se calcula con el protocolo de COCO ampliado a 1 000 detecciones por imagen.
8. **Resultados negativos.** Los experimentos que no mejoran el resultado se documentan igual que los que sí.

## 4. Estructura del repositorio

```
notebooks/
    libro/      NB_LIBRO_00 a NB_LIBRO_12: figuras y experimentos de cada capítulo
    palma/      NB00 a NB10: descarga, auditoría, partición, entrenamiento y evaluación
    pollos/     NB00 a NB08: descarga, auditoría, entrenamiento, conteo, seguimiento y zonas
resultados/     valores_capNN.json y tablas de cada experimento
modelos/        instrucciones de descarga de los pesos entrenados
docs/           guía de ejecución, datos y licencias, fichas de modelo
CITATION.cff    metadatos de cita
```

## 5. Correspondencia entre capítulos y notebooks

| Capítulo | Contenido | Notebook del libro |
|---|---|---|
| 1. Del campo a la imagen | Planteamiento y casos de estudio | NB_LIBRO_01 |
| 2. Fundamentos de la imagen digital | Píxel, espacios de color, histograma | NB_LIBRO_01 |
| 3. Calidad y preprocesamiento | Degradaciones, filtros, métricas de calidad | NB_LIBRO_02 |
| 4. Segmentación y medición clásica | Umbrales, morfología, contornos, conteo clásico | NB_LIBRO_03, NB_LIBRO_04 |
| 5. Construir un dataset confiable | Auditoría, duplicados, partición sin fuga | NB_LIBRO_06, NB_LIBRO_07 |
| 6. Aprendizaje profundo para visión | Redes convolucionales, transferencia, métricas | NB_LIBRO_05, NB_LIBRO_08 |
| 7. Caso palma africana | Clasificación en cinco estados | NB_LIBRO_09 |
| 8. Caso avícola | Detección y conteo | NB_LIBRO_10 |
| 9. Del fotograma al comportamiento | Seguimiento, movimiento y zonas | NB_LIBRO_11 |
| 10. ¿Se puede confiar en el modelo? | Grad-CAM, robustez, comparación de modelos | NB_LIBRO_12 |
| 11. Del resultado a la decisión | Indicadores y revisión manual | NB_LIBRO_12 (predicciones) |

Los notebooks de `palma/` y `pollos/` producen los modelos y las tablas de los que parten los notebooks del libro, y deben ejecutarse antes, en orden numérico.

## 6. Resultados principales

Las cifras siguientes resumen los hallazgos que el libro desarrolla. La última columna indica dónde verificarlas: un archivo de `resultados/`, cuando la cifra figura en él o se calcula directamente con sus columnas, o el notebook que la produce, cuando depende de archivos que no se publican por su tamaño.

**Clasificación de racimos de palma** (70 imágenes de prueba)

| Resultado | Valor | Fuente |
|---|---|---|
| F1 macro de YOLO11m, media de tres semillas (intervalo) | 0,846 (0,810 – 0,867) | `valores_cap07.json` |
| Diferencia de F1 macro medio entre los tamaños n, s y m | ≈ 0,01 | `valores_cap07.json` |
| Correlación entre F1 en validación y en prueba (9 entrenamientos) | 0,11 | calculada con `valores_cap07.json` |
| Errores concentrados en 6 de las 70 imágenes | 41 de 65 | `cap07_dificultad_prueba.csv` |
| F1 macro con desenfoque gaussiano de 2,5 px (modelo de referencia) | 0,867 → 0,506 | `cap10_experimentos/robustez_resumen.csv` |
| Exactitud media de nueve modelos con desenfoque de 2,5 px | 0,897 → 0,663 | `cap10_experimentos/robustez_resumen.csv` |
| Errores de madurez desplazados hacia una clase más madura, con ese desenfoque | 157 de 174 (9 modelos) | predicciones de NB_LIBRO_12 |
| Exactitud con desenfoque de 2,5 px: entrenamiento con copias desenfocadas frente a control | 0,905 frente a 0,786 | `cap10_experimentos/entreno_resumen.csv` |
| Predicciones que cambian al ocultar las celdas más activas de Grad-CAM, frente a celdas al azar | 48,6 % frente a 4,9 % | `valores_cap10.json` |
| Diferencia YOLO26 − YOLO11 en F1 macro (9 parejas; prueba de permutación) | +0,032 (p ≈ 0,31) | tablas de `palma/NB09` |

**Detección y conteo de pollos** (452 imágenes de validación)

| Resultado | Valor | Fuente |
|---|---|---|
| AP50 y AP50-95 de YOLO11s a 960 px (protocolo de COCO, 1 000 detecciones) | 0,975 y 0,752 | `valores_cap08.json` |
| AP50-95 del mismo detector con límite de 100 detecciones | 0,400 | `valores_cap10.json` |
| Error absoluto medio y sesgo de conteo | 13,9 y +13,2 aves por imagen | `valores_cap08.json` |
| Error de conteo al excluir la franja exterior del 5 % del encuadre | 4,2 aves por imagen | detecciones de NB_LIBRO_10 |
| Identificadores de seguimiento para unas 320 aves en 20 s (BoT-SORT) | 660 | `valores_cap09.json` |
| Aves que se desplazan más de media longitud de cuerpo en 2 s | 11 % | `valores_cap09.json` |
| AP50-95 de Faster R-CNN (5 épocas) frente a YOLO11s, mismo protocolo | 0,564 frente a 0,752 | `valores_cap10.json` |

## 7. Reproducibilidad

**Entorno.** Los resultados se obtuvieron en Google Colab con una GPU NVIDIA L4 y las versiones siguientes:

```
ultralytics==8.4.172
torch==2.11.0
torchvision==0.26.0
```

**Ejecución.** La guía completa está en [docs/EJECUCION.md](docs/EJECUCION.md). En síntesis: copiar los notebooks a Google Drive, ejecutar los de cada proyecto en orden numérico (el primero descarga los datos desde Zenodo) y, después, el notebook del capítulo de interés.

**Determinismo.** Las semillas y las particiones están fijadas. Con otra GPU o con otra versión de las bibliotecas, las métricas pueden variar en el último decimal y los tiempos de ejecución, de forma apreciable.

**Verificación.** Cada notebook del libro escribe un archivo `valores_capNN.json` con todas las cifras que el capítulo cita. Comparar ese archivo con el publicado en `resultados/` es la forma directa de comprobar una reproducción.

## 8. Modelos entrenados

Los pesos se distribuyen como archivos adjuntos a cada versión publicada (*Releases*). Cada modelo se acompaña de una ficha que declara su uso previsto, sus datos de entrenamiento, sus resultados y las condiciones en las que se sabe que falla (Mitchell et al., 2019):

- [Ficha del clasificador de racimos de palma](docs/FICHA_MODELO_clasificador_palma.md)
- [Ficha del detector de pollos de engorde](docs/FICHA_MODELO_detector_pollos.md)

## 9. Limitaciones

- Los dos conjuntos de datos son de terceros. Ningún modelo se ha evaluado con imágenes de una plantación o de un galpón distintos de los de esos conjuntos.
- El conjunto de palma no documenta su protocolo de captura ni el criterio de sus etiquetas; las clases *dañado* y *vacío* tienen 3 y 2 imágenes de prueba.
- El detector y los modelos de comparación se entrenaron una sola vez; el conjunto PIO no dispone de un subconjunto de prueba independiente.
- El análisis de video se basa en dos fragmentos de 45 y de 20 segundos, sin identidades anotadas.
- Las interpretaciones agronómicas y avícolas proceden de una revisión documental y no se han validado en campo.

En consecuencia, el material es adecuado para la enseñanza y la investigación metodológica, y **no** constituye una herramienta validada para decisiones de producción.

## 10. Consideraciones éticas y licencias

- **Código** (notebooks): [GNU Affero General Public License v3.0](LICENSE). Los notebooks dependen de la biblioteca Ultralytics, distribuida bajo la misma licencia.
- **Textos, tablas y figuras propias:** Creative Commons Atribución 4.0 Internacional.
- **Datos:** cada conjunto conserva la licencia y la atribución de sus autores (CC BY 4.0). Quien reutilice modelos o figuras derivados de ellos debe mantener esa atribución.

El uso de sistemas de este tipo para calificar producto, liquidar pagos o vigilar instalaciones afecta a terceros. El capítulo 11 del libro discute las condiciones mínimas de transparencia, revisión humana y protección de las personas que aparecen en las imágenes.

## 11. Cómo citar

Si utiliza este material, cite el libro y el repositorio. Los metadatos están en [CITATION.cff](CITATION.cff); GitHub genera la cita en el botón «Cite this repository».

> *AgroVisión: del píxel a la decisión. Material complementario* (versión 1.0.0) [Software y datos]. GitHub. https://github.com/Julians30/AgroVision

Cite también los conjuntos de datos originales.

## 12. Referencias

Boniche, K., Cruz, E., Rangel, J. C., Hidalgo-Rodríguez, M., y Gómez-Donoso, F. (2026). PIO, a large-scale dataset for broiler chicken detection under real poultry farming conditions. *Scientific Data, 13*, Artículo 801. https://doi.org/10.1038/s41597-026-07114-5

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., y Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12), 86–92. https://doi.org/10.1145/3458723

Hendrycks, D., y Dietterich, T. (2019). Benchmarking neural network robustness to common corruptions and perturbations. En *7th International Conference on Learning Representations*. https://openreview.net/forum?id=HJz6tiCqYm

Jocher, G., Qiu, J., y Chaurasia, A. (2023). *Ultralytics YOLO* [Programa informático]. https://github.com/ultralytics/ultralytics

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., y Gebru, T. (2019). Model cards for model reporting. En *Proceedings of the Conference on Fairness, Accountability, and Transparency* (pp. 220–229). ACM. https://doi.org/10.1145/3287560.3287596

MunirahRosbi. (2024). *Outdoor Tenera Oil Palm Fruit Image: FFB Dataset* (Versión v1) [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.11114885

Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., y Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. En *2017 IEEE International Conference on Computer Vision* (pp. 618–626). IEEE. https://doi.org/10.1109/ICCV.2017.74

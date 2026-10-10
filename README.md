# AgroVisión: del píxel a la decisión

Material complementario del libro *AgroVisión: del píxel a la decisión. Procesamiento digital de imágenes y visión artificial aplicada a la producción agropecuaria*.

El libro desarrolla dos casos con datos abiertos y los sigue desde la fotografía hasta el indicador:

- **Palma africana:** clasificación de racimos en cinco estados (inmaduro, maduro, sobremaduro, dañado y vacío).
- **Pollos de engorde:** detección, conteo, seguimiento y uso del espacio en galpón.

Este repositorio contiene los notebooks que generan cada figura, tabla y cifra del libro, y los archivos de valores con los resultados que el texto cita.

## Contenido

```
notebooks/
    libro/      NB_LIBRO_00 a NB_LIBRO_12: figuras y experimentos de cada capítulo
    palma/      NB00 a NB10 del proyecto PALMA_AFRICANA_YOLO
    pollos/     NB00 a NB08 del proyecto AgroUTMACH_PIX
resultados/     archivos de valores por capítulo (valores_capNN.json) y tablas de cada experimento
modelos/        instrucciones de descarga de los pesos entrenados (no se guardan en git)
docs/           fichas de modelo, datos y licencias, guía de ejecución
```

Los notebooks se publican sin salidas, para que el repositorio sea ligero. Al ejecutarlos se regeneran.

## Notebooks del libro

| Notebook | Contenido | Capítulo | Equipo |
|---|---|---|---|
| NB_LIBRO_00_Empaquetar_resultados_v2 | Utilidad: reúne en un paquete las tablas de los dos proyectos | — | CPU |
| NB_LIBRO_01_Figuras_Capitulos_1_2_v2 | Presentación de los casos, color e histogramas | 1 y 2 | GPU |
| NB_LIBRO_02_Figuras_Capitulo_3_v2 | Degradaciones, filtros y métricas de calidad | 3 | CPU |
| NB_LIBRO_03_Figuras_Capitulo_4 | Umbrales, segmentación por color, morfología y contornos | 4 | CPU |
| NB_LIBRO_04_Conteo_clasico_con_correccion | Conteo de aves con visión clásica | 4 | CPU |
| NB_LIBRO_05_Reevaluacion_mAP_detectores | Precisión media con el protocolo de COCO y conteo por imagen | 6 y 8 | GPU |
| NB_LIBRO_06_Figuras_Capitulo_5 | Inventario, duplicados, partición y formato de anotación | 5 | CPU |
| NB_LIBRO_07_Experimento_purga_particion_palma | Efecto de los casi duplicados entre particiones | 5 | GPU |
| NB_LIBRO_08_Figuras_y_experimentos_Capitulo_6 | Filtros aprendidos, transferencia y métricas | 6 | GPU |
| NB_LIBRO_09_Figuras_y_experimentos_Capitulo_7 | Nueve clasificadores, clases escasas e imágenes ajenas | 7 | GPU |
| NB_LIBRO_10_Figuras_y_experimentos_Capitulo_8 | Tamaño de imagen, umbrales y análisis del conteo | 8 | GPU |
| NB_LIBRO_11_Figuras_y_experimentos_Capitulo_9 | Algoritmos de seguimiento, movimiento y zonas | 9 | GPU |
| NB_LIBRO_12_Figuras_y_experimentos_Capitulo_10 | Grad-CAM, robustez y comparación de modelos | 10 y 11 | GPU |

Los notebooks de `palma/` y `pollos/` descargan los datos, entrenan los modelos y producen los resultados de cada proyecto. Deben ejecutarse antes que los del libro, en su orden numérico.

## Cómo ejecutarlos

Los notebooks están preparados para Google Colab y esperan tres carpetas en Google Drive: `PALMA_AFRICANA_YOLO`, `AgroUTMACH_PIX` y `AGROVISION_LIBRO`. La guía completa está en [docs/EJECUCION.md](docs/EJECUCION.md). En resumen:

1. Copie los notebooks a las carpetas correspondientes de su Drive.
2. Ejecute los notebooks de cada proyecto en orden. El primero de cada uno descarga los datos desde Zenodo.
3. Abra el notebook del capítulo que le interese, elija una GPU si la requiere y ejecute todas las celdas.

Los resultados del libro se obtuvieron con una GPU NVIDIA L4 y estas versiones:

```
ultralytics==8.4.172
torch==2.11.0
torchvision==0.26.0
```

## Datos

Este repositorio **no contiene imágenes ni videos**. Los dos conjuntos son públicos, se distribuyen con licencia CC BY 4.0 y los notebooks los descargan de su origen:

- MunirahRosbi. (2024). *Outdoor Tenera Oil Palm Fruit Image: FFB Dataset* (v1). Zenodo. https://doi.org/10.5281/zenodo.11114885
- Boniche, K., Cruz, E., Rangel, J. C., Hidalgo-Rodríguez, M., y Gómez-Donoso, F. (2026). PIO, a large-scale dataset for broiler chicken detection under real poultry farming conditions. *Scientific Data, 13*, 801. https://doi.org/10.1038/s41597-026-07114-5

Más detalles en [docs/DATOS_Y_LICENCIAS.md](docs/DATOS_Y_LICENCIAS.md).

## Modelos entrenados

Los pesos no se guardan en el repositorio. Se publican como archivos de cada versión (*Releases*), y pueden regenerarse con los notebooks. Antes de usarlos, lea su ficha:

- [Clasificador de racimos de palma](docs/FICHA_MODELO_clasificador_palma.md)
- [Detector de pollos de engorde](docs/FICHA_MODELO_detector_pollos.md)

## Qué no debe esperarse de este material

Los modelos se entrenaron y evaluaron con datos de terceros. Ninguno se ha probado en una plantación o en un galpón distintos de los de esos conjuntos, y las interpretaciones agronómicas del libro proceden de una revisión documental. Son material de enseñanza y de investigación, no herramientas validadas para tomar decisiones de producción.

## Licencias

- **Código** (notebooks y scripts): véase el archivo `LICENSE`.
- **Textos, tablas y figuras propias:** CC BY 4.0.
- **Imágenes de los conjuntos de datos** que aparezcan en figuras: CC BY 4.0, de sus autores originales.

## Cómo citar

Véase [CITATION.cff](CITATION.cff). GitHub muestra la cita en el botón «Cite this repository».

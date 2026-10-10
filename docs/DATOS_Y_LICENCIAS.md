# Datos y licencias

## Conjuntos de datos

Este repositorio no redistribuye imágenes ni videos. Los notebooks descargan los dos conjuntos desde su origen.

| Caso | Conjunto | Contenido | Licencia | Identificador |
|---|---|---|---|---|
| Palma | *Outdoor Tenera Oil Palm Fruit Image: FFB Dataset* (MunirahRosbi, 2024) | 466 fotografías de racimos en cinco clases; 452 tras eliminar copias exactas | CC BY 4.0 | https://doi.org/10.5281/zenodo.11114885 |
| Pollos | PIO (Boniche et al., 2026) | 1 487 imágenes con 327 289 aves anotadas, y videos | CC BY 4.0 | https://doi.org/10.1038/s41597-026-07114-5 |

La licencia CC BY 4.0 permite usar, modificar y redistribuir el material, también con fines comerciales, a condición de citar a sus autores. Quien publique figuras o modelos derivados de estos conjuntos debe mantener esa atribución.

## Lo que conviene saber de cada conjunto

**Palma.** El repositorio de origen no documenta el protocolo de captura ni el criterio con que se asignaron las etiquetas. Las clases dañado y vacío tienen 15 y 11 imágenes. La resolución de las fotografías y el fondo están asociados a la clase (véanse las secciones 5.2 y 10.2 del libro).

**Pollos.** Las imágenes proceden de dos galpones de Panamá, con cámara cenital fija. El conjunto se distribuye partido en entrenamiento (1 035 imágenes) y validación (452); no tiene un subconjunto de prueba aparte. Las anotaciones son incompletas en la franja exterior del encuadre (sección 8.4 del libro).

## Licencia de este repositorio

- Código: véase `LICENSE`. Los notebooks usan la biblioteca Ultralytics, que se distribuye con licencia AGPL-3.0.
- Textos, tablas y figuras propias: CC BY 4.0.

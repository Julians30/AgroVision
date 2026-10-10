# Guía de ejecución

## 1. Preparar Google Drive

Los notebooks esperan esta estructura en «Mi unidad»:

```
PALMA_AFRICANA_YOLO/04_NOTEBOOKS/      notebooks de notebooks/palma
AgroUTMACH_PIX/02_NOTEBOOKS/           notebooks de notebooks/pollos
AGROVISION_LIBRO/01_NOTEBOOKS/         notebooks de notebooks/libro
```

Las demás carpetas las crean los propios notebooks al ejecutarse.

## 2. Ejecutar los proyectos

En cada proyecto, ejecute los notebooks en orden numérico. `NB00` crea las carpetas y descarga el conjunto de datos desde Zenodo. Los notebooks de entrenamiento requieren GPU.

## 3. Ejecutar los notebooks del libro

1. Abra el notebook con Google Colab.
2. Menú «Entorno de ejecución» → «Cambiar tipo de entorno de ejecución» → GPU, si el notebook la requiere.
3. «Ejecutar todas». La primera celda pide permiso para acceder a Drive.
4. Al terminar, las figuras quedan en `AGROVISION_LIBRO/02_FIGURAS/capNN`, los valores en `AGROVISION_LIBRO/03_VALORES` y el navegador descarga un paquete comprimido.

## Reglas que siguen los notebooks del libro

- Solo leen las carpetas de los proyectos; nunca escriben en ellas.
- Cada sección se ejecuta de forma independiente: un error en una no detiene las demás, y queda anotado al final.
- Los entrenamientos terminados se guardan y se reutilizan si el notebook se ejecuta de nuevo.
- Todas las cifras que el libro cita se escriben en `valores_capNN.json`.

## Versiones

```
pip install ultralytics==8.4.172
```

Con otra versión de las bibliotecas o con otra GPU, las métricas pueden variar en el último decimal y los tiempos, bastante más. El notebook del capítulo 10 es el más largo: entre 25 y 40 minutos en una GPU L4.

## Semillas y particiones

Las semillas son 2026, 2027 y 2028. La partición del caso de palma (312 imágenes de entrenamiento, 70 de validación y 70 de prueba) se guarda en `PALMA_AFRICANA_YOLO/03_SPLITS`. Para comparar un modelo nuevo con los del libro debe usarse esa misma partición.

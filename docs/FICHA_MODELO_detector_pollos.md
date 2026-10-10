# Ficha de modelo: detector de pollos de engorde

**Modelo:** YOLO11s de detección, entrenado a 960 píxeles (`pollos_yolo11s_960.pt`, 19,2 MB, 9,4 millones de parámetros).
**Versión de la ficha:** 1.0, octubre de 2026.

## Uso previsto

Enseñanza e investigación: detección y conteo de aves visibles en imágenes cenitales de galpón, y base para seguimiento y análisis del uso del espacio.

## Usos no previstos

- Inventario del lote: el modelo cuenta las aves que la cámara ve, no las alojadas.
- Diagnóstico de bienestar o de salud.
- Uso en otro galpón, con otra cámara o a otra altura sin una validación propia.

## Datos de entrenamiento

Conjunto PIO (Boniche et al., 2026), CC BY 4.0: 1 035 imágenes de entrenamiento y 452 de validación, de un galpón comercial y un galpón prototipo de Panamá, durante las seis semanas del ciclo. Cámara cenital fija a unos 2 m, 1 920 × 1 080 píxeles. Una clase. El conjunto no tiene subconjunto de prueba: las cifras son de validación.

## Entrenamiento

60 épocas, 35 minutos en una GPU L4, una sola semilla, con el aumento de datos por defecto de la biblioteca.

## Resultados

Sobre las 452 imágenes de validación, con hasta 1 000 detecciones por imagen:

| Medida | Valor |
|---|---|
| AP50 | 0,975 |
| AP50-95 (protocolo de COCO) | 0,752 |
| Precisión y sensibilidad, umbral de confianza de 0,25 | 0,900 y 0,973 |
| Error absoluto medio de conteo | 13,9 aves por imagen (8,5 %) |
| Sesgo de conteo | +13,2 aves |
| Error de conteo en galpón comercial y en prototipo | 21,8 y 2,3 aves |
| Error de conteo excluyendo la franja exterior del 5 % | 4,2 aves |

## Parámetros de uso

`imgsz=960`, `conf=0.25`, `max_det=1000`. Con el límite de detecciones por defecto de la biblioteca se pierden aves en las escenas densas.

## Condiciones en las que se sabe que falla

- **Escenas densas.** El conteo excede a la anotación en un 9 % en el galpón comercial. Una parte del exceso son aves reales no anotadas en los bordes del encuadre.
- **Aves pequeñas.** En la primera semana se le escapan 5 de cada 100.
- **Bordes del encuadre.** Detecciones menos fiables y aves cortadas.
- **Video.** El conteo oscila unas 2 aves entre fotogramas consecutivos sin que nada cambie. Los primeros fotogramas de un clip recortado pueden decodificarse incompletos.
- **Seguimiento.** Con ByteTrack o BoT-SORT, el número de identificadores duplica al de aves en 20 segundos: no sirve para contar animales.

## Recomendaciones de uso

- Definir una zona de conteo que excluya la franja exterior del encuadre.
- Contar con un fotograma por segundo y resumir con una mediana.
- Informar siempre el error absoluto junto al sesgo.
- No convertir píxeles en distancias ni recuentos en densidades sin calibrar la cámara.

## Lo que no se ha probado

Otro galpón, otra cámara, otra altura, otra iluminación, otra línea genética. Varias semillas. El modelo en un equipo de bajo consumo.

## Referencia

Capítulos 8, 9, 10 y 11 del libro.

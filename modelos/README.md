# Modelos entrenados

Los pesos no se guardan en git (el límite por archivo es de 100 MB). Se publican como archivos de cada versión, en la pestaña **Releases** del repositorio.

| Archivo | Tarea | Tamaño | Resultado |
|---|---|---|---|
| palma_yolo11m_s2026.pt | Clasificar racimos | 19,9 MB | F1 macro de 0,867 en prueba |
| palma_yolo11n_s2026.pt | Clasificar racimos | 3,0 MB | F1 macro de 0,813 en prueba |
| pollos_yolo11s_960.pt | Detectar aves | 19,2 MB | AP50-95 de 0,752 en validación |

Uso mínimo:

```python
from ultralytics import YOLO
modelo = YOLO('palma_yolo11m_s2026.pt')
salida = modelo.predict('racimo.jpg', imgsz=384)[0]
print(salida.names[salida.probs.top1], float(salida.probs.top1conf))
```

Lea la ficha de cada modelo en `docs/` antes de usarlo.

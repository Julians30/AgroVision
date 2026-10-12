#!/usr/bin/env python3
"""Auditoría ligera de la estructura pública de AgroVisión.

No descarga datos externos, no entrena modelos y no verifica las métricas
científicas reproduciendo experimentos costosos. Usa solo Python estándar.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "requirements.txt",
    "docs/DATOS_Y_LICENCIAS.md",
    "docs/EJECUCION.md",
    "guiones/cap11_indicadores.py",
    "resultados/valores_para_texto.json",
)
MIN_NOTEBOOKS = {"libro": 13, "palma": 11, "pollos": 10}
FROZEN_CHAPTERS = tuple(range(3, 11))


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    for relative in REQUIRED:
        check((ROOT / relative).is_file(), f"Falta archivo: {relative}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    check("GNU AFFERO GENERAL PUBLIC LICENSE" in license_text,
          "LICENSE no identifica AGPL")
    citation_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    check("AgroVisión" in citation_text and "AGPL-3.0" in citation_text,
          "Metadatos de cita y licencia no coinciden")

    notebook_count = 0
    for folder, expected_minimum in MIN_NOTEBOOKS.items():
        notebooks = sorted((ROOT / "notebooks" / folder).glob("*.ipynb"))
        check(len(notebooks) >= expected_minimum,
              f"Faltan notebooks de {folder}: {len(notebooks)}")
        for path in notebooks:
            notebook = json.loads(path.read_text(encoding="utf-8"))
            check(notebook.get("nbformat") == 4,
                  f"Formato Jupyter inesperado: {path}")
            cells = notebook.get("cells")
            check(isinstance(cells, list) and len(cells) > 0,
                  f"Notebook sin celdas: {path}")
        notebook_count += len(notebooks)

    for chapter in FROZEN_CHAPTERS:
        path = ROOT / "resultados" / f"valores_cap{chapter:02d}.json"
        check(path.is_file(), f"Falta resumen del capítulo {chapter}")
        values = json.loads(path.read_text(encoding="utf-8"))
        check(isinstance(values, dict), f"Resultados no tabulados: {path}")

    data_tables = sorted((ROOT / "resultados").rglob("*.csv"))
    check(len(data_tables) >= 20, "No se encontraron suficientes tablas de resultados")
    for path in data_tables:
        check(path.stat().st_size > 0, f"Tabla vacía: {path}")

    print("AUDITORÍA AGROVISIÓN: CORRECTA")
    print(f"Notebooks Jupyter revisados: {notebook_count}")
    print(f"Resúmenes de capítulos revisados: {len(FROZEN_CHAPTERS)}")
    print(f"Tablas CSV no vacías: {len(data_tables)}")
    print("Código: licencia AGPL; textos/figuras: condiciones separadas.")
    print("Este control NO reentrena modelos ni certifica exactitud de métricas.")


if __name__ == "__main__":
    main()

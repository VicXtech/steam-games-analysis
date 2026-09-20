"""
Coleta dados de jogos da Steam via SteamSpy API.

- SteamSpy realiza uma paginação dos resultados: cada página retorna até 1000 jogos,
- ordenados por owners (mais populares primeiro nas primeiras páginas).
- O endpoint recomenda no máximo 1 request/segundo.

Uso:
    python collect_steamspy.py --pages 5
    (5 páginas +/- 5000 jogos)
"""

import argparse
import json
import time
from pathlib import Path

import requests

STEAMSPY_URL = "https://steamspy.com/api.php"
REQUEST_DELAY_SECONDS = 65  # margem de segurança acima do limite de 1 req/s
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def fetch_page(page: int) -> dict:
    """Busca uma página de até 1000 jogos (request=all é paginado)."""
    params = {"request": "all", "page": page}
    response = requests.get(STEAMSPY_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def collect(num_pages: int) -> dict:
    """Percorre N páginas e consolida os jogos em um único dicionário."""
    all_games: dict = {}

    for page in range(num_pages):
        print(f"Coletando página {page}...")
        page_data = fetch_page(page)

        if not page_data:
            print(f"Página {page} veio vazia — parando aqui.")
            break

        all_games.update(page_data)
        print(f"  -> {len(page_data)} jogos nessa página "
              f"(total acumulado: {len(all_games)})")

        time.sleep(REQUEST_DELAY_SECONDS)

    return all_games


def save(games: dict, filename: str = "steamspy_raw.json") -> Path:
    DATA_DIR.mkdir(exist_ok=True)
    output_path = DATA_DIR / filename

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(games, f, ensure_ascii=False, indent=2)

    print(f"\nSalvo: {output_path} ({len(games)} jogos no total)")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Coleta dados de jogos via SteamSpy")
    parser.add_argument(
        "--pages",
        type=int,
        default=5,
        help="Número de páginas a coletar (cada uma ~1000 jogos). Default: 5.",
    )
    args = parser.parse_args()

    games = collect(args.pages)
    save(games)


if __name__ == "__main__":
    main()
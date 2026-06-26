"""
Prode Toros 2026 - Actualizador de datos
Lee el Google Sheet y genera docs/data.json, luego hace push a GitHub.
Uso: python update_prode.py
     python update_prode.py --no-push  (solo genera el JSON, sin publicar)
"""

import csv
import io
import json
import os
import subprocess
import sys
from datetime import datetime
import urllib.request
import urllib.error

# --- Configuracion ---
SHEET_ID = "112gxMftT2pKnt3WPfbtrfhTaedodnmWZgOzEYdChYXg"
GID_DATA  = "587902986"   # Tab: DATA PARA TABLA

COLOR_PALETTE = {
    "Tomi Samitier":  "#FF5733",
    "Nico Conti":     "#33FF57",
    "Patru Maqui":    "#3357FF",
    "Lucas Tkacz":    "#FF33A1",
    "Epe Roth":       "#A133FF",
    "Tomi Marchiano": "#33FFF0",
    "Alejo Di Fiori": "#FF8F33",
    "Pulpo":          "#8FFF33",
    "Nico Gianola":   "#FF3333",
    "Fran Garoby":    "#33FF8F",
    "JZ":             "#8F33FF",
    "Juan Leoni":     "#FF338F",
    "Kovacic":        "#338FFF",
    "Conrado":        "#FFC133",
    "Gian Luttini":   "#33FFC1",
    "Fede Lacal":     "#C133FF",
}


def get_phase(match_id: str) -> str:
    num = match_id.replace("P", "")
    if not num.isdigit():
        return "Grupo"
    n = int(num)
    if n <= 72:   return "Grupo"
    if n <= 88:   return "16avos"
    if n <= 96:   return "Octavos"
    if n <= 100:  return "Cuartos"
    if n <= 102:  return "Semis"
    if n == 103:  return "Tercer Puesto"
    return "Final"


def fetch_csv(gid: str) -> str:
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={gid}"
    with urllib.request.urlopen(url) as r:
        return r.read().decode("utf-8-sig")


def parse_data(csv_text: str) -> dict:
    rows = list(csv.reader(io.StringIO(csv_text)))

    # Fila 0: N, Partido, Jugador1,,, Jugador2,,, ...
    # Fila 1: sub-headers (Pred.Local, Pred.Visitante, Puntos)
    # Filas 2+: datos de partidos
    # Ultima fila: "total puntaje"

    # Extraer nombres de jugadores (cada 3 columnas desde col 2)
    players = [rows[0][c].strip() for c in range(2, len(rows[0]), 3) if rows[0][c].strip()]

    matches_played = []
    history = {p: [0] for p in players}
    upcoming = []

    for row in rows[2:]:
        if not row or not row[0].strip() or not row[0].strip().startswith("P"):
            continue
        match_id   = row[0].strip()
        match_name = row[1].strip() if len(row) > 1 else ""
        if not match_name:
            continue

        # Extraer prediccion y puntos de cada jugador
        player_data = {}
        for i, player in enumerate(players):
            base = 2 + i * 3
            pred_l = row[base    ].strip() if base     < len(row) else ""
            pred_v = row[base + 1].strip() if base + 1 < len(row) else ""
            pts_s  = row[base + 2].strip() if base + 2 < len(row) else "0"
            player_data[player] = {
                "pred": f"{pred_l}-{pred_v}" if pred_l and pred_v else "",
                "pts":  int(pts_s) if pts_s.lstrip("-").isdigit() else 0,
            }

        total_pts  = sum(d["pts"] for d in player_data.values())
        has_preds  = any(d["pred"] for d in player_data.values())

        if total_pts > 0:
            # Partido jugado: avanzar historico acumulado
            matches_played.append(match_name)
            for p in players:
                history[p].append(history[p][-1] + player_data[p]["pts"])

        elif has_preds:
            # Partido proximo: predicciones cargadas, sin resultado aun
            score_groups: dict[str, list] = {}
            for player in players:
                score = player_data[player]["pred"]
                if score:
                    score_groups.setdefault(score, []).append(player)

            preds = sorted(
                [{"score": s, "count": len(v), "voters": v} for s, v in score_groups.items()],
                key=lambda x: -x["count"],
            )
            upcoming.append({
                "id":          match_id,
                "phase":       get_phase(match_id),
                "match":       match_name,
                "predictions": preds,
            })

    # Ranking final (ordenado por puntos desc)
    final_pts = {p: history[p][-1] for p in players}
    sorted_players = sorted(players, key=lambda p: -final_pts[p])
    ranking = [{"pos": i + 1, "name": p, "pts": final_pts[p]} for i, p in enumerate(sorted_players)]
    top3    = {r["name"]: r["pos"] for r in ranking if r["pos"] <= 3}

    return {
        "last_updated":   datetime.now().strftime("%d/%m/%Y %H:%M"),
        "players":        players,
        "matches_played": matches_played,
        "history":        history,
        "ranking":        ranking,
        "top3":           top3,
        "upcoming":       upcoming,
        "colors":         COLOR_PALETTE,
    }


def git_push(timestamp: str) -> None:
    cmds = [
        ["git", "add", "docs/data.json"],
        ["git", "commit", "-m", f"datos: {timestamp}"],
        ["git", "push"],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            # "nothing to commit" no es un error real
            if "nothing to commit" in result.stdout + result.stderr:
                print("  (sin cambios nuevos, ya estaba actualizado)")
                return
            raise RuntimeError(f"Error en '{' '.join(cmd)}':\n{result.stderr}")


def main() -> None:
    no_push = "--no-push" in sys.argv

    print("=" * 50)
    print("  PRODE TOROS 2026 - Actualizador")
    print("=" * 50)

    print("\n[1/3] Leyendo Google Sheet...")
    try:
        csv_text = fetch_csv(GID_DATA)
    except urllib.error.URLError as e:
        print(f"  ERROR: No se pudo conectar a Google Sheets.\n  {e}")
        sys.exit(1)

    print("[2/3] Procesando datos...")
    data = parse_data(csv_text)

    os.makedirs("docs", exist_ok=True)
    out = os.path.join("docs", "data.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n  Partidos jugados : {len(data['matches_played'])}")
    print(f"  Proximos partidos: {len(data['upcoming'])}")
    lider = data["ranking"][0]
    print(f"  Lider            : {lider['name']} ({lider['pts']} pts)")

    if no_push:
        print("\n[3/3] Modo --no-push: JSON generado localmente.")
        print(f"  Archivo: {os.path.abspath(out)}")
        return

    print("\n[3/3] Publicando en GitHub Pages...")
    try:
        git_push(data["last_updated"])
        print("  Listo! Panel disponible en:")
        print("  https://patyviena.github.io/prodetoros2026/")
    except RuntimeError as e:
        print(f"  ERROR al publicar:\n  {e}")
        print("  Podes publicar manualmente con: git push")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()

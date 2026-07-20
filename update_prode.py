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
from datetime import datetime, date
import urllib.request
import urllib.error

# --- Configuracion ---
SHEET_ID = "112gxMftT2pKnt3WPfbtrfhTaedodnmWZgOzEYdChYXg"
GID_DATA    = "587902986"   # Tab: DATA PARA TABLA
GID_CLASSIF = "2141517289"  # Tab: TABLA Clasificados

# Ultimo partido confirmado como jugado.
# Grupos=72, 16avos=88, Octavos=96, Cuartos=100, Semis=102, Final=104
# Actualizar cuando termine cada fase.
MATCHES_PLAYED_UP_TO = 72

# Fechas de 16avos y Octavos (YYYY-MM-DD). Corregir si hay error.
MATCH_DATES = {
    "P73": "2026-06-28",  # Sudafrica v Canada
    "P74": "2026-06-29",  # Alemania v Paraguay
    "P75": "2026-06-29",  # Paises Bajos v Marruecos
    "P76": "2026-06-29",  # Brasil v Japon
    "P77": "2026-06-30",  # Francia v Suecia
    "P78": "2026-06-30",  # Costa de Marfil v Noruega
    "P79": "2026-06-30",  # Mexico v Ecuador
    "P80": "2026-07-01",  # Inglaterra v RD Congo
    "P81": "2026-07-01",  # Estados Unidos v Bosnia
    "P82": "2026-07-01",  # Belgica v Senegal
    "P83": "2026-07-02",  # Portugal v Croacia
    "P84": "2026-07-02",  # Espana v Austria
    "P85": "2026-07-02",  # Suiza v Algeria
    "P86": "2026-07-03",  # Argentina v Cabo Verde
    "P87": "2026-07-03",  # Colombia v Ghana
    "P88": "2026-07-03",  # Australia v Egipto
    # Octavos de final
    "P89": "2026-07-03",  # Canada v Marruecos
    "P90": "2026-07-03",  # Paraguay v Francia
    "P91": "2026-07-05",  # Brasil v Noruega
    "P92": "2026-07-05",  # Mexico v Inglaterra
    "P93": "2026-07-06",  # Portugal v Espana
    "P94": "2026-07-06",  # Estados Unidos v Belgica
    "P95": "2026-07-07",  # Argentina v Egipto
    "P96": "2026-07-07",  # Suiza v Colombia
    # Cuartos de final
    "P97":  "2026-07-07",
    "P98":  "2026-07-07",
    "P99":  "2026-07-08",
    "P100": "2026-07-08",
    # Semifinales
    "P101": "2026-07-14",  # Francia v Espana
    "P102": "2026-07-15",  # Argentina v Inglaterra (habilitado al cargar todas las preds)
    # 3er Puesto y Final — habilitar cuando lleguen las predicciones
    "P103": "2026-07-19",  # 3er Puesto: Inglaterra v Francia — resultado: 6-4 Inglaterra
    "P104": "2026-07-19",  # Final: Argentina v Espana — hoy
}

BONUS_CATEGORIES = {
    "B1": {"label": "Campeon del Mundial",       "pts": 12},
    "B2": {"label": "Subcampeon",                "pts":  8},
    "B3": {"label": "Goleador del torneo",       "pts":  8},
    "B4": {"label": "Sel. mas goles a favor",    "pts":  5},
    "B6": {"label": "Sel. mas goles en contra",  "pts":  5},
}

# Resultados finales de bonus. B2 se deriva de B1 automaticamente (perdedor de Final).
# Usar nombres normalizados sin acento (comparacion es accent-insensitive).
# Ejemplo cuando se conozcan:  "B1": "Argentina",  "B3": "Mbappe",  "B4": "Espana"
BONUS_RESULTS: dict = {
    "B1": "España",    # Campeón
    # B2 = Argentina auto (subcampeón)
    "B3": "Mbappe",   # Goleador del torneo
    "B4": "Francia",  # Selección con más goles a favor
}

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


# Cuadro eliminatorio completo con placeholders
KNOCKOUT_BRACKET = [
    ("P73",  "16avos",     "1ro A vs 2do B"),
    ("P74",  "16avos",     "1ro B vs 2do A"),
    ("P75",  "16avos",     "1ro C vs 2do D"),
    ("P76",  "16avos",     "1ro D vs 2do C"),
    ("P77",  "16avos",     "1ro E vs 2do F"),
    ("P78",  "16avos",     "1ro F vs 2do E"),
    ("P79",  "16avos",     "1ro G vs 2do H"),
    ("P80",  "16avos",     "1ro H vs 2do G"),
    ("P81",  "16avos",     "1ro I vs 2do J"),
    ("P82",  "16avos",     "1ro J vs 2do I"),
    ("P83",  "16avos",     "1ro K vs 2do L"),
    ("P84",  "16avos",     "1ro L vs 2do K"),
    ("P85",  "16avos",     "3ros mejor (1) vs (2)"),
    ("P86",  "16avos",     "3ros mejor (3) vs (4)"),
    ("P87",  "16avos",     "3ros mejor (5) vs (6)"),
    ("P88",  "16avos",     "3ros mejor (7) vs (8)"),
    ("P89",  "Octavos",    "Gan. 16avos P1 vs P2"),
    ("P90",  "Octavos",    "Gan. 16avos P3 vs P4"),
    ("P91",  "Octavos",    "Gan. 16avos P5 vs P6"),
    ("P92",  "Octavos",    "Gan. 16avos P7 vs P8"),
    ("P93",  "Octavos",    "Gan. 16avos P9 vs P10"),
    ("P94",  "Octavos",    "Gan. 16avos P11 vs P12"),
    ("P95",  "Octavos",    "Gan. 16avos P13 vs P14"),
    ("P96",  "Octavos",    "Gan. 16avos P15 vs P16"),
    ("P97",  "Cuartos",    "Gan. Oct. P1 vs P2"),
    ("P98",  "Cuartos",    "Gan. Oct. P3 vs P4"),
    ("P99",  "Cuartos",    "Gan. Oct. P5 vs P6"),
    ("P100", "Cuartos",    "Gan. Oct. P7 vs P8"),
    ("P101", "Semis",      "Gan. Ctos. P1 vs P2"),
    ("P102", "Semis",      "Gan. Ctos. P3 vs P4"),
    ("P103", "3er Puesto", "Inglaterra v Francia"),
    ("P104", "Final",      "Argentina v España"),
]


def fetch_csv(gid: str) -> str:
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={gid}"
    with urllib.request.urlopen(url) as r:
        return r.read().decode("utf-8-sig")


def parse_classif(csv_text: str, players: list) -> dict:
    """Lee TABLA Clasificados y devuelve {match_id: {player: team_name_raw}}"""
    rows = list(csv.reader(io.StringIO(csv_text)))
    if not rows:
        return {}
    # Fila 0: N, Partido, Jugador1, Jugador2, ...
    header = rows[0]
    col_map = {cell.strip(): ci for ci, cell in enumerate(header) if cell.strip() in players}
    result = {}
    for row in rows[2:]:  # saltar fila 0 (headers) y fila 1 (sub-headers)
        if not row or not row[0].strip().startswith("P"):
            continue
        match_id = row[0].strip()
        for player, ci in col_map.items():
            val = row[ci].strip() if ci < len(row) else ""
            if val:
                result.setdefault(match_id, {})[player] = val
    return result


def parse_data(csv_text: str) -> dict:
    rows = list(csv.reader(io.StringIO(csv_text)))

    # Fila 0: N, Partido, Jugador1,,, Jugador2,,, ...
    # Fila 1: sub-headers (Pred.Local, Pred.Visitante, Puntos)
    # Filas 2+: datos de partidos
    # Ultima fila: "total puntaje"

    # Extraer nombres de jugadores (cada 3 columnas desde col 2)
    players = [rows[0][c].strip() for c in range(2, len(rows[0]), 3) if rows[0][c].strip()]

    matches_played = []
    group_total = 0      # total P1-P72 rows encontradas en el sheet
    group_preds  = []    # predicciones por partido para la matriz
    history = {p: [0] for p in players}
    knockout_data = {}   # match_id -> {match_name, player_data, played, has_preds}

    for row in rows[2:]:
        if not row or not row[0].strip() or not row[0].strip().startswith("P"):
            continue
        match_id   = row[0].strip()
        match_name = row[1].strip() if len(row) > 1 else ""
        if not match_name:
            continue

        player_data = {}
        for i, player in enumerate(players):
            base = 2 + i * 3
            pred_l = row[base    ].strip() if base     < len(row) else ""
            pred_v = row[base + 1].strip() if base + 1 < len(row) else ""
            pts_s  = row[base + 2].strip() if base + 2 < len(row) else "0"
            player_data[player] = {
                "pred": f"{pred_l}-{pred_v}" if pred_l and pred_v else None,
                "pts":  int(pts_s) if pts_s.lstrip("-").isdigit() else 0,
            }

        total_pts = sum(d["pts"] for d in player_data.values())
        has_preds = any(d["pred"] for d in player_data.values())
        num = match_id[1:]
        match_num = int(num) if num.isdigit() else 999

        if match_num <= 72:
            group_total += 1
            # Partido jugado si tiene puntos, O si la fase esta confirmada como completa
            if total_pts > 0 or (has_preds and match_num <= MATCHES_PLAYED_UP_TO):
                matches_played.append(match_name)
                for p in players:
                    history[p].append(history[p][-1] + player_data[p]["pts"])
                group_preds.append({
                    "id":          match_id,
                    "match":       match_name,
                    "predictions": {p: player_data[p]["pred"] for p in players},
                    "pts":         {p: player_data[p]["pts"]  for p in players},
                })
        else:
            # Eliminatorias
            knockout_data[match_id] = {
                "match_name": match_name,
                "player_data": player_data,
                "played": total_pts > 0,
                "has_preds": has_preds,
            }

    # Sumar puntos de eliminatorias jugadas al historial y ranking
    for match_id, phase, placeholder_name in KNOCKOUT_BRACKET:
        kd = knockout_data.get(match_id)
        if not kd or not kd["played"]:
            continue
        raw_name = kd["match_name"]
        mn = raw_name if (" vs " in raw_name.lower() or " v " in raw_name) else placeholder_name
        matches_played.append(mn)
        for p in players:
            history[p].append(history[p][-1] + kd["player_data"][p]["pts"])

    # Construir cuadro eliminatorio: bracket fijo + datos reales del sheet
    knockout_matches = []
    for match_id, phase, placeholder_name in KNOCKOUT_BRACKET:
        actual = knockout_data.get(match_id)
        using_real_name = False
        # Partidos jugados con 0 pts para todos (nadie acertó el ganador)
        PLAYED_OVERRIDES = {"P103"}
        if actual:
            raw_name = actual["match_name"]
            _placeholder_keywords = ("perdedor", "gan.", "ganador", "3ros", "1ro ", "2do ")
            _is_placeholder = any(k in raw_name.lower() for k in _placeholder_keywords)
            if (not _is_placeholder) and (" vs " in raw_name.lower() or " v " in raw_name):
                match_name = raw_name
                using_real_name = True
            else:
                match_name = placeholder_name   # nombre del sheet es solo label de fase
            player_data = actual["player_data"]
            played      = actual["played"] or match_id in PLAYED_OVERRIDES
            has_preds   = actual["has_preds"]
        else:
            match_name  = placeholder_name
            player_data = {p: {"pred": None, "pts": 0} for p in players}
            played      = False
            has_preds   = False

        is_tbd     = not using_real_name and not has_preds
        match_date = MATCH_DATES.get(match_id, "")
        today_str  = date.today().isoformat()
        show_preds = played or bool(match_date and match_date <= today_str)

        knockout_matches.append({
            "id":          match_id,
            "phase":       phase,
            "match":       match_name,
            "match_date":  match_date,
            "is_tbd":      is_tbd,
            "has_preds":   has_preds,
            "played":      played,
            "show_preds":  show_preds,
            "predictions": {p: player_data[p]["pred"] for p in players},
            "points":      {p: player_data[p]["pts"]  for p in players},
        })

    # Ranking final
    final_pts      = {p: history[p][-1] for p in players}
    sorted_players = sorted(players, key=lambda p: -final_pts[p])
    ranking = [{"pos": i + 1, "name": p, "pts": final_pts[p]} for i, p in enumerate(sorted_players)]
    top3    = {r["name"]: r["pos"] for r in ranking if r["pos"] <= 3}

    # Parsear filas bonus (B1, B2, ...)
    bonus_preds = []
    for row in rows[2:]:
        if not row or not row[0].strip():
            continue
        bid = row[0].strip()
        if not (bid.startswith("B") and bid[1:].isdigit()):
            continue
        cat = BONUS_CATEGORIES.get(bid)
        if not cat:
            continue
        preds, earned = {}, {}
        for i, player in enumerate(players):
            base = 2 + i * 3
            vals = [row[base + j].strip() if base + j < len(row) else "" for j in range(3)]
            pred_text = next((v for v in vals if v and not v.lstrip("-").isdigit()), "")
            pts_val   = next((int(v) for v in vals if v and v.lstrip("-").isdigit()), 0)
            preds[player]  = pred_text
            earned[player] = pts_val
        bonus_preds.append({
            "id":          bid,
            "label":       cat["label"],
            "pts_value":   cat["pts"],
            "predictions": preds,
            "earned":      earned,
        })

    # Aplicar BONUS_RESULTS — sobreescribe 'earned' segun resultado real conocido
    if BONUS_RESULTS:
        import unicodedata as _ud
        def _norm_bonus(s):
            return _ud.normalize("NFKD", str(s)).encode("ascii", "ignore").decode("ascii").strip().lower()

        b1_winner = BONUS_RESULTS.get("B1", "")
        b2_winner = ""
        if b1_winner:
            normed = _norm_bonus(b1_winner)
            b2_winner = "espana" if normed == "argentina" else "argentina"

        for b in bonus_preds:
            bid = b["id"]
            if bid == "B2":
                result_norm = b2_winner
            else:
                result_norm = _norm_bonus(BONUS_RESULTS.get(bid, ""))
            if not result_norm:
                continue
            for player in players:
                pred_norm = _norm_bonus(b["predictions"].get(player, ""))
                if pred_norm == result_norm:
                    b["earned"][player] = b["pts_value"]

    # Recomputar ranking incluyendo bonus ganados
    bonus_earned = {p: sum(b["earned"].get(p, 0) for b in bonus_preds) for p in players}
    total_with_bonus = {p: final_pts[p] + bonus_earned[p] for p in players}
    if any(v > 0 for v in bonus_earned.values()):
        sorted_players = sorted(players, key=lambda p: -total_with_bonus[p])
        ranking = [{"pos": i + 1, "name": p, "pts": total_with_bonus[p],
                    "base_pts": final_pts[p], "bonus_pts": bonus_earned[p]}
                   for i, p in enumerate(sorted_players)]
        top3 = {r["name"]: r["pos"] for r in ranking if r["pos"] <= 3}
    else:
        ranking = [dict(r, base_pts=r["pts"], bonus_pts=0) for r in ranking]

    # Ko_preds: partidos eliminatorios jugados, formato equivalente a group_preds
    ko_preds = [
        {
            "id":          m["id"],
            "match":       m["match"],
            "phase":       m["phase"],
            "pts":         m["points"],
            "predictions": m["predictions"],
            "classif":     m.get("classif"),
        }
        for m in knockout_matches
        if m["played"]
    ]

    return {
        "last_updated":     datetime.now().strftime("%d/%m/%Y %H:%M"),
        "players":          players,
        "group_total":      group_total,
        "matches_played":   matches_played,
        "group_preds":      group_preds,
        "history":          history,
        "ranking":          ranking,
        "top3":             top3,
        "knockout_matches": knockout_matches,
        "ko_preds":         ko_preds,
        "colors":           COLOR_PALETTE,
        "bonus_preds":      bonus_preds,
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

    print("      Leyendo clasificados...")
    try:
        classif_csv = fetch_csv(GID_CLASSIF)
        classif_data = parse_classif(classif_csv, data["players"])
        for m in data["knockout_matches"]:
            m["classif"] = classif_data.get(m["id"], {})
        cls_matches = sum(1 for m in data["knockout_matches"] if m["classif"])
        print(f"      Clasificados: {cls_matches} partidos con datos")
    except Exception as e:
        print(f"      Aviso: no se pudo leer clasificados ({e})")
        for m in data["knockout_matches"]:
            m["classif"] = {}

    os.makedirs("docs", exist_ok=True)
    out = os.path.join("docs", "data.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    lider = data["ranking"][0]
    print(f"\n  Partidos de grupos jugados : {len(data['matches_played'])}")
    print(f"  Lider                      : {lider['name']} ({lider['pts']} pts)")

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

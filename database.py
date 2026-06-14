import os
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

DB_PATH = "data.db"

# Supabase configuration (optional)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
_SUPABASE_AVAILABLE = False
_sb_client = None
if SUPABASE_URL and SUPABASE_KEY:
    try:
        from supabase import create_client

        _sb_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        _SUPABASE_AVAILABLE = True
    except Exception:
        _SUPABASE_AVAILABLE = False


def _get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            horas_trabalhadas REAL NOT NULL,
            status_calculado TEXT NOT NULL,
            mensagem_suporte TEXT,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def salvar_registro(horas_trabalhadas: float, status_calculado: str, mensagem_suporte: Optional[str]):
    created_at = datetime.utcnow().isoformat()
    if _SUPABASE_AVAILABLE and _sb_client is not None:
        try:
            payload = {
                "horas_trabalhadas": horas_trabalhadas,
                "status_calculado": status_calculado,
                "mensagem_suporte": mensagem_suporte or "",
                "created_at": created_at,
            }
            resp = _sb_client.table("registros").insert(payload).execute()
            return resp
        except Exception as e:
            # Fallback para SQLite em caso de falha
            pass

    # Fallback local
    init_db()
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO registros (horas_trabalhadas, status_calculado, mensagem_suporte, created_at) VALUES (?, ?, ?, ?)",
        (horas_trabalhadas, status_calculado, mensagem_suporte or "", created_at),
    )
    conn.commit()
    conn.close()


def ler_historico(limit: int = 100) -> List[Dict]:
    if _SUPABASE_AVAILABLE and _sb_client is not None:
        try:
            resp = _sb_client.table("registros").select("*").order("id", desc=True).limit(limit).execute()
            data = resp.data if hasattr(resp, "data") else resp
            # normaliza resultados
            results = []
            for r in data:
                results.append({
                    "id": r.get("id"),
                    "horas_trabalhadas": r.get("horas_trabalhadas"),
                    "status_calculado": r.get("status_calculado"),
                    "mensagem_suporte": r.get("mensagem_suporte"),
                    "created_at": r.get("created_at"),
                })
            return results
        except Exception:
            # fallback para sqlite
            pass

    init_db()
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, horas_trabalhadas, status_calculado, mensagem_suporte, created_at FROM registros ORDER BY id DESC LIMIT ?",
        (limit,),
    )
    rows = cur.fetchall()
    conn.close()
    results = []
    for r in rows:
        results.append(
            {
                "id": r["id"],
                "horas_trabalhadas": r["horas_trabalhadas"],
                "status_calculado": r["status_calculado"],
                "mensagem_suporte": r["mensagem_suporte"],
                "created_at": r["created_at"],
            }
        )
    return results

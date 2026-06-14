import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

DB_PATH = "data.db"

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
    init_db()
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO registros (horas_trabalhadas, status_calculado, mensagem_suporte, created_at) VALUES (?, ?, ?, ?)",
        (horas_trabalhadas, status_calculado, mensagem_suporte or "", datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

def ler_historico(limit: int = 100) -> List[Dict]:
    init_db()
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, horas_trabalhadas, status_calculado, mensagem_suporte, created_at FROM registros ORDER BY id DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()
    results = []
    for r in rows:
        results.append({
            "id": r["id"],
            "horas_trabalhadas": r["horas_trabalhadas"],
            "status_calculado": r["status_calculado"],
            "mensagem_suporte": r["mensagem_suporte"],
            "created_at": r["created_at"],
        })
    return results

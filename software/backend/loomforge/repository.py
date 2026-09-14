from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .models import JobRecord


class JobRepository:
    def __init__(self, path: str | Path):
        self.path = str(path)
        self._init()

    def _init(self) -> None:
        connection = sqlite3.connect(self.path)
        try:
            connection.execute("CREATE TABLE IF NOT EXISTS jobs (job_id TEXT PRIMARY KEY, disposition TEXT NOT NULL, payload TEXT NOT NULL)")
            connection.commit()
        finally:
            connection.close()

    def save(self, record: JobRecord) -> None:
        connection = sqlite3.connect(self.path)
        try:
            connection.execute("INSERT OR REPLACE INTO jobs(job_id, disposition, payload) VALUES(?,?,?)", (record.job_id, record.disposition, json.dumps(record.jsonable())))
            connection.commit()
        finally:
            connection.close()

    def get(self, job_id: str) -> dict | None:
        connection = sqlite3.connect(self.path)
        try:
            row = connection.execute("SELECT payload FROM jobs WHERE job_id=?", (job_id,)).fetchone()
        finally:
            connection.close()
        return json.loads(row[0]) if row else None

    def list(self) -> list[dict]:
        connection = sqlite3.connect(self.path)
        try:
            rows = connection.execute("SELECT payload FROM jobs ORDER BY rowid DESC").fetchall()
        finally:
            connection.close()
        return [json.loads(row[0]) for row in rows]

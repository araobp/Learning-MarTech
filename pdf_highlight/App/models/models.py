import os
import sqlite3

cwd = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(cwd, "../../database/search.db")

def get_sources():
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    sources = cur.execute('SELECT * FROM sources').fetchall()
  return sources

if __name__ == '__main__':
  print(get_sources())
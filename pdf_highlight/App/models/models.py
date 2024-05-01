import os
import sqlite3

cwd = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(cwd, "../../database/search.db")

def select_sources():
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    sources = cur.execute('SELECT * FROM sources').fetchall()
  return sources

def select_texts(base_url, keywords):
  keywords_ = [f'texts.text LIKE "%{e.strip()}%"' for e in keywords.split(',')]
  conditions = ' OR '.join(keywords_)
  
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    texts = cur.execute(f'SELECT texts.link_id, texts.page, texts.text FROM texts INNER JOIN links ON texts.link_id = links.id WHERE links.base_url="{base_url}" AND ({conditions})').fetchall()
  return texts

if __name__ == '__main__':
  print(select_texts("https://www.meti.go.jp", "ニュージーランド,アメリカ"))
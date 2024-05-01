import os
import sqlite3
import re
from urllib.parse import urljoin
import requests
import fitz
import io

cwd = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(cwd, "../../database/search.db")

def to_dict_list(list_, columns):
  dict_list = []
  for e in list_:
    d = {}
    i = 0
    for c in columns:
      d[c] = e[i]
      i += 1
    dict_list.append(d)
  return dict_list

def select_sources():
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    sources = cur.execute('SELECT base_url, org, doc FROM sources').fetchall()
  return to_dict_list(sources, columns=['base_url', 'org', 'doc'])

def select_texts(base_url, keywords):
  keywords = [e.strip() for e in keywords.split(',')]
  
  pattern = '|'.join(keywords)
  
  keywords_ = [f'texts.text LIKE "%{e}%"' for e in keywords]
  conditions = ' OR '.join(keywords_)
  
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    texts = cur.execute(f'SELECT texts.link_id, links.title, texts.page, texts.text FROM texts INNER JOIN links ON texts.link_id = links.id WHERE links.base_url="{base_url}" AND ({conditions})').fetchall()
  
  texts_ = []
  for text in texts:
    #link_id = text[0]
    #title = text[1]
    #page = text[2]
    original_text = text[3]
    
    spans = {}
    for m in re.finditer(pattern, original_text):
      keyword = m.group(0)
      if keyword not in spans:
        spans[keyword] = []
      spans[keyword].append([m.start(), m.end()])
    text_ = list(text)
    text_.append(spans)
    texts_.append(text_)
  return to_dict_list(texts_, columns=['link_id', 'title', 'page', 'text', 'spans'])

def pdf_highlight(link_id, page, keywords, all_pages):
  keywords = [e.strip() for e in keywords.split(',')]
  
  with sqlite3.connect(DB_PATH) as conn:
    cur = conn.cursor()
    base_url, path, title = cur.execute(f'SELECT base_url, path, title FROM links WHERE id={link_id}').fetchone()
    
  url = urljoin(base_url, path)
  print(url)
  resp = requests.get(url)
  doc = fitz.open(stream=resp.content)
  
  pdf = None
  
  if all_pages == 'true':
    for page in doc:
      for keyword in keywords:
        rects = page.search_for(keyword)
      page.add_highlight_annot(rects)
      
    pdf = io.BytesIO(doc.tobytes())
  
  else:
    from_page = page - 1 if page > 0 else page
    to_page = page + 1 if page < len(doc) else page
    pages = doc[from_page:to_page+1]

    for page in pages:
      for keyword in keywords:
        rects = page.search_for(keyword)
      page.add_highlight_annot(rects)
    
    doc2 = fitz.open()
    doc2.insert_pdf(doc, from_page=from_page, to_page=to_page, start_at = 0)
    
    pdf = io.BytesIO(doc2.tobytes())
  
  return (title, pdf)

if __name__ == '__main__':
  print(select_texts("https://www.meti.go.jp", "ニュージーランド,オーストラリア"))
  
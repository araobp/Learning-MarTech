# Date: 2024/04/28
# PDFテキストハイライト実験
from flask import Flask, send_file
import fitz
import requests
import io

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"
  
@app.route("/highlight_test/<string:keyword>")
def highlight_test(keyword):
  resp = requests.get('https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r05/pdf/n4700000.pdf')
  doc = fitz.open(stream=resp.content)
  for page in doc:
    rects = page.search_for(keyword)
    page.add_highlight_annot(rects)
  
  pdf_doc = doc.tobytes()
  
  return send_file(
    io.BytesIO(pdf_doc),
    mimetype='application/pdf',
    as_attachment=False,
    download_name='test.pdf')

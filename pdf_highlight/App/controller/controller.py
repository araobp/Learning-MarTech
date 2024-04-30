import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Blueprint, render_template, jsonify, request
from models import models

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sources')
def sources():
  sources = models.get_sources()
  return jsonify(sources)

@main.route('/search')
def search():
  base_url = request.args.get('base_url', default = None, type = str)
  keywords = request.args.get('keywords', default = None, type=str)
  keywords_ = [e.strip() for e in keywords.split(',')]
  return jsonify(keywords_)

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Blueprint, render_template, jsonify
from models import models

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sources')
def sources():
  sources = models.get_sources()
  return jsonify(sources)
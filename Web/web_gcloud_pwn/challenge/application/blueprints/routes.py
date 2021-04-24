from flask import Blueprint, request, render_template, abort
from application.util import gen_pdf

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@api.route('/cache', methods=['POST'])
def cache():
    if not request.is_json or 'url' not in request.json:
        return abort(400)
    
    return gen_pdf(request.json['url'])
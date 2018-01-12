from flask import Blueprint, jsonify, send_file
from inflection import singularize
from app import redis
import os
import pickle

blueprint = Blueprint('metadata_api', __name__, url_prefix='/metadata')


@blueprint.route('/<string:data>/<string:id>')
@blueprint.route('/<string:data>')
def api(data, id=None):
    data = singularize(data)

    if id:
        data = data + '/' + id

    large_attrs = ['sc_school']

    if data in large_attrs:
        return send_file(open(os.getcwd() + '/app/apis/large_attrs/' + data + '.json'),
                        attachment_filename=(data + '.json'),
                        mimetype='application/json')

    return jsonify(pickle.loads(redis.get(data)))

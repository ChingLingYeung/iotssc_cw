from flask import Flask, make_response, jsonify
from db_utils import update_db, get_entire_table, get_latest_row, get_json_table, get_json_row
from threading import Thread

webapp = Flask(__name__)


@webapp.route("/", methods=["GET"])
def root():
	return "Landing page"

@webapp.route('/history', methods=["GET"])
def history():
    table = get_entire_table()
#    json_table = jsonify(table)
    json_table = jsonify(get_json_table(table))
    resp = make_response(json_table, 200)
    return resp


@webapp.route("/latest_data", methods=["GET"])
def latest_data():
    row = get_latest_row()
    #json_row = jsonify(row)
    json_row = jsonify(get_json_row(row))
    resp = make_response(json_row, 200)
    return resp


if __name__ == "__main__":
    t = Thread(target=update_db)
    t.start()
    webapp.run('0.0.0.0', port=2333)

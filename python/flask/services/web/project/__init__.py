from ddtrace import patch_all
patch_all(logging=True)

from flask import abort, Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy

# import logging
# FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
#           '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
#           '- %(message)s')
# logging.basicConfig(format=FORMAT)
# log = logging.getLogger(__name__)
# log.level = logging.INFO


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

@app.errorhandler(404)
def resource_not_found(e):
    app.logger.error('Processing error request')
    return jsonify(error=str(e)), 404

@app.route('/api/post/<int:post_id>')
def api(post_id):
    app.logger.info("Processing /api/post/%s" % post_id)
    return 'Hello %s' % post_id

@app.route('/')
def hello_world():
    app.logger.info("Procesing index hello_world request GET /")
    return jsonify(hello="world")

@app.route('/error')
def error():
    app.logger.error("GET 404 Error")
    abort(404, description="Resource not found")

@app.route("/static/<path:filename>")
def staticfiles(filename):
    app.logger.info("GET /static/%s" % filename)
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

if __name__ == '__main__':
  print('Starting hello-world server...')

  app.run(host='0.0.0.0')

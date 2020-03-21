import os
from os import path

from flask import Flask
from flask import jsonify, make_response

from data import db_session
from data.db_session import create_session
from data.models.jobs import Jobs

app = Flask(__name__)

db_session.global_init(path.join(path.dirname(__file__), './db/mars_explorer.db'))


@app.route('/api/jobs')
def find_jobs():
    db = create_session()
    jobs = db.query(Jobs).all()
    return jsonify({
        'jobs': [
            job.to_dict(rules=('-user.jobs', '-user.news', '-user.hashed_password'))
            for job in jobs
        ]
    })


@app.route('/api/jobs/<int:id>')
def find_job(id):
    db = create_session()
    job = db.query(Jobs).get(id)
    if job:
        return jsonify(job.to_dict(
            rules=('-user.jobs', '-user.news', '-user.hashed_password')
        ))
    else:
        return make_response(jsonify({'error': 'NOT FOUND'}), 404)


def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

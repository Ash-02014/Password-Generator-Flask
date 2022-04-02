from flask import Flask, jsonify, request
from db import DB
from utils import Utilities
from datetime import datetime

app = Flask(__name__)
db = DB()
utils = Utilities(db.check_db, db.store)

@app.post('/')
def pwd_generator():
    data = request.get_json()
    if not data or 'length' not in data: pwd_length = 16 
    else: pwd_length = data['length']
    passw = utils.generate_pass(pwd_length)
    pwds = db.read_data()
    return jsonify({
        'status_code': 200,
        'password': {
            'length': pwd_length,
            'unique': True,
            'created_at': datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
            "password_id": len(pwds),
            "password": passw
        }
    })

app.run()
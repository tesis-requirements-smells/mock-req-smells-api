import numpy as np
from flask import Flask
from flask import jsonify
from datetime import datetime

app = Flask(__name__)

BASE_URL = 'reqsmells'
PORT = 8080

reports_resume = [
    {
        'report_id': 1,
        'report_name': 'Evaluación de ejemplo # 1',
        'report_date': datetime(2024, 4, 10),
        'report_overall_score': 75.12,
        'report_requirements': [ 
            { 'req_id': 1, 'req_code': 'HU001', 'req_name': 'Inicio de sesión' },
            { 'req_id': 2, 'req_code': 'HU002', 'req_name': 'Cerrar sesión' },
            { 'req_id': 3, 'req_code': 'HU003', 'req_name': 'registro' }
        ]
    },
    {
        'report_id': 2,
        'report_name': 'Evaluación de ejemplo # 2',
        'report_date': datetime(2024, 4, 11),
        'report_overall_score': 70.12,
        'report_requirements': [ 
            { 'req_id': 1, 'req_code': 'HU001', 'req_name': 'Inicio de sesión' }
        ]
    },
    {
        'report_id': 3,
        'report_name': 'Evaluación de ejemplo # 3',
        'report_date': datetime(2024, 4, 11),
        'report_overall_score': 10.12,
        'report_requirements': [ 
            { 'req_id': 1, 'req_code': 'HU001', 'req_name': 'Inicio de sesión' },
            { 'req_id': 2, 'req_code': 'HU002', 'req_name': 'Cerrar sesión' },
            { 'req_id': 3, 'req_code': 'HU003', 'req_name': 'registro' },
            { 'req_id': 4, 'req_code': 'HU004', 'req_name': 'Mostrar productos' },
            { 'req_id': 5, 'req_code': 'HU005', 'req_name': 'Eliminar producto' }
        ]
    },
    {
        'report_id': 4,
        'report_name': 'Evaluación de ejemplo # 4',
        'report_date': datetime(2024, 4, 12),
        'report_overall_score': 20.12,
        'report_requirements': [ 
            { 'req_id': 1, 'req_code': 'HU001', 'req_name': 'Inicio de sesión' },
            { 'req_id': 2, 'req_code': 'HU002', 'req_name': 'Cerrar sesión' },
            { 'req_id': 3, 'req_code': 'HU003', 'req_name': 'registro' }
        ]
    },
    {
        'report_id': 5,
        'report_name': 'Evaluación de ejemplo # 5',
        'report_date': datetime(2024, 4, 10),
        'report_overall_score': 40.12,
        'report_requirements': [ 
            { 'req_id': 1, 'req_code': 'HU001', 'req_name': 'Inicio de sesión' },
            { 'req_id': 2, 'req_code': 'HU002', 'req_name': 'Cerrar sesión' },
            { 'req_id': 3, 'req_code': 'HU003', 'req_name': 'registro' }
        ]
    }
]

# Listado de reportes
@app.route(f'/{BASE_URL}/get-reports-resume', methods=['GET'])
def predict():    
    return jsonify({'reports' : reports_resume})


if __name__ == "__main__":
    app.run(port=PORT)
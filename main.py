from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

BASE_URL = 'reqsmells'
PORT = 8080

# json files
reports_resume_url = './data/reports-resume.json'


# Listado de reportes
@app.route(f'/{BASE_URL}/get-reports-resume', methods=['GET'])
def get_reports_resume(): 
    reports_resume = read_json('./data/reports-resume.json')       
    return jsonify({'reports' : reports_resume})


# Eliminar reporte
@app.route(f'/{BASE_URL}/delete-report/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):    
    reports_resume = read_json(reports_resume_url)
    previous_len = len(reports_resume)

    # delete 
    reports_resume = [d for d in reports_resume if d['report_id'] != report_id]
    write_json(reports_resume_url, reports_resume)

    # prepare response
    report_found = len(reports_resume) < previous_len
    response_message = 'Registro eliminado exitosamente' if report_found else 'No se pudo encontrar reporte para eliminar'
    status = 200 if report_found else 404    

    return jsonify({'message' : response_message}), status


def read_json(url: str):
    with open(url, 'r', encoding='utf-8') as data_file:
        return json.load(data_file)
    

def write_json(url: str, data:list):
    with open(url, 'w', encoding='utf-8') as data_file:
        json.dump(data, data_file, indent=4)


if __name__ == "__main__":
    app.run(port=PORT)
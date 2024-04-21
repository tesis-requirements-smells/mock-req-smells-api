from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

BASE_URL = 'reqsmells'
PORT = 8080

# Campos del reporte que deberian salir en el resumen
RESUME_FIELDS = ['report_id', 'report_name', 'report_date', 'report_overall_score']

# json files
REPORTS_URL = './data/reports.json'


# Listado de reportes resumido, sin paginación
@app.route(f'/{BASE_URL}/get-reports-resume', methods=['GET'])
def get_reports_resume(): 
    reports_resume = read_json(REPORTS_URL)

    # Devolver solo los campos de resumen
    reports_resume = [{field: d[field] for field in RESUME_FIELDS} for d in reports_resume]

    return jsonify({
        'reports' : reports_resume
    })


# Listado de reportes resumido, paginado
@app.route(f'/{BASE_URL}/get-reports-resume/<int:page>/<int:page_size>', methods=['GET'])
def get_paged_reports_resume(page: int, page_size:int): 
    reports_resume = read_json(REPORTS_URL)

    # Devolver solo los campos de resumen
    reports_resume = [{field: d[field] for field in RESUME_FIELDS} for d in reports_resume]
    paged_list, pages_count = paginate_list(reports_resume, page, page_size)

    return jsonify({
        'reports' : paged_list,
        'page': page,
        'pages_count': pages_count
    })


# Obtener detalle de un reporte
@app.route(f'/{BASE_URL}/get-report/<int:report_id>', methods=['GET'])
def get_get_report_by_id(report_id:int): 
    reports = read_json(REPORTS_URL)

    # search
    reports = [d for d in reports if d['report_id'] == report_id]
    report = reports[0] if reports != None and len(reports) > 0 else None

    # prepare response    
    error_message = 'No se pudo encontrar el reporte'
    status = 200 if report != None else 404
    response = {'report': report} if report != None else {'message': error_message}

    return jsonify(response), status


# Eliminar reporte
@app.route(f'/{BASE_URL}/delete-report/<int:report_id>', methods=['DELETE'])
def delete_report(report_id:int):    
    reports_resume = read_json(REPORTS_URL)
    previous_len = len(reports_resume)

    # delete 
    reports_resume = [d for d in reports_resume if d['report_id'] != report_id]
    write_json(REPORTS_URL, reports_resume)

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


def paginate_list(lista, page_number, page_size):
    """
    Function to paginate a list.

    Args:
    - lista: The list to paginate.
    - page_number: The desired page number (starting from 1).
    - page_size: The size of the page.

    Returns:
    - A tuple containing the current page and the total pages.
    """

    # Calculate the start and end index for the current page
    start = (page_number - 1) * page_size
    end = start + page_size

    # Get the current page from the list
    current_page = lista[start:end]

    # Calculate the total pages
    total_pages = len(lista) // page_size
    if len(lista) % page_size != 0:
        total_pages += 1

    return current_page, total_pages



if __name__ == "__main__":
    app.run(port=PORT)
import json

from bottle import get, run, post, request, Response
from pony.orm import db_session

from loans_api.models import db, Product


@db_session
def create_new_loan(loan_id: str, name: str) -> None:
    Product(uid=loan_id, name=name)


@db_session
def get_loan_data(loan_id: str) -> dict:
    p = Product[loan_id]

    data = {
        'loan_id': p.uid,
        'name': p.name
    }

    return data


@post('/loans/')
def loan_create_view():
    data = request.json
    create_new_loan(**data)

    return Response(status=201)


@get('/loans/<loan_id>/')
def loan_detail_view(loan_id):
    loan_data = get_loan_data(loan_id)
    json_data = json.dumps(loan_data)

    return Response(body=json_data)


def run_server():
    db.bind(provider='sqlite', filename=':memory:')
    db.generate_mapping(create_tables=True)

    run(host='localhost', port=8080)


if __name__ == '__main__':
    run_server()

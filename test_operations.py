import pytest
import json

def test_get_last_operations():
    with open('operations.json', 'r') as f:
        operations = json.load(f)
    assert len(get_last_operations('operations.json')) == 5

def test_format_operation():
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    formatted_operation = format_operation(operation)
    assert formatted_operation.startswith("26.08.2019 Перевод организации")

def test_print_operations(capsys):
    print_operations('operations.json')
    captured = capsys.readouterr()
    assert len(captured.out.split('\n\n')) == 5
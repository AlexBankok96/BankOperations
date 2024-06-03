import operations

def test_mask_card_number():
    assert operations.mask_card_number('1234567890123456') == '1234 XX** **** 3456'

def test_mask_account_number():
    assert operations.mask_account_number('1234567890') == '**7890'

def test_print_operation(capsys):
    operation = {
        "date": "2024-06-01T09:12:34.567890",
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Test operation",
        "from": "1234567890123456",
        "to": "1234567890"
    }
    operations.print_operation(operation)
    captured = capsys.readouterr()
    assert "Date: " in captured.out

def test_print_executed_operations(capsys):
    operations_data = [
        {
            "state": "EXECUTED",
            "date": "2024-06-01T09:12:34.567890",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Test operation",
            "from": "1234567890123456",
            "to": "1234567890"
        },
        {
            "state": "CANCELED",
            "date": "2024-06-01T09:12:34.567890",
            "operationAmount": {
                "amount": "50.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Another test operation",
            "from": "6543210987654321",
            "to": "0987654321"
        }
    ]
    operations.print_executed_operations(operations_data)
    captured = capsys.readouterr()
    assert "Date: " in captured.out

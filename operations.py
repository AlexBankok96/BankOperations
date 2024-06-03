import json

def load_operations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def mask_card_number(card_number):
    masked_number = card_number[:4] + ' XX** **** ' + card_number[-4:]
    return masked_number

def mask_account_number(account_number):
    masked_number = '**' + account_number[-4:]
    return masked_number

def print_operation(operation):
    date = operation['date'].split('T')[0].replace('-', '.')
    from_info = mask_card_number(operation.get('from', ''))
    to_info = mask_account_number(operation.get('to', ''))
    print(f"Date: {date}")
    print(f"Operation Amount: {operation['operationAmount']['amount']} {operation['operationAmount']['currency']['code']}")
    print(f"Description: {operation['description']}")
    print(f"From: {from_info}")
    print(f"To: {to_info}")

def print_executed_operations(operations_data):
    executed_operations = [operation for operation in operations_data if operation.get('state') == 'EXECUTED']
    last_executed_operations = list(reversed(executed_operations))[:5]
    for operation in last_executed_operations:
        print_operation(operation)
        print()

if __name__ == "__main__":
    operations_data = load_operations('operations.json')
    print_executed_operations(operations_data)
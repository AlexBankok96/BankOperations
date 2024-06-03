import json

def get_last_operations(file_name):
    with open(file_name, 'r') as f:
        operations = json.load(f)
    executed_operations = [op for op in operations if op['state'] == 'EXECUTED']
    executed_operations.sort(key=lambda x: x['date'], reverse=True)
    return executed_operations[:5]

def format_operation(operation):
    date = operation['date'][:10].replace('-', '.')
    description = operation['description']
    from_account = operation['from']
    to_account = operation['to']
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    if ' ' in from_account:
        from_account = ' '.join([from_account[:6] + '****' + from_account[-4:]])
    else:
        from_account = '**' + from_account[-4:]

    if ' ' in to_account:
        to_account = ' '.join([to_account[:6] + '****' + to_account[-4:]])
    else:
        to_account = '**' + to_account[-4:]

    return f"{date} {description}\n{from_account} -> {to_account}\n{amount} {currency}"

def print_operations(file_name):
    operations = get_last_operations(file_name)
    for operation in operations:
        print(format_operation(operation))
        print()

if __name__ == "__main__":
    file_name = 'operations.json'
    print_operations(file_name)
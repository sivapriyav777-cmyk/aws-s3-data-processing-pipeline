def validate_customer(customer):
    if not customer["customer_id"]:
        return False

    if not customer["name"].strip():
        return False

    if "@" not in customer["email"]:
        return False

    return True


def validate_records(records):
    valid_records = []
    invalid_records = []

    for record in records:
        if validate_customer(record):
            valid_records.append(record)
        else:
            invalid_records.append(record)

    return valid_records, invalid_records

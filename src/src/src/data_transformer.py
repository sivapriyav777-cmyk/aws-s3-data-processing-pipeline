def transform_records(records):
    transformed = []

    for record in records:
        transformed.append({
            "customer_id": int(record["customer_id"]),
            "name": record["name"].strip().title(),
            "email": record["email"].strip().lower(),
            "city": record["city"].strip().title()
        })

    return transformed

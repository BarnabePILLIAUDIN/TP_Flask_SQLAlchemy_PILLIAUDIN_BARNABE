def get_missing_field(data, fields):
    missing_fields = []
    for field in fields:
        if not data[field]:
            missing_fields.append(field)
    return ', '.join(missing_fields)
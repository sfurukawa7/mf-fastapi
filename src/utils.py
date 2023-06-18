def row_to_dict(row) -> dict:
    return {column: getattr(row, column) for column in row.__table__.columns.keys()}

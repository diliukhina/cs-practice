def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts)!=3:
        raise ValueError("Неверное количество полей")
    city, temp, date = parts
    temp=float(temp)
    return {"city": city, "temp": temp, "date": date }

def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            records.append(parse_record(line))
        except ValueError:
            continue

    return records

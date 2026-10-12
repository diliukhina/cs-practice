
def parse_record(line: str) -> dict:
    """Проверяет строку и преобразует её в словарь."""
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Неверное количество полей")

    city, temp, date = parts

    city = city.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("Пустой город или дата")

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {"city": city, "temperature": temp, "date": date}


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


def average_by_city(records: list[dict]) -> dict:
    """Вычисляет среднюю температуру для каждого города."""
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0) + record["temperature"]
        counts[city] = counts.get(city, 0) + 1

    averages = {}

    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        return ""

    return sorted(
        averages,
        key=lambda city: (-averages[city], city)
    )[0]

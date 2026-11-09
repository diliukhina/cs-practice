import json


def csv_to_records(text: str) -> list[dict]:
    lines = []

    for line in text.splitlines():
        if line.strip():
            lines.append(line)

    if not lines:
        return []

    headers = [name.strip() for name in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        values = [value.strip() for value in line.split(",")]
        record = dict(zip(headers, values))
        records.append(record)

    return records


def parse_settings(lines: list[str]) -> dict:
    def convert(value):
        value = value.strip()

        if value.lower() in ("true", "yes"):
            return True

        if value.lower() in ("false", "no"):
            return False

        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value)
        except ValueError:
            return value

    settings = {}
    current_list = None

    for line in lines:
        line = line.split("#", 1)[0].strip()

        if not line:
            continue

        if line.startswith("- "):
            if current_list is not None:
                value = line[2:].strip()
                settings[current_list].append(convert(value))
        else:
            name, value = line.split(":", 1)
            name = name.strip()
            value = value.strip()

            if value == "":
                settings[name] = []
                current_list = name
            else:
                settings[name] = convert(value)
                current_list = None

    return settings


def merge_by_key(
    rows: list[dict], extra: dict, key: str = "id"
) -> list[dict]:
    result = []

    for row in rows:
        additional = extra.get(row.get(key), {})
        merged = additional.copy()
        merged.update(row)
        result.append(merged)

    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        ensure_ascii=False,
        sort_keys=True,
        indent=2
    )
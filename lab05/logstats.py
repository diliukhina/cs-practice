def parse_event(line):
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Неполная строка")

    time, level, message = parts

    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("Неизвестный уровень")

    return {
        "time": time,
        "level": level,
        "message": message
    }

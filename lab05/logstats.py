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


def count_levels(lines):
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"

        if level not in counts:
            counts[level] = 0

        counts[level] += 1

    return counts

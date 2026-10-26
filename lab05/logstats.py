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


def top_errors(lines, n):
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]

            if message not in counts:
                counts[message] = 0

            counts[message] += 1

    errors = []

    for message in counts:
        errors.append([message, counts[message]])

    errors.sort(key=lambda item: (-item[1], item[0]))

    return errors[:max(0, n)]


def format_report(counts, errors):
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for message, count in errors:
        lines.append(f"– {message} – {count}")

    return "\n".join(lines) + "\n"

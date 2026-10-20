def count_by_extension(paths):
    result = {}

    for path in paths:
        name = path.split("/")[-1]
        extension = ""

        if "." in name:
            extension = name.split(".")[-1].lower()

        if extension not in result:
            result[extension] = 0

        result[extension] += 1

    return result


def deepest_path(paths):
    result = ""

    for path in sorted(paths):
        if result == "" or path.count("/") > result.count("/"):
            result = path

    return result


def human_size(n_bytes):
    size = n_bytes
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    i = 0

    while size >= 1024 and i < 4:
        size = size / 1024
        i += 1

    if i == 0:
        return f"{size} Б"

    return f"{size:.1f} {units[i]}"

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

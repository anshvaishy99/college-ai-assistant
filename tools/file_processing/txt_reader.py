def read_txt(file_path: str):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()
def read_file(file, mode):
    if mode == "env":
        with open(file, "r") as f:
            content = f.readlines()
    else:
        raise ValueError("Mode available: env, json")
    return content


def check_file_or_str(file, str_content):
    if not file and not str_content:
        raise ValueError("Must provide either file or str_content")
    if file and str_content:
        raise ValueError("Cannot provide both file and str_content")

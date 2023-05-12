import json

from api.logic.shared import check_file_or_str, read_file


def read_env(file, str_content):
    check_file_or_str(file, str_content)
    if file is not None:
        content = read_file(file, "env")
    elif str_content is not None:
        content = str_content.split("\n")
    else:
        raise ValueError("Please provide either file or str_content")
    return content


def env2json(file=None, str_content=None):
    content = read_env(file, str_content)

    env_dict = {}
    for line in content:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            env_dict[key] = value

    return json.dumps(env_dict, indent=4)

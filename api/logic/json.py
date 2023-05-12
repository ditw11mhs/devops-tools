import json

from api.logic.shared import check_file_or_str, read_file


def read_json(file, str_content):
    check_file_or_str(file, str_content)
    if file is not None:
        content = read_file(file, "json")
    elif str_content is not None:
        content = str_content
    else:
        raise ValueError("Please provide either file or str_content")

    data = json.loads(content)

    return data


def anonym_dict_traverse(in_dict):
    out_dict = {}
    for key, value in in_dict.items():
        if isinstance(value, dict):
            out_dict[key] = anonym_dict_traverse(value)
        else:
            out_dict[key] = key
    return out_dict


def json_anonymizer(file=None, str_content=None):
    content = read_json(file, str_content)

    out_anonym = anonym_dict_traverse(content)

    return json.dumps(out_anonym, indent=4)


def find_environment_name(json_content):
    return list(json_content.keys())


def json2env(file=None, str_content=None):
    content = read_json(file, str_content)

    env_output = ""

    for env_name, env in content.items():
        for key, value in env.items():
            env_key = key.upper()
            env_output += f"{env_key}={value} #{env_name}\n"
        env_output += "\n\n"
    return env_output

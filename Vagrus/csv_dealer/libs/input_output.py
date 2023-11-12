import os
import json


def read_lines(path, split_char='\n'):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n"""')
    return lines


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            data = [None,e]
    return data


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


def get_filepaths(root_path, file_format=None, excludes=None):
    paths = []
    tree = os.walk(root_path)
    for root, dirs, files in tree:
        if not files:
            continue
        for filename in files:
            if excludes:
                if type(excludes) != list:
                    continue
                if filename in excludes:
                    continue
            if file_format:
                if type(file_format) != str:
                    return 'wrong file_format type'
                if not filename.endswith(f'.{file_format}'):
                    continue
            paths.append(f'{root}\\{filename}')
    return paths

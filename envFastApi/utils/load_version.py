import json

path = '../version.json'

def load_version():
    with open(path) as f:
        return (json.load(f)['version'])


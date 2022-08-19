import yaml


def load_config() -> dict:
    with open("env/setting.yml") as yaml_file:
        conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
    return conf

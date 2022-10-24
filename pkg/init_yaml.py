import os

import yaml
# from yaml.loader import SafeLoader
from yaml import Loader


def init_yaml() -> dict:
    __path_to_yml_config = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        "../internal/serviceConfig/config.yml")

    with open(__path_to_yml_config) as config:
        return yaml.load(config, Loader=Loader)

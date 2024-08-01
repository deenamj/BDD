from configparser import ConfigParser

def config_reader(category, key):
    config = ConfigParser()
    config.read("Configuration/config.ini")
    return config.get(category, key)

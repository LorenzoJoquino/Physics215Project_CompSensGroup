import numpy as np
import configparser 

def parseConfig(path, category = 'DEFAULT'):
    config = configparser.ConfigParser()
    config.read(path)
    return config[category]

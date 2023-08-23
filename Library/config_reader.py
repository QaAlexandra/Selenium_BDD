import configparser


def read_config_data(section, key):
    config = configparser.RawConfigParser(allow_no_value=True)
    config.read('/home/alex/Profiscech/autotests/FrontPS/ConfigurationFiles/config.ini')
    return config.get(section, key)

def read_element_location(section, key):

    config = configparser.RawConfigParser(allow_no_value=True)
    config.read('/home/alex/Profiscech/autotests/FrontPS/ConfigurationFiles/elements.ini')
    return config.get(section, key)


def read_assertion_data(section, key):

    config = configparser.RawConfigParser(allow_no_value=True)
    config.read('/home/alex/Profiscech/autotests/FrontPS/ConfigurationFiles/assertion_data.ini')
    return config.get(section, key)




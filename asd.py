import configparser

def config_generator():
    config = configparser.ConfigParser()

    config['pytest'] = {}
    config['pytest']['qt_api'] = 'pyqt5'

    with open('pytest.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

config_generator()
from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    """Получения конфигурации для подключения к базе данных"""
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


def check_salary(salary):
    """Приведение значения зарплата в нужный вид"""
    return salary if not salary is None else 0

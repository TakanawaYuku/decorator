from functools import wraps
import datetime as dt
import csv
import inspect
import os


def log_file_path(path, file_name, s=None):

    def log_function(st_func):
        nonlocal s

        @wraps(st_func)
        def func(*args, **kwargs):
            nonlocal s
            dt.date = f'{dt.datetime.now()}'
            name = st_func.__name__
            arg = inspect.getfullargspec(st_func).args
            arg = [s for s in arg if s not in kwargs.keys()]
            value_arg = dict(zip(arg, list(arg))) | kwargs
            result = st_func(*args, **kwargs)
            result = result if result else None

            logs = {
                'name_function': name,
                'value_args': value_arg if s else None,
                'date': dt.date,
                'result': result
            }
            log_csv(os.path.join(path, file_name), logs)
            return result

        return func

    return log_function


def log_csv(file_csv: str, log: dict):
    # # Вариант 1
    # if os.path.isfile(file_csv):
    #     method = 'a'
    #     flat_generator = [list(log.values())]
    # else:
    #     method = 'w'
    #     flat_generator = [list(log.keys()), list(log.values())]
    # with open(file_csv, f'{method}', encoding='utf-8') as file:
    #     write_log = csv.writer(file, delimiter=',')
    #     write_log.writerows(flat_generator)

    #Вариант 2
    if os.path.isfile(file_csv):
        method = 'a'
        book_csv = [list(log.values())]
    else:
        method = 'w'
        book_csv = [list(log.keys()), list(log.values())]
    with open(file_csv, f'{method}', encoding='utf-8') as file:
        write_log = csv.writer(file, delimiter=',')
        write_log.writerows(book_csv)

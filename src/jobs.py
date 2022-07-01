from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar='"')

        head, *data = csv_reader

    return [dict(zip(head, row)) for row in data]


if __name__ == '__main__':
    print(read('src/jobs.csv'))

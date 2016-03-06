#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 5, 2016

.. codeauthor: svitlana vakulenko <svitlana.vakulenko@gmail.com>
'''

import os
import pandas as pd

from hash_sim import NilsimsaHash


PATH = '/home/vendi/Projects/DoingDataScience/data/at_dump_v1/daopat'
FILES = ['httpwww.wienticket.atfeedsvorverkauf.phpformatcsv',
            'httpwww.apcs.atapcsausgleichsenergiemarktstatistikenopendatastatistikrz2013.csv']

def get_files_from_dir(root, file_type='csv'):
    result = []
    for base, subdirs, files in os.walk(root):
        for name in files:
            if name.lower().endswith('.%s' % file_type.lower()):
                fp = os.path.join(base, name)
                result.append(fp)
    return result


def read_tables(fps, delimiter):
    '''
    Input:
    fps <list of strings>  full paths to files to read tables from

    Return:
    tables <dict> {file_path: rows_generator}
    '''
    tables = {}
    for path in fps:
        df = pd.read_csv(path, sep=delimiter)
        tables[path] = df
    return tables


def test_read_tables():

    # collect file paths
    fps = []
    for file in FILES:
        fps.append(os.path.join(PATH, file))
    print fps
    tables = read_tables(fps, delimiter=';')
    for path, table in tables.items():
        print path
        # print header - columns' labels
        print table.columns.values


def hash_column_str(hash_func, column):
    '''
    Input:
    column <Series>  one column from pandas data frame

    Return:
    hash <str> hash value of the column
    '''
    column_str = str(column)
    return hash_func.compute_hash(column_str)


def hash_column_row_by_row(hash_func, column):
    '''
    Input:
    column <Series>  one column from pandas data frame

    Return:
    hash <str> hash value of the column
    '''

    # column.apply(hash)
    # collect/cluster similar hashes into baskets
    baskets = []
    for row in column:
        # hash only the first row
        row_hash = hash_func.compute_hash(str(row))
        if row_hash not in baskets:
            baskets.append(row_hash)
    # all fields are identical -> single basket for the column
    if len(baskets) == 1:
        return baskets[0]
    else:
        return baskets


def test_hash_column():
    fp = os.path.join(PATH, FILES[0])  # choose first sample file
    table = read_tables([fp], delimiter=';')[fp]  # get the table as a df
    print table.columns.values  # show the header
    # get one column of the table
    column = table['Ort'][:5]  # 10 times 'Wien'
    print column  # class Series, shows column info: length and data type
    # represent column as a string
    # hash
    hash_func = NilsimsaHash()
    print hash_column_str(hash_func, column)
    print hash_column_row_by_row(hash_func, column)


def test_hash_column_length():
    fp = os.path.join(PATH, FILES[0])  # choose first sample file
    table = read_tables([fp], delimiter=';')[fp]  # get the table as a df
    print table.columns.values  # show the header
    # get one column of the table
    column = table['Ort'][:1000]
    print column
    column_short = column[:5]  # first 10 rows
    print column_short
    # hash
    hash_func = NilsimsaHash()
    column_hash = hash_column_str(hash_func, column)
    print column_hash
    column_short_hash = hash_column_str(hash_func, column_short)
    print hash_func.distance_function(column_hash, column_short_hash)
    # assert hash_func.distance_function(column_hash, column_short_hash) == 0
    # test row by row hash function
    column_hash = hash_column_row_by_row(hash_func, column)
    print column_hash
    print int(column_hash, hash_func.hash_base)*2
    column_short_hash = hash_column_row_by_row(hash_func, column_short)
    print hash_func.distance_function(column_hash, column_short_hash)
    assert hash_func.distance_function(column_hash, column_short_hash) == 0


if __name__ == '__main__':
    test_hash_column_length()

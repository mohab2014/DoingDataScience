#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 5, 2016

.. codeauthor: svitlana vakulenko <svitlana.vakulenko@gmail.com>
'''

import os
import pandas as pd


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
    path = '/home/vendi/Projects/DoingDataScience/data/at_dump_v1/daopat'
    files = ['httpwww.wienticket.atfeedsvorverkauf.phpformatcsv',
            'httpwww.apcs.atapcsausgleichsenergiemarktstatistikenopendatastatistikrz2013.csv']
    # collect file paths
    fps = []
    for file in files:
        fps.append(os.path.join(path, file))
    print fps
    tables = read_tables(fps, delimiter=';')
    for path, table in tables.items():
        print path
        # print header - columns' labels
        print table.columns.values

if __name__ == '__main__':
    test_read_tables()

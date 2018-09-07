#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
import argparse
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder


# from sklearn.model_selection import train_test_split


def import_dataset(path: str):
    """
    Import dataset

    :param path:
    :return:
    """
    return pd.read_csv(path)


def encoding_categorical_data_x(matrix):
    label_encoded = LabelEncoder()
    matrix[:, 0] = label_encoded.fit_transform(matrix[:, 0])
    one_hot_encoder = OneHotEncoder(categorical_features=[0])
    return one_hot_encoder.fit_transform(matrix).toarray()


def encoding_categorical_data_y(matrix):
    label_encoded = LabelEncoder()
    return label_encoded.fit_transform(matrix)


def fill_in_missing_values(matrix):
    """
    Take care of missing data in matrix

    :param matrix:
    :return:
    """
    imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imputer.fit(matrix[:, 1:3])
    matrix[:, 1:3] = imputer.transform(matrix[:, 1:3])
    return matrix


def main():
    args = parse_args()
    setup_logging(level=args.loglevel)

    data = import_dataset(path=args.dataset)

    X = data.iloc[:, :-1].values
    Y = data.iloc[:, 3].values
    X = fill_in_missing_values(matrix=X)
    X = encoding_categorical_data_x(matrix=X)
    Y = encoding_categorical_data_y(matrix=Y)
    print(X)
    print(Y)


def setup_logging(level: str):
    fmt = '%(asctime)-15s %(levelname)-8s: %(message)s'
    logging.basicConfig(format=fmt)
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % level)
    logging.basicConfig(level=numeric_level)
    logging.getLogger().setLevel(level=numeric_level)


def parse_args():
    """Get arguments for the command line."""
    parser = argparse.ArgumentParser(
        description='Get information from markets and store into json file')
    parser.add_argument('--loglevel', '-l', default='info',
                        help='logging level')
    parser.add_argument('--dataset', '-d', default='Data.csv')
    return parser.parse_args()


if __name__ == "__main__":
    numeric_level = getattr(logging, 'INFO', None)
    logging.basicConfig(level=numeric_level)
    logging.getLogger().setLevel(numeric_level)
    main()

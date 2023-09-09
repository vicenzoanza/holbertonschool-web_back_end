#!/usr/bin/env python3
""" task 8 """
from pymongo import *


def list_all(mongo_collection):
    """ function that lists all documents in a collection """
    empty_list = []
    for lista in mongo_collection.find():
        empty_list.append(lista)
    return empty_list
        
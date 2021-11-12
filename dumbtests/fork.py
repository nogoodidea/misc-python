#!/bin/python

def fork():
    print("forked")
    fork()
    fork()

fork()

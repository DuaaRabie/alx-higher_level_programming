#!/usr/bin/python3

""" This Module to read files """


def read_file(filename=""):
	""" This function to read files """
	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			print(line, end="")

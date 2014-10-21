#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fasta_label_to_id(label):
    u"""Extract meaningful ID from fasta label"""
    import re
    pattern = re.compile(r'>\w+[ |(]+(\w+)[ |)]')
    match = pattern.match(label)
    return match.group(1)

def binary_search(x, element):
    u"""Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    #  but not including index_end
    index_start = 0
    index_end = len(x)
    while (index_end - index_start)>0:
        index_current = (index_end-index_start)//2 + index_start
        if element == x[index_current]:
            return True
        elif element < x[index_current]:
            index_end = index_current
        elif element > x[index_current]:
            index_start = index_current+1
    return False

def fasta_to_list(filename):
    u""" Læser filer i fasta formatet.

        args:
            filename: String

        returnerer:
            fasta_dict: dict(String, String)
    """
    fasta_ids = []
    unparsed_strings = ""
    with open(filename, "r") as fasta_file:
        for line in fasta_file:
            if line[0] == ">": # Starten på en ny nøgle
                if len(unparsed_strings):
                    fasta_id = fasta_label_to_id(unparsed_strings)
                    fasta_ids.append(fasta_id)
                unparsed_strings = line
            else:
                unparsed_strings += line
    return fasta_ids

def fasta_to_dict(filename):
    return dict.fromkeys(fasta_to_list(filename))
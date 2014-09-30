#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# Funktioner
def find_prot(ecoli_dict, protein_name):
	u""" Finder et protein i ecoli_dict med nøglen protein_name

		args:
			ecoli_dict: dict(String, String)
			protein_name: String

		returnerer:
			protein_sequence: String

		fejl:
			Hvis ikke der findes et protein med navnet protein_name
			returneres en Exception med en fejlmeddelelse.
	"""
	try:
		return ecoli_dict[protein_name]
	except:
		return Exception("Kunne ikke finde ecoli protein med navnet %s" % protein_name)

def find_prot2(ecoli_dict, protein_regex):
	u""" Finder alle nøgler i en dict der matcher protein_regex.

		Hvis ingen nøgler matcher protein_regex returneres en tom liste.

		args:
			ecoli_dict: dict(String, String)
			protein_regex: String

		returnerer:
			keys: List(String)
	"""
	regex = re.compile(protein_regex)
	keys = []
	for key in ecoli_dict:
		if regex.match(key):
			keys.append(key)
	return keys

def read_fasta(filename):
	u""" Læser filer i fasta formatet.

		args:
			filename: String

		returnerer:
			fasta_dict: dict(String, String)
	"""
	fasta_dict = {}
	unparsed_strings = []
	with open(filename, "r") as fasta_file:
		for line in fasta_file:
			if line[0] == ">": # Starten på en ny nøgle
				(name, protein) = __parse_fasta(unparsed_strings)
				fasta_dict[name] = protein
				unparsed_strings = [line]
			else:
				unparsed_strings.append(line)
	del fasta_dict[""] # Fordi unparsed_strings ved første kald til __parse_fasta
					   # er tom, skal der slettes en tom nøgle inden vi returnerer.
	return fasta_dict

# Hjælpefunktioner
def __parse_fasta(lines):
	u""" Intern hjælpefunktion.

		Splitter navn og protein sekvensen samt fjerner linjeskift.
	"""
	if lines == []:
		return ("","")
	name = lines[0][1:-1] # Første tegn er ">", sidste tegn er et linjeskift.
	protein = ""
	for line in lines[1:]:
		protein = protein + line[:-1] # Sidste tegn er et linjeskift.
	return(name, protein)
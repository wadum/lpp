#!/usr/bin/env python
# -*- coding: utf-8 -*-
import handin4

# Konstanter
fasta_fil = "Ecoli.prot.fasta" # Filen der indeholder Ecoli i fasta format.
protein_regex = "[A-Z]{3}_ECOLI" # Regex til del 3 der finder alle nøgler med 3 bogstaver før _ECOLI

# Tests
def test_read_fasta():
	u""" Tester om read_fasta returnerer en ikke tom dict.

		returnerer:
			True hvis dict ikke er tom.
			False hvis dict er tom.
	"""
	return len(handin4.read_fasta(fasta_fil).keys()) != 0

def test_find_prot():
	u""" Tester om find_prot returnerer de korrekte værdier.
		
		Der testes på to protein navne der skal være til 
		stede og på et protein navn der ikke findes.

		returnerer:
			True hvis alle tests er vellykket.
			False hvis bare en enkel test fejler.
	"""
	ingen_fejl = True
	ecoli_dict = handin4.read_fasta(fasta_fil)
	if handin4.find_prot(ecoli_dict, "YBGC_ECOLI") != "MNTTLFRWPVRVYYEDTDAGGVVYHASYVAFYERARTEMLRHHHFSQQALMAERVAFVVRKMTVEYYAPARLDDMLEIQTEITSMRGTSLVFTQRIVNAENTLLNEAEVLVVCVDPLKMKPRALPKSIVAEFKQ":
		print "test_read_fasta fejl på værdi der findes."
		ingen_fejl = False
	if handin4.find_prot(ecoli_dict, "ACPS_ECOLI") != "AILGLGTDIVEIARIEAVIARSGDRLARRVLSDNEWAIWKTHHQPVRFLAKRFAVKEAAAKAFGTGIRNGLAFNQFEVFNDELGKPRLRLWGEALKLAEKLGVANMHVTLADERHYACATVIIES":
		print "test_read_fasta fejl på værdi der findes."
		ingen_fejl = False
	if str(handin4.find_prot(ecoli_dict, "PROTEIN_FINDES_IKKE")) != "Kunne ikke finde ecoli protein med navnet PROTEIN_FINDES_IKKE":
		print "test_read_fasta fejl på værdi der ikke findes."
		ingen_fejl = False
	return ingen_fejl

def test_find_prot2():
	u""" Tester om find_prot2 returnerer korrekte værdier.

		Der testes for om alle returnerede værdier 
		har den korrekte længde.

		returnerer:
			True hvis alle værdier har den korrekte længde.
			False hvis ikke alle værdier har den korrekte længde.
	"""
	ecoli_dict = handin4.read_fasta(fasta_fil)
	ecoli_key_list = handin4.find_prot2(ecoli_dict, protein_regex)
	for key in ecoli_key_list:
		if len(key) != 9:
			return False
	return True

def testAlle():
	u""" Kører alle tests

	"""
	if test_read_fasta() and test_find_prot() and test_find_prot2():
		print "Alle tests er vellykket."

# Main
if __name__ == '__main__':
	testAlle()
	ecoli_dict = handin4.read_fasta(fasta_fil)
	ecoli_key_list = handin4.find_prot2(ecoli_dict, protein_regex)
	print "Antal proteiner med navne på 3 bogstaver før _ECOLI = %d" % len(ecoli_key_list)
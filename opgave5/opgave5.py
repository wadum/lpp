#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

dna_regex = re . compile ( "[U]" )
rna_regex = re . compile ( "[T]" )

class Seq :
	""" Klasse til at gemme biologiske sekvenser. """
	def __init__ ( self , seq , pattern ):
		""" Initialisere en biologisk sekvens. """
		if pattern . search ( seq ):
			print " Warning : sequence contains illegal characters "
		self . data = seq . upper ()
	
	def __getitem__ ( self , index ):
		""" Returnere elementet i sekvensen med det givne index. """
		return self . data [ index ]
	
	def __len__ ( self ):
		""" Returnere længden af sekvensen. """
		return len ( self . data )

class DNA(Seq):
	""" Klasse til at gemme DNA sekvenser """
	def __init__ ( self , seq ):
		""" Initialisere en DNA sekvens. Der må ikke optræde U i sekvensen. """
		Seq . __init__ ( self , seq , dna_regex )

	def __repr__ ( self ) :
		""" Implementere repræsentationen af en DNA streng. """
		return "DNA sequence: %s" % str ( self . data )

	def translate_to_RNA ( self ):
		""" Oversætter DNA strengen til RNA. """
		return RNA ( self . data . replace ( "T" , "U" ) )

class RNA(Seq):
	""" Klasse til at gemme RNA sekvenser """
	def __init__ ( self , seq ):
		""" Initialisere en RNA sekvens. Der må ikke optræde T i sekvensen. """
		Seq . __init__ ( self , seq , rna_regex )
	def __repr__ ( self ):
		""" Implementere repræsentationen af en DNA streng. """
		return "RNA sequence: %s" % str ( self . data )
	def translate_to_DNA ( self ):
		""" Oversætter RNA strengen til DNA. """
		return DNA ( self . data . replace ( "U" , "T" ) )

def RNAorDNA( seq ):
	""" Returnerer seq enten som en DNA eller RNA """
	if dna_regex . search ( seq ):
		return RNA ( seq )
	if rna_regex . search ( seq ):
		return DNA ( seq )


# Print tests fra opgaven.
d = DNA ( ' ACCCGT ' )
print d
r = RNA ( ' UGACG ' )
print r

dna1 = DNA ( ' ACCCGT ' )
rna1 = dna1 . translate_to_RNA ()
print rna1
rna2 = RNA ( ' UGACG ' )
dna2 = rna2 . translate_to_DNA ()
print dna2

print RNAorDNA( ' ACCCGT ' )
print RNAorDNA( ' UGACG ' )
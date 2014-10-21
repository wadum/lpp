#!/usr/bin/env python
# -*- coding: utf-8 -*-
import handin6

test1 = handin6.fasta_to_list("test1.fasta")
test2 = handin6.fasta_to_list("test2.fasta")
test1.sort()
test2.sort()
print test1
print test2
for item1 in test1:
	if not handin6.binary_search(test2, item1):
		print item1
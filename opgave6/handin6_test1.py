#!/usr/bin/env python
# -*- coding: utf-8 -*-
import handin6

test1 = handin6.fasta_to_list("test1.fasta")
test2 = handin6.fasta_to_list("test2.fasta")

print test1
print test2
for item1 in test1:
	midres = False
	for item2 in test2:
		if item1 == item2:
			midres = True
			break
	if not midres:
		print item1

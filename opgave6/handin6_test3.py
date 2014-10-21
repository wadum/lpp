#!/usr/bin/env python
# -*- coding: utf-8 -*-
import handin6

test1 = handin6.fasta_to_dict("test1.fasta")
test2 = handin6.fasta_to_dict("test2.fasta")

for item1 in test1:
	if not item1 in test2:
		print item1
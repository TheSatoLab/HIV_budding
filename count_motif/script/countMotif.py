#!/usr/bin/env python

"""
Usage:
python2 countMotif.py <seq_fasta_file> <motif_1> <motif_2> ... <motif_n>
"""

import sys,re
argvs = sys.argv

fasta_f = open(argvs[1])
fasta_d = {}
for line in fasta_f:
  line = line.strip()
  if '>' in line:
    name = line.replace('>','')
    fasta_d[name] = ""
  else:
    seq = line.upper()
    fasta_d[name] += seq

motif_l = []
for motif in argvs[2:]:
  motif = motif.upper()
  motif_l.append(motif)

print 'seq_name\t' + "\t".join(motif_l)
for name in fasta_d:
  seq = fasta_d[name]
  count_l = []
  for motif in motif_l:
    matched_seq_l = re.findall(motif,seq)
    count = len(matched_seq_l)
    count_l.append(count)
  print name + "\t" + "\t".join([str(c) for c in count_l])


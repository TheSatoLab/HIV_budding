#!/usr/bin/env python

import sys
argvs = sys.argv

min_score = 50

#blast_f = open(argvs[1])

score_d = {}
for f_name in argvs[1:]:
  f = open(f_name)
  for line in f:
    line = line.strip().split()
    read = line[0]
    subject = line[1]
    score = float(line[-1])
    if read not in score_d:
      score_d[read] = {}
    if subject not in score_d[read]:
      score_d[read][subject] = 0
    if score > score_d[read][subject]:
      score_d[read][subject] = score

count_d = {'CH185_WT':0,'CH185_dPTAP1':0,'CH185_dPTAP2':0}
for read in score_d:
  d = score_d[read]
  l = sorted(d.items(), key=lambda x: -x[1])
  subject_top = l[0][0]
  score_top = l[0][1]
  if score_top >= min_score:
    if len(l) > 1:
      score_second = l[1][1]
    else:
      score_second = 0
    if score_top != score_second:
      count_d[subject_top] += 1

print "subject\tcount"
for subject in sorted(count_d):
  count = count_d[subject]
  print subject + "\t" + str(count)


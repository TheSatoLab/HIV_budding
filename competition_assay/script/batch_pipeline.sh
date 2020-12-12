#!/usr/bin/env bash

sample="P4_S8"


java -jar script/trimmomatic-0.39.jar \
  PE \
  -threads 4 \
  -phred33 \
  -trimlog log.txt \
  test_data/${sample}_L001_R1_001.fastq \
  test_data/${sample}_L001_R2_001.fastq \
  ${sample}_L001_R1_001.trimmed.fastq \
  /dev/null \
  ${sample}_L001_R2_001.trimmed.fastq \
  /dev/null \
  SLIDINGWINDOW:4:20 \
  MINLEN:100


#make fasta
  #Read1
  python2 script/fastq2fasta.py \
    ${sample}_L001_R1_001.trimmed.fastq \
    > ${sample}_L001_R1_001.trimmed.fasta
  #Read2
  python2 script/fastq2fasta.py \
    ${sample}_L001_R2_001.trimmed.fastq \
    > ${sample}_L001_R2_001.trimmed.fasta


#blast
  #Read1
  blastn \
    -db blast_db/CH185_reference_150nt.db \
    -query ${sample}_L001_R1_001.trimmed.fasta \
    -out ${sample}_1.txt \
    -word_size 11 -outfmt 6 -num_threads 6 -evalue 1.0E-3

  #Read2
  blastn \
    -db blast_db/CH185_reference_150nt.db \
    -query ${sample}_L001_R2_001.trimmed.fasta \
    -out ${sample}_2.txt \
    -word_size 11 -outfmt 6 -num_threads 6 -evalue 1.0E-3



#read count
  python2 script/assign_read.py \
         ${sample}_*.txt \
         > count_${sample}.txt


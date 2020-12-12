# Competition assay

## Summary
The analysis of RNA-sequencing data reveals the proportion of the three viruses simultaneously inoculated into humanized mice.

## Descrition
Three different HIV-1, CH185 wild-type, the CH185 delta PTAP1 mutant (i.e., CH185\_dPATAP1), and the CH185 delta PTAP2 mutant (i.e., CH185\_dPATAP2) were co-inoculated into nine humanized mice.
At two weeks post-infection, the mice were sacrificed after anesthesia and plasma and spleen were collected.
To analyze the proportion of the three different viruses in plasma and spleen samples prepared above, the RT-PCR amplicon sequencing that targets the p6 gag region in HIV-1 was performed.
As RT-PCR primers, the CH269-PTAP-F “TAGGGAAAATTTGGCCTTCC” and the CH269-PTAP-R “CCTCCAATTCCCCCTATCAT” were used.

- **script/batch\_pipeline.sh**: a shell script to run the analysis
- **script/assign\_read.py**: a python script to count RNA-Seq flagments that assign to each type of virus.
- **script/fastq2fasta.py**: a python script to convert fastq to fasta
- **blast_db**: a directory containing blast db for the three types of viruses
- **test\_data**: a directory containing test data (fastq files)

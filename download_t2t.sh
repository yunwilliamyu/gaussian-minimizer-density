#!/bin/bash
# Downloads the telomere to telomere human chromosomes

if [ ! -f chm13v2.0.fa ]
then
	wget -nc https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/CHM13/assemblies/analysis_set/chm13v2.0.fa.gz
	gunzip -k chm13v2.0.fa.gz
fi

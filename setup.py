#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd

# Download saintq from sourceforge
cmd = "wget https://sourceforge.net/projects/saint-apms/files/saintq_v0.0.4.tar.gz"
os.system(cmd)

cmd = "tar -zxvf saintq_v0.0.4.tar.gz"
os.system(cmd)


cmd = "cd saintq/ ; make ; cd ../"
os.system(cmd)



# Download GTEx data
os.system("wget https://storage.googleapis.com/gtex_analysis_v8/rna_seq_data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct.gz -P data/databases")


# Download gnomAD constraint
cmd = "wget https://storage.googleapis.com/gnomad-public/release/2.1.1/constraint/gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz -P data/databases/"
os.system(cmd)

os.system("gunzip -c data/databases/gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz > data/databases/gnomad_constraint.txt")
os.system("rm data/databases/gnomad.v2.1.1.lof_metrics.by_gene.txt.bgz")


# ### Create folders

if not os.path.exists('intermediate/saintq_config'):
    os.makedirs('intermediate/saintq_config')
    
if not os.path.exists('intermediate/interactome_lists'):
    os.makedirs('intermediate/interactome_lists')
    
if not os.path.exists('manuscript/figures'):
    os.makedirs('manuscript/figures')
    
if not os.path.exists('manuscript/tables'):
    os.makedirs('manuscript/tables')





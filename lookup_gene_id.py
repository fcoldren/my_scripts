#!/usr/bin/env python

from Bio import Entrez

Entrez.email = 'fcoldren@mail.med.upenn.edu'

def lookup_gene_id(gene_symbol):
    """Return the gene ID for a given gene symbol for the human gene."""
    search_term = gene_symbol + " [Preferred Symbol] AND homo sapiens[Orgn]"
    handle = Entrez.esearch(db="gene", term=search_term)
    record = Entrez.read(handle)
    return record['IdList'][0]

def lookup_gene_symbol(gene_id):
    """Return the gene symbol for a gene ID."""
    handle = Entrez.esummary(db="gene", id=gene_id)
    record = Entrez.read(handle)
    return record[0]['Name']

gene_list = ["PTGS1", "ALOX15", "PTGIR"]
gene_list_ids = ["5742", "246", "5739"]

for gene in gene_list_ids:
    gene_info = lookup_gene_symbol(gene)
    print gene_info, gene



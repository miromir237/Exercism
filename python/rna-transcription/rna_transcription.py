def to_rna(dna_strand):
    rna = ''
    for n in dna_strand:
        if n == 'G':
            rna += 'C'
        elif n == 'C':
            rna += 'G'
        elif n == 'T':
            rna += 'A'
        elif n == 'A':
            rna += 'U'
    return rna


    mydict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    return dna_strand.translate(mydict)
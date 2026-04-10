# DNA Complement Tool

A simple Python command-line tool that reads a DNA sequence from a FASTA file and returns its complement.

## How It Works

Each DNA base is swapped with its complementary base:

| Base | Complement |
|------|------------|
| A    | T          |
| T    | A          |
| G    | C          |
| C    | G          |

## Usage

```bash
python dna_complement.py
```

You will be prompted to enter the path to your FASTA file:

```
Enter file path: sample.fasta
Complement:
TACGGCTA...
```

### Example FASTA Input (`sample.fasta`)

```
>My Sequence
ATGCATGC
```

### Output

```
TACGTACG
```

## Requirements

- Python 3.6+
- No external libraries required

## Error Handling

- Invalid characters in the sequence are reported with their position.
- Missing files produce a clear error message instead of a crash.

## Project Structure

```
dna-complement-tool/
├── dna_complement.py   # Main script
├── sample.fasta        # Example input file
└── README.md
```

## Test Data

The sample sequence used in this project is the **TP53 coding sequence (CDS)** — the most frequently mutated gene in human cancer, encoding the tumor suppressor protein p53.

| Field | Details |
|-------|---------|
| Gene | TP53 (tumor protein p53) |
| Organism | *Homo sapiens* |
| Accession | NM_000546.6 |
| Protein | NP_000537.3 (cellular tumor antigen p53 isoform a) |
| Location | CDS: 143–1324 |
| Database | NCBI RefSeq |

**Source:** https://www.ncbi.nlm.nih.gov/nuccore/NM_000546.6

## References

- Bouaoun L, et al. (2016). TP53 Variations in Human Cancers: New Lessons from the IARC TP53 Database. *Human Mutation*, 37(9), 865–876.
- NCBI RefSeq: NM_000546.6 — https://www.ncbi.nlm.nih.gov/nuccore/NM_000546.6

## License

MIT License

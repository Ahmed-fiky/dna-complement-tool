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

## License

MIT License

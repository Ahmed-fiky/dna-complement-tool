"""
DNA Complement Tool
Reads a DNA sequence from a FASTA file and returns its complement.
"""

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def parse_fasta(file_path: str) -> str:
    """Read a FASTA file and return the raw sequence (uppercase, no headers)."""
    with open(file_path, "r") as f:
        lines = f.readlines()
    return "".join(
        line.strip() for line in lines if not line.startswith(">")
    ).upper()


def get_complement(sequence: str) -> str:
    """
    Return the complement of a DNA sequence.

    Args:
        sequence: A string of DNA bases (A, T, G, C).

    Returns:
        The complement string.

    Raises:
        ValueError: If the sequence contains an invalid character.
    """
    result = []
    for i, base in enumerate(sequence):
        if base not in COMPLEMENT:
            raise ValueError(
                f"Invalid base '{base}' at position {i + 1}. "
                f"Only A, T, G, C are allowed."
            )
        result.append(COMPLEMENT[base])
    return "".join(result)


def get_dna_complement_from_file(file_path: str) -> str:
    """Parse a FASTA file and return the complement of its sequence."""
    sequence = parse_fasta(file_path)
    return get_complement(sequence)


def main():
    file_path = input("Enter file path: ").strip()
    try:
        complement = get_dna_complement_from_file(file_path)
        print(f"Complement:\n{complement}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

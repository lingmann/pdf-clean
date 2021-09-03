#!/usr/bin/env python3

import argparse
from pathlib import Path

import pikepdf


def main():
    parser = argparse.ArgumentParser(
        description="Remove PDF modification protection. File specified must be underneath current working directory. Cleaned file will be written with `-cleaned` added to the file name.")
    parser.add_argument('source_file', help='PDF to be cleaned')
    args = parser.parse_args()
    source_original_path = Path(vars(args)['source_file'])
    source_data_path = Path("/data") / source_original_path
    dest_path = source_data_path.parent / (source_data_path.stem + "-cleaned.pdf")

    try:
        cleaned = pikepdf.open(source_data_path)
        cleaned.save(dest_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

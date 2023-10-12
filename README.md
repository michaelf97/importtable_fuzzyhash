# PE Import Table Fuzzy Hashing

This script computes the fuzzy hash (ssdeep) of the import table of a given Portable Executable (PE) file.
Prerequisites

Before running the script, ensure you have the following Python libraries installed:

* pefile: For parsing PE files.
* ssdeep: For calculating ssdeep hash.

You can install these libraries using pip:

```bash
pip install pefile ssdeep
```

## Usage

To run the script:
```bash
python script_name.py <path_to_PE_file>
```

For help:
```bash
python script_name.py -h
```

## Example
Given a PE file named sample.exe, you can compute its import table's ssdeep hash as follows:
```bash
#> ~/Documents/Python$ python script_name.py sample.exe
192:Co+4q7+MD0aBqdF4ia/EXfTP6ggv3vJgEIAbjNPMAO4:Co/m+MD0aBqdF4i1TP6gsvJgEIAI4
```

## Code Overview

* get_import_table_data(pe): Extracts the import table data from the PE file.

* calculate_ssdeep_of_import_table(file_path): Computes the ssdeep hash for the import table data of the PE file at the specified path.

When executed, the script checks for the provided command-line arguments and calculates the ssdeep hash of the import table if a valid file path is provided.

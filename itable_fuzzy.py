import pefile
import ssdeep
import sys

docstring = '''
Name: PE Import Table Fuzzy Hash calculator
Description: Calculates the Fuzzy Hash (ssdeep) of a PE files import table.
'''

help_message = f'''
Usage: {sys.argv[0]} <path_to_pe>'''


def get_import_table_data(pe):

    imports_data = []

    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            for imp in entry.imports:
                imports_data.append((entry.dll, imp.name))

    imports_bytes = b''.join([dll + func if func else dll for dll, func in imports_data])

    return imports_bytes

def calculate_ssdeep_of_import_table(file_path):
    pe = pefile.PE(file_path)
    imports_data = get_import_table_data(pe)
    return ssdeep.hash(imports_data)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print(f"{docstring}{help_message}")
            sys.exit(0)
    else:
        print("Please provide a filename")
        sys.exit(1)

    file_path = sys.argv[1]

    print(calculate_ssdeep_of_import_table(file_path))

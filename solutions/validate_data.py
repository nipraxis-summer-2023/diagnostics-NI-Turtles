

from pathlib import Path
import sys
import hashlib


def file_hash(filename):
    """ Get SHA1 hash of the contents of a file
    Parameters
    ----------
    filename : str
        Name of file to read
    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """



def validate_data(data_directory):
    """ Read ``data_hashes.txt`` file in `data_directory`, check hashes
    Parameters
    ----------
    data_directory : str
        Directory containing data and ``data_hashes.txt`` file.
    Returns
    -------
    None
    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``data_hashes.txt`` file.
    """



def main():
    # This function (main) is called when this file is run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please provide the data directory as a command-line argument")
    data_directory = sys.argv[1]

    try:
        # Call the function to validate data in the data directory
        validate_data(data_directory)
        print("Validation successful. All files have matching hashes.")
    except ValueError as e:
        print(f"Validation failed: {str(e)}")


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()

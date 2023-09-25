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
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as fobj:
        data = fobj.read()  # Read the entire file at once
        sha1.update(data)
    contents = Path(filename).read_bytes()
    return hashlib.sha1(contents).hexdigest()


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

    data_path = Path(data_directory)
    data_hashes_file = data_path / 'hash_list.txt'

    # Read the file as text and split it into lines
    for line in data_hashes_file.read_text().splitlines():
        recorded_hash, filename = line.strip().split()

        full_filename = data_path / filename

        if not full_filename.is_file():
            raise ValueError(f"File not found: {full_filename}")

        calculated_hash = file_hash(full_filename)

        if recorded_hash != calculated_hash:
            raise ValueError(
                f"Hash mismatch for file '{filename}': expected {recorded_hash}, got {calculated_hash}")

    print("Validation of Hash List is Successful")


def main():
    # This function (main) is called when this file is run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please provide the data directory as a command-line argument")
    data_directory = sys.argv[1]
    # Call the function to validate data in the data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()

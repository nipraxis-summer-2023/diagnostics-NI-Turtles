# your_script.py
import os
from pathlib import Path
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

# Import the modified findoutlie library
from findoutlie import outfind



def print_outliers(data_directory):
    # Find outliers using the outfind library
    outlier_dict = outfind.find_outliers(data_directory)

    for fname, outlier_volumes in outlier_dict.items():
        if len(outlier_volumes) > 0:
            print(f"Scan: {fname}")
            print(f"Outlier Volumes: {', '.join(map(str, outlier_volumes))}")

            # Create a summary text file in the data directory
            data_dir = os.path.dirname(fname)
            summary_filename = os.path.join(data_dir, "OutlierExplained.txt")
            with open(summary_filename, 'w') as summary_file:
                summary_file.write(f"Scan: {fname}\n")
                summary_file.write(f"Outlier Volumes: {', '.join(map(str, outlier_volumes))}\n")
                summary_file.write("Summary:\n")
                # Add your summary and educated guess here
                summary_file.write("Why this scan should be rejected as an outlier: [Your Explanation]\n")
                summary_file.write("Educated guess about the cause of the difference: [Your Guess]\n")

def get_parser():
    parser = ArgumentParser(
        description=__doc__,  # Usage from docstring
        formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'data_directory',
        help='Directory containing data'
    )
    return parser


def main():
    # This function (main) is called when this file is run as a script.
    #
    # Get the data directory from the command-line arguments
    parser = get_parser()
    args = parser.parse_args()

    # Call the function to find and print outliers
    print_outliers(args.data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()

# Import the check_quine function from the quine_checker.py file:
from quine_checker import check_quine
import argparse


def main():
    """
    Entry point for the quine checker script.
    """
    parser = argparse.ArgumentParser(description="Check if a given "
                                     "Python script is a quine.")
    parser.add_argument('file_path', type=str,
                        help="Path to the Python script to check.")

    args = parser.parse_args()
    file_path = args.file_path

    result = check_quine(file_path)
    print(result)


if __name__ == "__main__":
    main()

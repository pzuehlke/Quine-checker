import logging
import io
from contextlib import redirect_stdout


logging.basicConfig(filename='logfile.txt', level=logging.INFO)


def read_file_content(file_path: str) -> str:
    """
    Reads the contents of a file and returns it as a string.
    Parameters:
        * file_path: The path to the file to be read.
    Returns:
        * The content of the file as a string if successful.
    Raises:
        FileNotFoundError: If the file is not found.
        IOError: If an IOError occurs while reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as infile:
            file_content = infile.read()
            logging.info(f"The content of {file_path} was "
                         "successfully extracted.")
            return file_content
    except FileNotFoundError as e:
        logging.error(f"File {file_path} was not found!")
        raise e
    except IOError as e:
        logging.error(f"An IOError occurred while reading {file_path}!")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}!")
        raise e


def execute_script_and_capture_output(file_path: str) -> str:
    """
    Executes a Python script given its file path and captures its std. output.
    WARNING: Please ensure that the script to be checked can safely be run!
    Parameters:
        * file_path: The path to the Python script to be executed.
    Returns:
        * The standard output (str) produced by the script.
    """
    class ScriptExecutionError(Exception):
        """An error occurred while executing a Python script."""

    # Read the file (assuming that `read_file_content` has been defined):
    script_content = read_file_content(file_path)

    # Capture the output and the error:
    output = io.StringIO()
    try:
        with redirect_stdout(output):
            exec(script_content)
    except Exception as e:
        raise ScriptExecutionError(f"Could not execute the script: {e}")

    stdout_content = output.getvalue()
    return stdout_content


def first_differing_words(string_1: str, string_2: str) -> (str, str):
    """
    Compares two strings word by word and returns the first pair of words where
    they differ.
    Parameters:
        * string_1: The first string to compare.
        * string_2: The second string to compare.
    Returns:
        * The first pair of words where the two strings differ, or a pair of
          empty strings if they are identical.
    """
    words_1 = string_1.split()
    words_2 = string_2.split()

    # Zip the lists and compare each word pair:
    for word_1, word_2 in zip(words_1, words_2):
        if word_1 != word_2:
            return word_1, word_2

    # Handle the case where one string is a substring of the other:
    len_1 = len(words_1)
    len_2 = len(words_2)
    if len_1 == len_2:
        return "", ""
    elif len_1 < len_2:
        return "", words_2[len_1]
    else:
        return words_1[len_2], ""


def check_quine(file_path: str) -> str:
    """
    Checks if the script located at the given file path is a quine.
    Parameters:
        * file_path: The path to the Python script to be checked.
    Returns:
        * A message indicating whether the script is a quine or not.
    """
    try:
        content = read_file_content(file_path)
        output = execute_script_and_capture_output(file_path)
    except Exception as e:
        logging.error(f"An error occurred while processing the script: {e}")
        raise

    word_1, word_2 = first_differing_words(content, output)
    delimiter = "```"

    if word_1 == word_2 == "":
        result = "\nCongratulations! The script you provided is a quine."
    else:
        result = (f"Unfortunately, the script you provided is not a quine. "
                  f"The first differing words in the content and output "
                  f"(respectively) are: {word_1} and {word_2}")

    content_info = ("\n\nHere is the content, delimited by triple backticks:"
                    f"\n{delimiter}\n{content}{delimiter}")
    output_info = ("\n\nAnd here is the output:"
                   f"\n{delimiter}\n{output}{delimiter}")

    return f"{result}{content_info}{output_info}"

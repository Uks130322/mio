"""
mio: module (contains functions capture_output, restore_output, print_file and clear_file)
"""

import sys
_file_object = None


def capture_output(file="capture_file.txt"):
    """
    redirect standard output into the file
    :return: None
    """
    global _file_object
    print(f"output will be sent to file: {file}")
    print("restore to normal by calling 'mio.restore_output()'")
    _file_object = open(file, 'w')
    sys.stdout = _file_object


def restore_output():
    """
    restore to normal standard output
    :return: None
    """
    global _file_object
    sys.stdout = sys.__stdout__
    _file_object.close()
    print("standard output has been restored back to normal")


def print_file(file='capture_file.txt'):
    """
    hand over the file into standard output
    :return: None
    """
    f = open(file, 'r')
    print(f.read())
    f.close()


def clear_file(file='captured_file.txt'):
    """
    clear the file
    :return: None
    """
    f = open(file, 'w')
    f.close()

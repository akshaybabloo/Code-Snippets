from __future__ import print_function

import os


def list_files(startpath, write_to_file=False):
    """
    This lists the files & folders recursively and displays as a tree structure.

    Parameters
    ----------
    write_to_file
    startpath

    """

    if write_to_file is True:
        fg = open('structure.txt', 'w+')

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        a = ('{}|-{}/'.format(indent, os.path.basename(root)))
        print(a)
        if write_to_file is True:
            fg.write(a)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            b = ('{}|-{}'.format(subindent, f))
            print(b)
            if write_to_file is True:
                fg.write(b)


if __name__ == "__main__":
    list_files("")  # enter your folder location

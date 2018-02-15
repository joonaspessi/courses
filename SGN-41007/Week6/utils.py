from os.path import join, abspath
from os import walk


def absolute_file_paths(directories):
    for directory in directories:
        for dir_path, _, file_names in walk(directory):
            for f in file_names:
                yield abspath(join(dir_path, f))
# coding: utf-8
from __future__ import absolute_import

import os

from setuptools import find_packages
from setuptools import setup
import setuptools.command.build_py


# Create custom `find_packages` function.
def custom_find_packages(where='.', exclude=(), include=('*',)):
    """
    Find package names.

    :param where: Start directory.

    :param exclude: Excluded patterns.

    :param include: Included patterns.

    :return: Accepted package names list.
    """
    # Find package names.
    # Delegate to original `find_packages` function.
    package_names = find_packages(where=where, exclude=exclude, include=include)

    # Accepted package names.
    accepted_packages_names = []

    # For each package name.
    for package in package_names:
        # If the package name contains `excluded`.
        if 'excluded' in package:
            # Reject the package name.
            continue
        # If the package name not contains `excluded`.
        else:
            # Accept the package name.
            accepted_packages_names.append(package)

    # Return accepted package names
    return accepted_packages_names


# Store original `find_package_modules` function
find_package_modules = \
    setuptools.command.build_py.build_py.find_package_modules


# Create custom `find_package_modules` function
def custom_find_package_modules(self, package, package_dir):
    """
    Find module infos in given package.

    :param package: Package name.

    :param package_dir: Package directory path.

    :return: Accepted module infos list.
    """
    # Find module infos in the package.
    # Delegate to original `find_package_modules`.
    infos = find_package_modules(self, package, package_dir)

    # Accepted module infos.
    accepted_infos = []

    # For each module info.
    for info in infos:
        # Unpack the module info.
        pkg_full_name, module_bare_name, module_path = info

        # If the module name contains `excluded`.
        if 'excluded' in module_bare_name:
            # Reject the module info.
            continue
        # If the module name not contains `excluded`.
        else:
            # Accept the module info.
            accepted_infos.append(
                (pkg_full_name, module_bare_name, module_path)
            )

    # Return accepted module info list
    return accepted_infos


# Replace original `find_package_modules` function with the custom one.
setuptools.command.build_py.build_py.find_package_modules = \
    custom_find_package_modules


# Store original `find_data_files` function.
find_data_files = \
    setuptools.command.build_py.build_py.find_data_files


# Create custom `find_data_files` function.
def custom_find_data_files(self, package, src_dir):
    """
    Find data file paths in given package.

    :param package: Package name.

    :param src_dir: Package directory path.

    :return: Accepted data file paths list.
    """
    # Accepted data file paths.
    accepted_file_paths = []

    # For each file in the package directory.
    for file_bare_name in os.listdir(src_dir):
        # Get file path.
        file_path = os.path.join(src_dir, file_bare_name)

        # If the file is regular file.
        if os.path.isfile(file_path):
            # If the file is not `.py` file.
            if not file_bare_name.endswith('.py'):
                # If the file name contains `excluded`.
                if 'excluded' in file_bare_name:
                    # Reject the file path.
                    continue
                # If the file name not contains `excluded`.
                else:
                    # Accept the file path.
                    accepted_file_paths.append(file_path)

    # Return accepted data file paths.
    return accepted_file_paths


# Replace original `find_data_files` function with the custom one
setuptools.command.build_py.build_py.find_data_files = \
    custom_find_data_files


if __name__ == '__main__':
    setup(
        # Project name.
        name='AoikSetupPyIncludeExclude',

        # Project description.
        description=(
            'How to include and exclude Python module files and data files in'
            'setup.py flexibly.'
        ),

        # Project version.
        version='0.0.1',

        # Package root directory.
        package_dir={
            '': 'src'
        },

        # Find package names in package root directory `src`.
        packages=custom_find_packages('src'),
    )

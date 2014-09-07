# -*- coding:utf-8 -*-
#  _________________________________________________________________________
#
#  Gcovr: A parsing and reporting tool for gcov
#  Copyright (c) 2013 Sandia Corporation.
#  This software is distributed under the BSD License.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  For more information, see the README.md file.
#  _________________________________________________________________________

from optparse import OptionParser
from os import environ
import os.path


def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = OptionParser()
    parser.add_option(
        '--version',
        help='Print the version number, then exit.',
        action='store_true',
        dest='version',
        default=False
    )
    parser.add_option(
        '-v', '--verbose',
        help='Print progress messages.',
        action='store_true',
        dest='verbose',
        default=False
    )
    parser.add_option(
        '--object-directory',
        help='Specify the directory that contains the gcov data files.  gcovr '
             'must be able to identify the path between the *.gcda files and '
             'the directory where gcc was originally run.  Normally, gcovr '
             'can guess correctly.  This option overrides gcovr\'s normal '
             'path detection and can specify either the path from gcc to the '
             'gcda file (i.e. what was passed to gcc\'s \'-o\' option), or '
             'the path from the gcda file to gcc\'s original working '
             'directory.',
        action='store',
        dest='objdir',
        default=None
    )
    parser.add_option(
        '-o', '--output',
        help='Print output to this filename.',
        action='store',
        dest='output',
        default=None
    )
    parser.add_option(
        '-k', '--keep',
        help='Keep the temporary *.gcov files generated by gcov.  '
             'By default, these are deleted.',
        action='store_true',
        dest='keep',
        default=False
    )
    parser.add_option(
        '-d', '--delete',
        help='Delete the coverage files after they are processed.  '
             'These are generated by the users\'s program, and by default '
             'gcovr does not remove these files.',
        action='store_true',
        dest='delete',
        default=False
    )
    parser.add_option(
        '-f', '--filter',
        help='Keep only the data files that match this regular expression.',
        action='append',
        dest='filter',
        default=[]
    )
    parser.add_option(
        '-e', '--exclude',
        help='Exclude data files that match this regular expression.',
        action='append',
        dest='exclude',
        default=[]
    )
    parser.add_option(
        '--gcov-filter',
        help='Keep only gcov data files that match this regular expression.',
        action='store',
        dest='gcov_filter',
        default=None
    )
    parser.add_option(
        '--gcov-exclude',
        help='Exclude gcov data files that match this regular expression.',
        action='append',
        dest='gcov_exclude',
        default=[]
    )
    parser.add_option(
        '-r', '--root',
        help='Defines the root directory for source files.  '
             'This is also used to filter the files, and to standardize '
             'the output.',
        action='store',
        dest='root',
        default=None
    )
    parser.add_option(
        '-x', '--xml',
        help='Generate XML instead of the normal tabular output.',
        action='store_true',
        dest='xml',
        default=False
    )
    parser.add_option(
        '--xml-pretty',
        help='Generate pretty XML instead of the normal dense format.',
        action='store_true',
        dest='prettyxml',
        default=False
    )
    parser.add_option(
        '--html',
        help='Generate HTML instead of the normal tabular output.',
        action='store_true',
        dest='html',
        default=False
    )
    parser.add_option(
        '--html-details',
        help='Generate HTML output for source file coverage.',
        action='store_true',
        dest='html_details',
        default=False
    )
    parser.add_option(
        '--html-absolute-paths',
        help='Set the paths in the HTML report to be absolute instead '
             'of relative.',
        action='store_false',
        dest='relative_anchors',
        default=True
    )
    parser.add_option(
        '-b', '--branches',
        help='Tabulate the branch coverage instead of the line coverage.',
        action='store_true',
        dest='show_branch',
        default=None
    )
    parser.add_option(
        '-u', '--sort-uncovered',
        help='Sort entries by increasing number of uncovered lines.',
        action='store_true',
        dest='sort_uncovered',
        default=None
    )
    parser.add_option(
        '-p', '--sort-percentage',
        help='Sort entries by decreasing percentage of covered lines.',
        action='store_true',
        dest='sort_percent',
        default=None
    )
    parser.add_option(
        '--gcov-executable',
        help='Defines the name/path to the gcov executable [defaults to the '
             'GCOV environment variable, if present; else \'gcov\'].',
        action='store',
        dest='gcov_cmd',
        default=environ.get('GCOV', 'gcov')
    )
    parser.add_option(
        '--exclude-unreachable-branches',
        help='Exclude from coverage branches which are marked to be excluded '
             'by LCOV/GCOV markers or are determined to be from lines '
             'containing only compiler-generated "dead" code.',
        action='store_true',
        dest='exclude_unreachable_branches',
        default=False
    )
    parser.add_option(
        '-g', '--use-gcov-files',
        help='Use preprocessed gcov files for analysis.',
        action='store_true',
        dest='gcov_files',
        default=False
    )
    parser.add_option(
        '-s', '--print-summary',
        help='Prints a small report to stdout with line & branch '
             'percentage coverage',
        action='store_true',
        dest='print_summary',
        default=False
    )
    parser.usage = 'gcovr [options]'
    parser.description = \
        'A utility to run gcov and generate a simple report that summarizes ' \
        'the coverage'
    (options, args) = parser.parse_args()
    if options.output is not None:
        options.output = os.path.abspath(options.output)
    return (options, args)

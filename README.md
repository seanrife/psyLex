psyLex
======

A collection of functions for the psychological analysis of corpora using LIWC-style dictionaries. The psyLex program and associated functions are designed to be used with larger datasets in a wide variety of environments, for which the original LIWC software may be unsuitable. psyLex can esaily be implemented as part of a shell script, using batch jobs, in an interactive form (e.g., in an app), or as part of a larger Python program.

## Overview

Two primary functions are provided:
- readDict(): reads in a LIWC-style dictionary file and returns (1) a dictionary of linguistic categories (e.g., positive emotion, anger, etc.) and (2) a multidimensional list of words and the categories to which they belong.
- wordCount(): analyzes a given string using the word list returned by readDict() and returns raw word counts or percentages for each category supplied by readDict().

These functions can be implemented in any existing Python program. Additionally, a main script - psyLex.py - can be run as a standalone program using any Python interpreter.

## Notes

For those familiar with the LIWC program, there are a number of notable differences. As such, results obtained from psyLex may differ from those obtained with LIWC. However, such differences should be quite small, and of little statistical/practical significance (particularly when used with extremely large datasets).
- The original LIWC program used a wildcard-style method ("*") of specifying word stems in the dictionary. In order to enhance forward-compatibility and flexibility, psyLex identifies dictionary words with wildcards and uses a stemmer (the Porter Stemming Algorithm by default) to match dictionary stems with words in the analyzed text.
- At present, only English is supported (non-utf8 characters are filtered out). This is mostly because I'm an arrogant American and haven't bothered to learn any other languages. If anyone wants to help with this, let me know...

## Dependencies

Basic linguistic functions (tokenization, stemming, etc.) are performed via. the Python Natural Language Toolkit - available from nltk.org.

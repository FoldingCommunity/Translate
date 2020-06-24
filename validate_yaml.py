#!/usr/bin/env python3

import fnmatch
import yaml
import traceback
import os
import sys


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


# eg: Localization/en-US/statistics.yaml
def path_to_language(file):
    (head, tail) = os.path.split(file)
    (head, tail) = os.path.split(head)
    return tail


def filename_is(path, filename):
    (head, tail) = os.path.split(path)
    return tail == filename


def ensure_schema(translation, path):
    keys = ["url", "language", "text", "title"]

    for key in keys:
        if key not in translation:
            raise Exception("Missing '%s' key in %s" % (key, path))


def ensure_language(translation, path):
    expected_language = path_to_language(path)
    if translation["language"] != expected_language:
        raise Exception(
            "%s was expected to be in language %s, but instead was %s" %
            (path, expected_language, translation["language"]))


exit_code = 0
for path in find("*.yaml", "Localization"):
    with open(path) as f:
        print("Validating", path)
        try:
            translation = yaml.safe_load(f)
            ensure_schema(translation, path)
            ensure_language(translation, path)
        except Exception as e:
            exit_code = 1
            traceback.print_exc(file=sys.stdout)

exit(exit_code)

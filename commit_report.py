#!/usr/bin/env python3

import os
import sys
import base64
from github import Github

TRANSLATION_REPORT_FILENAME = "translation_report.md"

github_token = sys.argv[1]
g = Github(github_token)
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
branch = os.getenv("GITHUB_REF")


def get_previous_file(path):
    return repo.get_contents(path, ref=os.getenv("GITHUB_SHA"))


def decode_contents(contents):
    decoded_bytes = base64.b64decode(contents.content)
    return str(decoded_bytes, "utf-8")


previous_report_obj = get_previous_file(TRANSLATION_REPORT_FILENAME)
previous_report = decode_contents(previous_report_obj)

with open(TRANSLATION_REPORT_FILENAME) as r:
    current_report = r.read()

if previous_report != current_report:
    repo.update_file(path=TRANSLATION_REPORT_FILENAME, message="Updated translation report", content=current_report,
                     sha=previous_report_obj.sha, branch=branch)

#!/usr/bin/env python3

import os
import sys
import base64
from github import Github

TRANSLATION_REPORT_FILENAME = "translation_report.md"

github_token = sys.argv[1]
g = Github(github_token)
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
branch = sys.argv[2]

previous_report_obj = repo.get_contents(TRANSLATION_REPORT_FILENAME, ref=branch)
previous_report = previous_report_obj.decoded_content.decode("utf-8")

with open(TRANSLATION_REPORT_FILENAME) as r:
    current_report = r.read()

if previous_report != current_report:
    repo.update_file(previous_report_obj.path, "Updated translation report", current_report, previous_report_obj.sha,
                     branch=branch)

#!/usr/bin/env python3

import os
import sys
import json
from github import Github

with open(os.getenv("GITHUB_EVENT_PATH")) as e:
    github_event = json.load(e)

github_token = sys.argv[1]
g = Github(github_token)
repo = g.get_repo(github_event['pull_request']['head']['repo']['full_name'])
branch = github_event['pull_request']['head']['ref']

TRANSLATION_REPORT_FILENAME = "translation_report.md"

previous_report_obj = repo.get_contents(TRANSLATION_REPORT_FILENAME, ref=branch)
previous_report = previous_report_obj.decoded_content.decode("utf-8")

with open(TRANSLATION_REPORT_FILENAME) as r:
    current_report = r.read()

if previous_report != current_report:
    repo.update_file(previous_report_obj.path, "Updated translation report", current_report, previous_report_obj.sha,
                     branch=branch)

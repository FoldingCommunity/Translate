#!/usr/bin/env python3

from pathlib import Path
from typing import TextIO


class POHeaderData:
    def __init__(self, header_fields: dict):
        self.header_fields = header_fields


class ReportGenerator:
    """
    Reads .po files from a folder (see ROOT_FOLDER) and locates the original files (see SOURCE_LANGUAGE)
    to compare them to the other available translations. Then it will render out a Markdown-formatted
    report of the current status of those available translations.

    To retrieve the report, just call `get_report()`.
    """
    ROOT_FOLDER = 'Localization/'
    SOURCE_LANGUAGE = 'en-US'

    def get_report(self) -> str:
        translations = {}
        original_files = self._find_po_files(Path(f'{self.ROOT_FOLDER}{self.SOURCE_LANGUAGE}'))
        languages = self._find_languages()
        for (language, directory) in sorted(languages.items(), key=lambda item: item[0]):
            translations[language] = {'files': {}}
            files = self._find_po_files(directory)
            for file in sorted(original_files.keys()):
                if file in files:
                    translations[language]['files'][file] = self._verify_translation(original_files[file], files[file], language)
                else:
                    translations[language]['files'][file] = {'error': 'missing'}
        return self._render_report(translations)

    def _find_po_files(self, path: Path) -> dict:
        files = {}
        for file in path.glob('*.po'):
            with file.open('r', encoding='UTF-8') as fh:
                files[file.name] = self._extract_po_header(fh)
        return files

    @staticmethod
    def _extract_po_header(file_handler: TextIO) -> POHeaderData:
        in_header = False
        header_fields = {}
        header_string = ""
        for line in file_handler:
            if line.startswith('msgid ""') and not in_header:
                in_header = True
            elif line.startswith('msgid ""') and in_header:
                break
            elif line.startswith('msgstr "'):
                header_string += line[8:-2]
            elif line.startswith('"'):
                header_string += line[1:-2]
        for line in header_string.split("\\n"):
            fields = line.split(':')
            if len(fields) == 2:
                header_fields[fields[0].strip()] = fields[1].strip()
        return POHeaderData(header_fields)

    def _find_languages(self) -> dict:
        root_folder = Path(self.ROOT_FOLDER)
        languages = {}
        for directory in root_folder.glob('*-*'):
            if directory.name != self.SOURCE_LANGUAGE:
                languages[directory.name] = directory
        return languages

    @staticmethod
    def _verify_translation(original_file: POHeaderData, translated_file: POHeaderData, language: str) -> dict:
        details = {}
        if translated_file.header_fields['Target-Language'] == language:
            details['Target-Language'] = '✔'
        else:
            details['Target-Language'] = f"""is "{translated_file.header_fields['Target-Language']}" but should be "{language}" """
        if translated_file.header_fields['Source-Version'] == original_file.header_fields['Source-Version']:
            details['Source-Version'] = '✔'
        else:
            details['Source-Version'] = f"""not up-to-date ({translated_file.header_fields['Source-Version']} vs {original_file.header_fields['Source-Version']})"""
        return details

    @staticmethod
    def _render_report(translations: dict):
        details = """## Details\n"""
        overview = {}
        for (language, files) in translations.items():
            details += f"""### {language}\n"""
            details += """| File | Target-Language | Source-Version | Error |\n"""
            details += """| ---- | --------------- | -------------- | ----- |\n"""
            errors = 0
            updates_needed = 0
            for (file, file_info) in files['files'].items():
                if 'error' in file_info:
                    details += f"""| {file} | ? | ? | {file_info['error']} |\n"""
                    errors += 1
                else:
                    details += f"""| {file} | {file_info['Target-Language']} | {file_info['Source-Version']} | - |\n"""
                    if file_info['Target-Language'] != '✔' or file_info['Source-Version'] != '✔':
                        updates_needed += 1
            details += """\n[↑ Back to the overview](#overview)\n"""
            overview[language] = {'percentage_done': round((len(files['files']) - errors) / len(files['files']) * 100), 'updates_needed': updates_needed}

        result = """# Translation Status Report\n"""
        result += """## Overview\n"""
        result += """| Language | Done % | Updates Needed |\n"""
        result += """| -------- | -----: | -------------: |\n"""
        for (language, stats) in overview.items():
            result += f"""| [{language}](#{language}) | """
            if stats['percentage_done'] >= 100:
                result += '✔ '
            result += f"""{stats['percentage_done']}% | """
            if stats['updates_needed'] == 0:
                result += '✔ '
            result += f"""{stats['updates_needed']} |\n"""
        result += details

        return result


with open('translation_report.md', 'w', encoding='UTF-8') as fh:
    report = (ReportGenerator()).get_report()
    fh.write(report)

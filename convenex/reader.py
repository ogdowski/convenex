from typing import List

import xmltodict


class Note:
    def __init__(self, title: str, content: str, created: str, updated: str, tag: List[str] = []) -> None:
        self.title = title
        self.content = content
        self.created = created
        self.updated = updated
        self.tag = tag

    def __str__(self) -> str:
        name = f'{self.title}'
        return name


class Reader:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def _parse_file(self) -> dict:
        with open(self.filename, "r") as file:
            data = file.read()
            parsed_data = xmltodict.parse(data)
            return parsed_data

    def get_notes(self) -> list:
        notes = []
        data = self._parse_file()
        notes_data = data["en-export"]["note"]
        for note in notes_data:
            del note["note-attributes"]  # breaks unpacking, not needed
            note = Note(**note)
            notes.append(note)
        return notes

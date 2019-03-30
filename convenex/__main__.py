#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click

from convenex.reader import Reader


@click.command()
@click.argument("filename")
def main(filename: str) -> None:
    """Tool for converting Evernote XML (.enex) files into Markdown (.md) files"""
    click.echo(f"Starting converting {filename}")
    reader = Reader(filename)
    notes = reader.get_notes()
    for note in notes:
        click.echo(note)

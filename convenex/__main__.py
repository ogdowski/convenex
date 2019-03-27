#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import click


@click.command()
@click.option("--file", help="Path to the file you want to convert")
def main(file):
    """Tool for converting Evernote XML (.enex) files into Markdown (.md) files"""
    click.echo(f"{file}")

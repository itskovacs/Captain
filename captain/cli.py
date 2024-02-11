#!/bin/python3
from os.path import isfile
from sys import exit as sysexit
import click
from captain.utils.formatter import logger, LOG_HANDLER
from captain.captain import Captain

CUSTOM_CONTEXT_SETTINGS = {"help_option_names": ['-h', '--help']}

@click.group(context_settings=CUSTOM_CONTEXT_SETTINGS)
def cli():
    pass


@cli.command("run", help="Run agents on the specified file")
@click.option("-v", "--verbose", "logdebug", is_flag=True, default=False,
              help="When set, set log level to debug (default: info)")
@click.option("-f", 'file', type=click.Path(), required=True, help="File to run agents on")
def run(logdebug, file):
    """Start agents on specified file"""
    logger.setLevel(10 if logdebug else 20)  # logging.DEBUG = 10, logging.INFO = 20
    LOG_HANDLER.setLevel(10 if logdebug else 20)
    if isfile(file):
        captain = Captain(file, logdebug)
        captain.run()

    else:
        logger.critical('Specified file could not be found.')
        sysexit(1)


@cli.command("agents", help="Display agents with their mission")
def display_agents():
    """Display a table describing every agent"""
    Captain.display_agents()


if __name__ == "__main__":
    cli()

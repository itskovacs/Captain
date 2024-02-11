import importlib
import pkgutil

from ..base import Base

for module in pkgutil.iter_modules(__path__):
    try:
        importlib.import_module("." + module.name, package=__name__)
    except (ImportError, AttributeError):
        raise

AGENTS = {}
for agent in Base.__subclasses__():
    AGENTS[agent.NAME.lower()] = agent


def get_enabled_agents(agents, args):
    """Retrieve agents to run, based on their metadata"""
    for agent in agents:
        # Add your other conditions here, in this if.
        # For instance: agents[agent].ACTIVATED and agents[agent].CUSTOM_VAR == my_var
        if agents[agent].ACTIVATED:
            yield agent
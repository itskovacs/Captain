from concurrent.futures import ProcessPoolExecutor
from prettytable import PrettyTable
from .utils.formatter import logger
from .agents import AGENTS, get_enabled_agents
from multiprocessing import cpu_count


def available_agents(file):
    """Retrieve agents to run"""
    # Add conditions in `agents/__init__.py in get_enabled_agents()` to filter agents
    args = {'file': file}
    return get_enabled_agents(AGENTS, args)


def deploy_agent(arg):
    """Run an agent"""
    name, _arg = arg
    agent = AGENTS[name](_arg)
    return (name, agent.run())


def prepare_agents(agent_args):
    """Spawning processes for agents"""
    if len(agent_args) == 0:
        logger.error(f'[Captain] No agent to run')
        exit(1)

    workers_cnt = len(agent_args) if len(agent_args) < cpu_count() else cpu_count()

    with ProcessPoolExecutor(max_workers=workers_cnt) as ex:
        [ex.submit(deploy_agent, arg) for arg in agent_args]  # Later monitor .result()


class Captain():
    """Captain controlling agents"""
    def __init__(self, file, loglevel):
        self.file = file
        self.loglevel = loglevel

    @staticmethod
    def display_agents():
        """Display a table describing every agent"""
        table = PrettyTable()
        table.field_names = ["Name", "Activated", "Version", "Mission"]
        table.align = "l"

        for agent in sorted(AGENTS):
            row = AGENTS[agent]
            table.add_row(
                [
                    row.NAME,
                    row.ACTIVATED,
                    row.VERSION,
                    row.MISSION
                ]
            )
        print(table)

    def run(self):
        """Run agents"""
        logger.info(f"[Captain] Deploying agents on {self.file}.")
        agents = available_agents(self.file)
        prepare_agents([[agent, self.file] for agent in agents])


import sys
from pprint import pprint

from src.config import config
from src.manager import Manager
from src.setup.systems import systems


def main():
    manager = Manager()
    mapping = manager.mapping_create(8, systems.snes.name, systems.snes.extensions)
    # manager.create_mapping(10, systems.snes.name, systems.snes.extensions, ["#Demo"])
    # manager.create_mapping(8, systems.snes.name, systems.snes.extensions)

    games = manager.mapping_calculate(mapping).new
    results = manager.mapping_games_download(mapping, games)

    # pprint(results)

if __name__ == "__main__":
    main()
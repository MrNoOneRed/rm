import sys

from src.config import config
from src.manager import Manager
from src.setup.systems import systems


def main():
    manager = Manager()
    mapping = manager.create_mapping(9, systems.snes.name, systems.snes.extensions, ["#Aftermarket"])
    # manager.create_mapping(10, systems.snes.name, systems.snes.extensions, ["#Demo"])
    # manager.create_mapping(8, systems.snes.name, systems.snes.extensions)

    manager.check_mapping(mapping)

if __name__ == "__main__":
    main()
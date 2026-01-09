import sys

from src.config import config
from src.manager import Manager
from src.setup.systems import systems


def main():
    manager = Manager()
    manager.create_mapping(9, "snes", systems.snes.extensions, ["#Aftermarket"])
    manager.create_mapping(10, "snes", systems.snes.extensions, ["#Demo"])
    manager.create_mapping(8, "snes", systems.snes.extensions)



if __name__ == "__main__":
    # if sys.argv[1] == "dev":
    #     config.base.root_path = "./data"
    # else:
    #     config.base.root_path = "/userdata"


    main()
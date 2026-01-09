import sys

from src.config import config
from src.manager import Manager


def main():
    manager = Manager()
    manager.create_mapping(9, "snes-aftermarket", ["#Aftermarket"])
    manager.create_mapping(10, "snes-demo", ["#Demo"])
    manager.create_mapping(8, "snes")



if __name__ == "__main__":
    # if sys.argv[1] == "dev":
    #     config.base.root_path = "./data"
    # else:
    #     config.base.root_path = "/userdata"


    main()
class Terminal:
    @staticmethod
    def progress_bar(title: str, offset: int, total: int, overwrite: bool = False):
        left = round((offset / total) * 100)
        right = 100 - left

        print(f"{title}[{"\u2588" * left}{"\u2591" * right}] - {left}%", end="\r" if overwrite else "\n")

from pathlib import Path


def count_files(path: str, extensions: tuple[str, ...] = None) -> int:
    path = Path(path)

    return sum(
        1 for f in path.iterdir()
        if f.is_file() and f.suffix.lower() in extensions
    )
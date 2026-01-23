import hashlib
import sys
import zipfile
from collections.abc import Callable

import zlib

from pathlib import Path
from typing import IO

from src.models.Hash import Hash


class FileManager:
    @staticmethod
    def file_count(path: str, extensions: tuple[str, ...] | None = None) -> int:
        path = Path(path)

        return sum(
            1 for f in path.iterdir()
            if f.is_file() and (extensions is None or f.suffix.lower() in extensions)
        )

    @staticmethod
    def file_hashes(path: str | Path, extensions: tuple[str, ...] | None = None, unzip: bool = True) -> Hash | None:
        file_path = Path(path)

        # ZIP
        if unzip and zipfile.is_zipfile(file_path):
            results: Hash | None = None

            with zipfile.ZipFile(file_path) as zip_ref:
                infos = zip_ref.infolist()
                files = [i for i in infos if not i.filename.endswith("/")]

                for info in files:
                    if info.is_dir() or (extensions is not None and not info.filename.lower().endswith(extensions)):
                        continue

                    with zip_ref.open(info) as f:
                        results = FileManager._file_hash(f)
                        break

            return results

        with open(file_path, "rb") as f:
            return FileManager._file_hash(f)

    @staticmethod
    def files_unzip(zip_path: str, output_dir: str, progress: Callable | None = None) -> None:
        zip_path = Path(zip_path)
        output_dir = Path(output_dir)

        if not output_dir.exists():
            raise FileNotFoundError(f"Output directory {output_dir} does not exist")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            infos = zip_ref.infolist()
            files = [i for i in infos if not i.filename.endswith("/")]
            total = sum(i.file_size for i in files)
            offset = 0

            for info in files:
                filename = Path(info.filename).name
                target_path = output_dir / filename

                with zip_ref.open(info) as src, open(target_path, "wb") as dst:
                    dst.write(src.read())

                offset += info.file_size

                if progress:
                    progress("Extracting: ", offset, total, True)

            if progress:
                progress("Extracting: ", total, total)


    @staticmethod
    def _file_hash(stream: IO[bytes], chunk_size: int = 1024 * 1024) -> Hash:
        crc = 0
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()

        while chunk := stream.read(chunk_size):
            crc = zlib.crc32(chunk, crc)
            md5.update(chunk)
            sha1.update(chunk)

        return Hash(crc=format(crc & 0xFFFFFFFF, "08x"), md5=md5.hexdigest(), sha1=sha1.hexdigest())

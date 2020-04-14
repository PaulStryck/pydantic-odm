from bson.codec_options import TypeEncoder
from pathlib import PosixPath
from typing import Any, Set, List


class PathEncoder(TypeEncoder):
    python_type = PosixPath

    def transform_python(self, value: PosixPath) -> str:
        return str(value)


class SetEncoder(TypeEncoder):
    python_type = Set

    def transform_python(self, value: Set[Any]) -> List[Any]:
        return list(value)

from bson.codec_options import TypeEncoder
from typing import Any, Set, List

class Codec(TypeEncoder):
    python_type = Set

    def transform_python(self, value: Set[Any]) -> List[Any]:
        return list(value)


codec = Codec()

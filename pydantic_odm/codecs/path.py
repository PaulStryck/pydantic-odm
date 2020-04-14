from bson.codec_options import TypeEncoder
from pathlib import PosixPath


class Codec(TypeEncoder):
    python_type = PosixPath

    def transform_python(self, value: PosixPath) -> str:
        return str(value)


codec = Codec()

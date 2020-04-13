from bson.codec_options import TypeCodec
from pathlib import PosixPath


class Codec(TypeCodec):
    python_type = PosixPath
    bson_type = str

    def transform_python(self, value: PosixPath) -> str:
        return str(value)

    def transform_bson(self, value: str) -> PosixPath:
        return PosixPath(value)


codec = Codec()

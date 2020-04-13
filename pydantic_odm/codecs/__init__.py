from typing import List

from bson.codec_options import TypeCodec

from pydantic_odm.codecs import path

all_codecs: List[TypeCodec] = [
    path.codec
]

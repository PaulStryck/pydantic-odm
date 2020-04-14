from bson.codec_options import TypeRegistry

from .encoders import (
    PathEncoder,
    SetEncoder
)

path_encoder = PathEncoder()
set_encoder = SetEncoder()
type_registry = TypeRegistry([
    path_encoder,
    set_encoder
])

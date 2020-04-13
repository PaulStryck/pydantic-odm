from bson.codec_options import TypeRegistry

from . import codecs

type_registry = TypeRegistry(codecs.all_codecs)

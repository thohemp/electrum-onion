# -*- coding: utf-8 -*-
import sys

try:
    from deeponion_x13_hash import getPoWHash
    import_success = True
    load_libx13hash = False
except ImportError:
    import_success = False
    load_libx13hash = True


if load_libx13hash:
    from ctypes import cdll, create_string_buffer, byref

    if sys.platform == 'darwin':
        name = 'libx13hash.dylib'
    elif sys.platform in ('windows', 'win32'):
        name = 'libx13hash-0.dll'
    else:
        name = 'libx13hash.so'

    try:
        lx13hash = cdll.LoadLibrary(name)
        deeponion_x13_hash = lx13hash.deeponion_x13_hash
    except:
        load_libx13hash = False


if load_libx13hash:
    hash_out = create_string_buffer(32)

    def getPoWHash(header):
        deeponion_x13_hash(header, byref(hash_out))
        return hash_out.raw

if not import_success and not load_libx13hash:
    raise ImportError('Can not import x13_hash')


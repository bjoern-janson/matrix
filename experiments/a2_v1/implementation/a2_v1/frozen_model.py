"""Load the pinned original policy boundary from verified source bytes."""
import sys
from types import ModuleType
from hashlib import sha256
from .authorities import PATHS, EXPECTED

def _load():
    data=PATHS['model'].read_bytes()
    if sha256(data).hexdigest()!=EXPECTED['model']:
        raise RuntimeError('FROZEN_MODEL_IDENTITY_MISMATCH')
    name='a2_v1._verified_v0_model'
    module=ModuleType(name)
    sys.modules[name]=module
    exec(compile(data,str(PATHS['model']),'exec'),module.__dict__)
    return module

model=_load()

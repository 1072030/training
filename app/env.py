from dotenv import load_dotenv
import os
from typing import List, TypeVar, Optional, Type
from ast import literal_eval
load_dotenv(verbose=True)
def get_env(key,default=None):
    val = os.getenv(key)
    if val is None:
        if default is not None:
            return default
    else:
        return val


ALGORITHM = get_env("ALGORITHM")

JWT_SECRET = get_env("JWT_SECRET", str)
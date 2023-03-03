from dotenv import load_dotenv
import os
from typing import List, TypeVar, Optional, Type
from ast import literal_eval
load_dotenv(verbose=True)
def get_env(key):
    val = os.getenv(key)
    return val

ALGORITHM = get_env("ALGORITHM")

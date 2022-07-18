from __future__ import division
from typing import Optional, Sequence
from dataclasses import dataclass
import enum

class hashTypes(enum.Enum):
    simpleHash = 'simpleHashFunction'
    division = 'division'
    multiplication = 'multiplication'
       
@dataclass
class HashTableInstanceArgs():
    capacity: int
    hashType: Optional[hashTypes]
    


   
    
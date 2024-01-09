#entity: return type of a function
from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)  #this is not python class but dataclass, here you can define the veriables without using self keyword.
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path


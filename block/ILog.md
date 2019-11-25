***block/ILog.py - documentation***
___

This file is used as base class for every log-type block.
It contains the base class for every log and an enum representing
the orientation of the log.

It contains at the moment no code for the "stripping" system.
This will change in the future. 


1. class LogAxis(enum.Enum)
    
    enum for orientation of the log
    
    attributes: X, Y and Z
    
2. class ILog(block.Block.Block)

    base class for every log, overwrites some existing methods
    of block.Block.Block to make log-like behaviour possible.
    
    1. def on_create(self)
    
        overwrite of super method. Will setup the log data like 
        orientation
        
    2. def get_model_state(self) -> dict
    
        overwrite of super method, will return the dict {"axis": <axis name>}
        
    3. def set_model_state(self, state: dict)
    
        overwrite of super method, will look out for the "axis"-key
        in state and set it if provided
        
    4. def get_all_model_states() -> list
    
        overwrite of super method, will return the state data for every
        of the 3 states of the log.
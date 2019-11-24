***setup.py - documentation***
___

This file is used for the prebuilding system.
For more information, see prebuilding.md.

1. line 8 - 24: simple description of the system

2. class IPrepareAbleTask(object)
    base class for every "normal" prebuild task
    
    1. def get_name() -> str
    
        abstract method for getting the name of the task
        
    2. def dump_data(directory: str)
        
        abstract method for dumping data into the build-folder
        
    3. variable bool USES_DIRECTORY
    
        if an directory should be created for these task

3. variable event.Registry.Registry taskregistry: registry for 
prebuilding tasks

4. def add()
    
    loading function for adding the tasks
    
    1. class Cleanup(setup.IPrepareAbleTask)
        
        class notated to G.registry for rebuilding. Will remove all data
        from the cache
        
        1. def get_name() -> str
        
            overwrite of super method
        
        2. def dump_data(directory: str)
        
            overwrite of super method, will remove folder
        
        3. variable bool USES_DIRECTORY = False
        
            overwrite of super variable
            
    2. class TextureFactoryGenerate(IPrepareAbleTask)
    
        class notated to G.registry for rebuilding. Will prepare
        various texture files for usage by the game
        
        WARNING: these class is "empty" and has no affect on the game
        
        1. def get_name() -> str
        
            overwrite of the super method
            
        2. def dump_data(directory: str)
        
            clear overwrite of the super method
        
        3. variable bool USES_DIRECTORY = False
        
            overwrite of super variable

5. def execute()

    will execute all registered prebuild tasks in order of registration
    
6. line 89 to 93: setup game's stuff & register to loading system
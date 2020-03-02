Mcpython provides an mod loader

It will try to load everything located in the mods-folder

You can provide pure .py files, folders and zip-archives

Loading:

- .py files are simply imported
- in folders & zip-files, an file called mod.json MUST be located. This file has in version 1.1.0 the following structure:
    
    {
        "version": "1.1.0",
        "loader": "python:default",
        "load:files": [<an list of your python files to import on beginning without .py location relative from folder base>]
    }

You can then when your python file are imported create mod.Mod.Mod-instanced giving an modname and an modversion.
The object you will get you can modify. You can add dependencies [see documentation of mod.Mod.Mod] and
subscribe to various loading events:
    \<your mod object>.eventbus.subscribe(\<loading stage name>, \<your function to call on the stage>)

You will need to subscribe to "stage:mod:init" for setting up your basic stuff, all others are optional.
For an full list of all events, see modding/loading stages.md and mod/ModLoader.md 

For advanced modders:

- I want to change an internal block/item to my own one, how to do?

    Registries support overriding existing elements when providing the same registry name. If you want to not deactivate
    cross-mod compatibility, extend your override to the registry entry before 
    
- I want to override another mod's file

    WARNING: this can end into unwanted behaviour
    
    depending on the relation between your mod and the mod you want to modify, you can register the other mod as load after me
    and simply insert the files. This might NOT work depending on some very complex effects. You may want to provide an
    extra ResourcePack in your mod which you register yourself to ResourceLocator's table. This works sadly for non-script files.
    You could also try to manipulate sys.argv to change import priority, but this on your own risk.
    
    You could also try to override the class/function/variable in runtime (python allows a lot when it goes to exchanging
    functional parts of loaded scripts).
    
    Sadly, there is NO method to access-transform stuff or to change code fragments in an function. For doing this kind of stuff,
    I can only refer to the official python wiki under https://docs.python.org/3/
    
- I want to implement an function used for sub-classes of XY

    You may want to search with hasattr function; function should start with mod name to make sure that it does not 
    override another mod's function
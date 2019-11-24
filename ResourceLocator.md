***ResourceLocator.py - documentation***
___

This file is used for accessing the resources found in the minecraft.jar
and equal folders in resourcepacks-dir

WARNING: ResourceLocator must be initialised for using. This is done in
normal \_\_main__-call, but not at direct top level.

How to add own resource locations to the index?
    
    add an object of ResourceLocator.ResourceZipFile for compressed files or 
    an object of ResourceLocator.ResourceDirectory for directories to the
    ResourceLocator.RESOURCE_LOCATIONS-list OR add an parameter called
    "--addresourcepath <path>" to the call of \_\_main__.py to automatically
    add it into the system.
    

How do mods interact with these?

    Mods are as files/folders automatically added as resource locations
    into the system. .py files are sorted out because the do NOT contain
    any resource loadable by this system. Any mod can add more resource
    locations by following above schema.

What file name formats are accepted?

- for selecting an special ResourceLocation, use 
"@\<location for resource location>|\<path>
- relative files like "assets/minecraft/textures/block/stone.png"
- special encoded files like "block/stone"
- special mod encoded files like "minecraft:block/stone"


And what is in this file?

1. line 8 - 21: description on ResourceLocator

2. class IResourceLocation(object)

    base class for every resource location class
    
    1. def is_valid(path: str) -> bool
    
        static abstract function for checking if an file/dir can be loaded
        with this IResourceLocation. Used by the resourcepack loading system
    
    2. def is_in_path(self, filename: str) -> bool
    
        abstract check function if the filename is in the location.
        used by exists and by read for checking reasons
    
    3. def read(self, filename: str, mode: str) -> object
    
        abstract method for reading an file by mode. Should raise
        ValueError if "mode" is not supported. Return type is set by
        "mode". Possible modes: 
        - None: read bytes
        - "json": read with json decoder
        - "pil": read as PIL.Image
        - "pyglet": read as pyglet image
        
    4. def close(self)
        
        abstract, not needed method for closing opened resources. Will be
        called when cleaning up after crash / game close
    
    5. def get_all_entrys_in_directory(self, directory: str) -> list
    
        abstract method os.listdir / os.walk style returning an list of
        files & directories
    
3. class ResourceZipFile(ResourceLocation.IResourceLocation)
    
    class for holding an compressed file as resource location
    
    1. def is_valid(path: str) -> bool
    
        overwrite of super method, calls zipfile.is_zipfile
        
    2. def \_\_init__(self, path: str)
    
        creates an new object of these class. Opens the compressed
        archive with zipfile
        
    3. def is_in_path(self, filename: str) -> bool
    
        overwrite of super method, checks if filename is in namelist
        
    4. def read(self, filename: str, mode: str)
    
        overwrite of super method, will read from archive
        
    5. def close(self)
    
        overwrite of super method, will close the archive
        
    6. def get_all_entrys_in_directory(self, directory: str, go_sub=False)
    
        extended overwrite of super method, will iterate over namelist
        and insert valid entries into an list which is than returned.
        
4. class ResourceDirectory(ResourceLocator.IResourceLocation)

    class for holding an directory as resource location
    
    1. def is_valid(path: str) -> bool
    
        overwrite of super method, will use os.path.isdir
    
    2. def \_\_init__(self, path: str)
    
        creates an new object of the class
        
    3. def is_in_path(self, filename: str)
    
        overwrite of the super method, will use os.path.isfile for check
        
    4. def read(self, filename: str, mode: str)
    
        overwrite of super method, will read the file in mode
        
    5. def get_all_entrys_in_directory(self, directory: str) -> list
    
        returns the result of os.listdir

5. variable list<class ResourceLocator.IResourceLocation> 
    RESOURCE_PACK_LOADERS: list of resource location loaders to use for 
    resource packs, former RESOURCE_LOADER
    
6. variable list<ResourceLocator.IResourceLocation> RESOURCE_LOCATIONS:
    list of loaded resource locations to read files from
    
7. def load_resource_packs()
    
    former load_resources(), will load all valid files & directories in
    resourepacks-folder
    
8. def close_all_resources()

    will close all IResourceLocations in (6)
    
9. variable list<str> MC_IMAGE_LOCATIONS: an list of locations under
    "assets/minecraft/textures" which should be arrival by 
    "<space>/<path>", used for custom file format
    
10. def transform_name(file: str) -> str
    
    will transform the filename into an file as in format 2 from format
    3 or 4
    
11. def exists(file, transform=True)

    returns if the file is in any resource location. For that, on every
    resource location in (6) the function is_in_path will be called.
    when transform is True, it will try to call (10) if not found on
    filename and than check again
    
12. def read(file, mode=None)

    will read an file from first resource location found by mode
    
13. def get_all_entries(directory: str) -> list

    will return an list of distinct entries found in directory
    
14. def get_all_entries_special(directory: str) -> list
    
    like (13), but returns no distinct list. Instead, all found files in
    format 1
    
15. def add_resources_by_modname(modname, pathname)
    
    Helper function for mods. Will notate all default locations for an
    mod to the loading system
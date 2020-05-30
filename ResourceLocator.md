***ResourceLocator.py - documentation - last updated on 30.5.2020 by uuk***
___

    specifications for the resource loader system
    On startup / on reload, so called ResourceLocations are created for every archive / directory in resourcepack-folder
    functions to access data:
        to_filename(representation: str) -> str: returns the transformed name (for example block/dirt gets 
            assets/minecraft/textures/block/dirt.png)
        exists(filename: str) -> bool: returns if an directory exists somewhere
        read(filename: str, mode=select from None for bytes, "json", "pil", "pyglet") -> object: loads the file
    How mods do interact with these?
        Mod files are automatically added to these system to make it easier to add own resources


    class IResourceLocation
        
        base class for an class holding an link to an resource system


        static
        function is_valid(path: str) -> bool
            
            checks if an location is valid as an source
            :param path: the path to check
            :return: if it is valid or not


        function is_in_path(self, filename: str) -> bool
            
            checks if an local file-name is in the given path
            :param filename: the file name to check
            :return: if it is in the path


        function read(self, filename: str, mode: str)
            
            will read an file into the system
            :param filename: the file name to use
            :param mode: the mode to use
            :return: the content of the file loaded in the correct mode


        function close(self)
            
            implement if you need to close an resource on end


        function get_all_entries_in_directory(self, directory: str) -> list
            
            should return all entries in an local directory
            :param directory: the directory to check
            :return: an list of data
            todo: make generator


    class ResourceZipFile extends IResourceLocation
        
        implementation for archives


        static
        function is_valid(path: str) -> bool

        function __init__(self, path: str)

            variable self.archive

            variable self.path

        function is_in_path(self, filename: str) -> bool

        function read(self, filename: str, mode: str)

        function close(self)

        function get_all_entries_in_directory(self, directory: str, go_sub=True) -> list

    class ResourceDirectory extends IResourceLocation
        
        implementation for raw directories


        static
        function is_valid(path: str) -> bool

        function __init__(self, path: str)

            variable self.path

        function is_in_path(self, filename: str) -> bool

        function read(self, filename: str, mode: str)

        function get_all_entries_in_directory(self, directory: str) -> list

    variable RESOURCE_PACK_LOADERS - data loaders for the resource locations

    variable RESOURCE_LOCATIONS - an list of all resource locations in the system

    function load_resource_packs()
        
        will load the resource packs found in the paths for it


    function close_all_resources()
        
        will close all opened resource locations


    variable MC_IMAGE_LOCATIONS - how mc locations look like

    function transform_name(file: str) -> str
        
        will transform an MC-ResourceLocation string into an local path
        :param file: the thing to use
        :return: the transformed
        :raises NotImplementedError: when the data is invalid


    function exists(file: str, transform=True)
        
        checks if an given file exists in the system
        :param file: the file to check
        :param transform: if it should be transformed for check
        :return: if it exists or not


    function read(file: str, mode: typing.Union[None, str] = None)
        
        will read the content of an file
        :param file: the file to load
        :param mode: the mode to load in, or None for binary
        :return: the content


    function get_all_entries(directory: str) -> list
        
        will get all files & directories [ending with an "/"] of an given directory across all resource locations
        :param directory: the directory to use
        :return: an list of all found files
        todo: make return an generator


    function get_all_entries_special(directory: str) -> list
        
        returns all entries found with their corresponding '@[path]:file'-notation
        :param directory: the directory to searc from
        :return: an list of found resources
        todo: make use an generator


    function add_resources_by_modname(modname, pathname=None)
        
        loads the default data locations into the system for an given namespace
        :param modname: the name of the mod for the loading stages
        :param pathname: the namespace or None if the same as the mod name

***ResourceLocator.py - documentation - last updated on 16.5.2020 by uuk***
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

        static function is_valid(path: str) -> bool

        function is_in_path(self, filename: str) -> bool

        function read(self, filename: str, mode: str)

        function close(self)

        function get_all_entries_in_directory(self, directory: str) -> list

    class ResourceZipFile extends IResourceLocation

        static function is_valid(path: str) -> bool

        function __init__(self, path: str)

            variable self.archive

            variable self.path

        function is_in_path(self, filename: str) -> bool

        function read(self, filename: str, mode: str)

        function close(self)

        function get_all_entries_in_directory(self, directory: str, go_sub=True) -> list

    class ResourceDirectory extends IResourceLocation

        static function is_valid(path: str) -> bool

        function __init__(self, path: str)

            variable self.path

        function is_in_path(self, filename: str) -> bool

        function read(self, filename: str, mode: str)

        function get_all_entries_in_directory(self, directory: str) -> list

    variable RESOURCE_PACK_LOADERS

    variable RESOURCE_LOCATIONS

    function load_resource_packs()

    function close_all_resources()

    variable MC_IMAGE_LOCATIONS

    function transform_name(file: str) -> str

    function exists(file, transform=True)

    function read(file, mode=None)

    function get_all_entries(directory: str) -> list

    function get_all_entries_special(directory: str) -> list
        
        returns all entries found with their corresponding '@[path]:file'-notation
        :param directory: the directory to searc from
        :return: an list of found resources


    function add_resources_by_modname(modname, pathname=None)
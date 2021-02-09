***ResourceLoader.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


        class PIL_Image

            class Image

            static
            function open(cls, file: str)
    
    specifications for the resource loader system
    On startup / on reload, so called ResourceLocations are created for every archive / directory in resourcepack-folder
    functions to access data:
        to_filename(representation: str) -> str: returns the transformed name (for example block/dirt gets 
            assets/minecraft/textures/block/dirt.png)
        exists(filename: str) -> bool: returns if an directory exists somewhere
        read(filename: str, mode=select from None for bytes, "json", "pil", "pyglet") -> object: loads the file
    How mods do interact with these?
        Mod files are automatically added to these system to make it easier to add own resources


    class IResourceLoader extends ABC
        
        Base class for an class holding an link to an resource source, like and directory or zip-file


        static
        function is_valid(path: str) -> bool
            
            checks if an location is valid as an source
            :param path: the path to check
            :return: if it is valid or not


        function get_path_info(self) -> str

        function is_in_path(self, path: str) -> bool
            
            checks if an local file-name is in the given path
            :param path: the file path to check
            :return: if it is in the path


        function read_raw(self, path: str) -> bytes
            
            will read an file into the system in binary mode
            :param path: the file name to use
            :return: the content of the file loaded in binary


        function read_image(self, path: str) -> PIL_Image.Image
            
            will read an file into the system as an PIL_Image.Image
            :param path: the file name to use
            :return: the content of the file loaded as image


        function read_decoding(self, path: str, encoding: str) -> str
            
            will read an file into the system as an string
            :param path: the file name to use
            :param encoding: the encoding to use
            :return: the content of the file loaded as string


        function close(self)
            
            Called when the resource path should be closed


        function get_all_entries_in_directory(
                self, directory: str, go_sub=True
                ) -> typing.Iterator[str]:
            
            Should return all entries in an local directory
            :param directory: the directory to check
            :param go_sub: if sub directories should be iterated or not
            :return: an list of data


    class ResourceZipFile extends IResourceLoader
        
        Implementation for zip-archives


        static
        function is_valid(path: str) -> bool

        function __init__(self, path: str)

            variable self.archive

            variable self.path

            variable self.namelist_cache

        function get_path_info(self) -> str

        function is_in_path(self, filename: str) -> bool

        function read_raw(self, path: str) -> bytes

        function read_image(self, path: str) -> PIL_Image.Image

        function close(self)

        function get_all_entries_in_directory(
                self, directory: str, go_sub=True
                ) -> typing.Iterator[str]:

        function __repr__(self)

    class ResourceDirectory extends IResourceLoader
        
        Implementation for raw directories


        static
        function is_valid(path: str) -> bool

        function __init__(self, path: str)

            variable self.path

        function get_path_info(self) -> str

        function is_in_path(self, filename: str) -> bool

        function read_raw(self, path: str) -> bytes

        function read_image(self, path: str) -> PIL_Image.Image

        function get_all_entries_in_directory(
                self, directory: str, go_sub=True
                ) -> typing.Iterator[str]:

                    variable file

                    variable file

        function __repr__(self)

    class SimulatedResourceLoader extends IResourceLoader
        
        In-memory resource loader instance


        variable SIMULATOR_ID

        function __init__(self)

            variable self.raw

            variable self.images

            variable self.id

        function provide_raw(self, name: str, raw: bytes)

        function provide_image(self, name: str, image: PIL_Image.Image)

        static
        function is_valid(path: str) -> bool

        function get_path_info(self) -> str

        function is_in_path(self, path: str) -> bool

        function read_raw(self, path: str) -> bytes

        function read_image(self, path: str) -> PIL_Image.Image

        function close(self)

        function get_all_entries_in_directory(
                self, directory: str, go_sub=True
                ) -> typing.Iterator[str]:

            variable yielded_directories

                        variable d

    variable RESOURCE_PACK_LOADERS

    variable RESOURCE_LOCATIONS - an list of all resource locations in the system

    function load_resource_packs()
        
        will load the resource packs found in the paths for it


                variable file

                variable flag

                        variable flag

        variable i

            variable element

                variable path

    function close_all_resources()
        
        will close all opened resource locations


    variable MC_IMAGE_LOCATIONS

    function transform_name(file: str, raise_on_error=True) -> str
        
        will transform an MC-ResourceLocation string into an local path
        :param file: the thing to use
        :return: the transformed
        :param raise_on_error: will raise downer exception, otherwise return the file iself
        :raises NotImplementedError: when the data is invalid


                variable f

                variable f

    function exists(file: str, transform=True)
        
        checks if an given file exists in the system
        :param file: the file to check
        :param transform: if it should be transformed for check
        :return: if it exists or not


            variable data

            variable resource

            variable file

    function read_raw(file: str)
        
        will read the content of an file in binary mode
        :param file: the file to load
        :return: the content


            variable data

            variable resource

            variable file

                variable file

            variable file

        variable loc

    function read_image(file: str)
        
        will read the content of an file in binary mode
        :param file: the file to load
        :return: the content


            variable data

            variable resource

            variable file

                variable file

            variable file

        variable loc

    function read_json(file)

    function read_pyglet_image(file)

    function get_all_entries(directory: str) -> typing.Iterator[str]
        
        Will get all files & directories [ending with an "/"] of an given directory across all resource locations
        :param directory: the directory to use
        :return: an list of all found files


    function get_all_entries_special(directory: str) -> typing.Iterator[str]
        
        Returns all entries found with their corresponding '@<path>:<file>'-notation
        :param directory: the directory to search from
        :return: an list of found resources

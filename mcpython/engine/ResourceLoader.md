***ResourceLoader.py - documentation - last updated on 28.12.2021 by uuk***
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
                function open(cls, file: str | io.BytesIO)
    
    ---------------------------------------------
    Specifications for the resource loader system
    ---------------------------------------------
    On startup / on reload, so called ResourceLocation's are created for every archive / directory in resourcepack-folder
    and other asset sources (mod files)
    functions to access data:
        to_filename(representation: str) -> str: returns the transformed name (for example block/dirt gets 
            assets/minecraft/textures/block/dirt.png)
        exists(filename: str) -> bool: returns if an directory exists somewhere
        read_<xy>(filename: str) -> object: loads the file in the speicified mode
    How mods do interact with these?
        Mod files are automatically added to these system to make it easier to add own resources
    There is a special class for simulating files in-memory 


    class IResourceLoader extends ABC
        
        Base class for a class holding a link to a resource source, like and directory or zip-file
        (but in theory can be anything, even over network)


        static
        function is_valid(path: str) -> bool
            
            Checks if a location is valid as a source to load via the constructor
            :param path: the path to check
            :return: if it is valid or not


        function get_path_info(self) -> str
            
            Returns a unique identifier for this loader, like a path loaded from, or some mod name

            
            Checks if a local file-name is in the given path, so it can be loaded
            :param path: the file path to check
            :return: if it is in the path

            
            Will read a file in binary mode
            :param path: the file name to use
            :return: the content of the file loaded in binary

            
            Will read a file as a PIL.Image.Image
            :param path: the file name to use
            :return: the content of the file loaded as image


            variable data
            
            Will read a file into the system as a string, decoding the raw bytes in the given encoding
            :param path: the file name to use
            :param encoding: the encoding to use
            :return: the content of the file loaded as string


        function close(self)
            
            Called when the resource path should be closed
            Should be used for cleanup


        function get_all_entries_in_directory(
                self, directory: str, go_sub=True
                ) -> typing.Iterator[str]:
            
            Should return all entries in a local directory
            :param directory: the directory to check
            :param go_sub: if sub directories should be iterated or not
            :return: a list of data
            todo: add a regex variant


    class ResourceZipFile extends IResourceLoader
        
        Implementation for zip-archives


        static
        function is_valid(path: str) -> bool

        function __init__(self, path: str, close_when_scheduled=True)

            variable self.archive

            variable self.path

            variable self.namelist_cache

            variable self.close_when_scheduled

        function get_path_info(self) -> str

            variable data

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

                variable path

                variable data: bytes

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

        function debug_dump(self, directory: str)

                variable file

                variable d

        function provide_raw(self, name: str, raw: bytes)

            variable self.raw[name]

        function provide_image(self, name: str, image: PIL_Image.Image)

        static
        function is_valid(path: str) -> bool

        function get_path_info(self) -> str

        function close(self)

        function get_all_entries_in_directory(
                self, directory: str, go_sub=True
                ) -> typing.Iterator[str]:

            variable yielded_directories

                        variable d

    variable RESOURCE_PACK_LOADERS
        data loaders for the resource locations, SimulatedResourceLoader is not a default loader

    variable RESOURCE_LOCATIONS - a list of all resource locations in the system

    function load_resource_packs()
        
        Will load the resource packs found in the paths for it
        todo: add a way to add resource locations persistent to reloads


                variable file

                variable flag

                        variable flag

        variable i

            variable element

                variable path

    function close_all_resources()
        
        Will close all opened resource locations using <locator>.close()
        Will call the resource:close event in the process


    variable MC_IMAGE_LOCATIONS
        how mc locations look like
        
        Will transform an MC-ResourceLocation string into a local path
        :param file: the thing to use
        :return: the transformed
        :param raise_on_error: will raise downer exception, otherwise return the file name
        :raises NotImplementedError: when the data is invalid


        variable f

                variable f

                variable f
        
        Checks if a given file exists in the system
        :param file: the file to check
        :param transform: if it should be transformed for check
        :return: if it exists or not


            variable file

            variable data

            variable resource

            variable file
        
        Will read the content of a file in binary mode
        :param file: the file to load
        :return: the content


            variable file

            variable data

            variable resource

            variable file

                variable file

            variable file

        variable loc
        
        Will read the content of a file in binary mode
        :param file: the file to load
        :return: the content


            variable file

            variable data

            variable resource

            variable file

                variable file

                variable file

                variable file

        variable loc
        
        Reads a .json file from the system


            variable data
        
        Will get all files & directories [ending with an "/"] of an given directory across all resource locations
        :param directory: the directory to use
        :return: a list of all found files


        variable loc
        
        Returns all entries found with their corresponding '@<path>:<file>'-notation
        :param directory: the directory to search from
        :return: a list of found resources

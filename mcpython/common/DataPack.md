***DataPack.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class DatapackLoadException extends Exception

    class DataPackStatus extends enum.Enum
        
        Enum for the loading-status of an data-pack


        variable INACTIVE - status for every new created datapack

        variable ACTIVATED - the datapack is active

        variable DEACTIVATED - the datapack is deactivated (by the user)

        variable ERROR - the datapack has an error in it and can not be loaded for that reason

        variable UNLOADED - the datapack was unloaded and must be loaded before usage

        variable SYSTEM_ERROR - during loading the datapack, an internal error occurred. This datapack can't be used anymore

    class DataPackHandler
        
        Handler for datapacks


        function __init__(self)

            variable self.loaded_data_packs

        function schedule_datapack_load(self)
            
            Will load all data packs in the default locations and call an event for
            subsequent systems to register them (datapack:search)
            WARNING: this function is called also on each reload


        function load_datapack_from_directory(self, directory: str, raise_on_error=False) -> typing.Optional["DataPack"]
            
            Will try to load the data pack in the given directory/file
            :param directory: the directory or file to load from
            :param raise_on_error: if a DatapackLoadException should be raised on error


        function reload(self)
            
            Reloads all loaded data packs
            todo: look out for new ones at special locations


                        variable datapack.status

        function cleanup(self)
            
            Removes all data packs from the system
            Used during reload for cleaning the list of datapacks


        function try_call_function(
                self,
                name: str,
                info: mcpython.server.command.CommandParser.ParsingCommandInfo = None,
                ):
            
            Will try to invoke a function in a datapack
            :param name: the name of the function, e.g. "minecraft:test"
            :param info: the info-object to use; when None, one is constructed for this
            WARNING: will only invoke ONE function/tag from the datapacks, not all


                variable info

                    variable tag

    variable datapack_handler

    class DataPack
        
        Class for a single data pack


        function __init__(self, directory: str)
            
            Will create a new DataPack-object
            :param directory: where the datapack is located


            variable self.directory

            variable self.function_table

            variable self.status

            variable self.name

            variable self.access

            variable self.description

        function load(self)
            
            Will load the data pack


        function unload(self)
            
            Will unload the datapack


        function set_status(self, status: DataPackStatus)
            
            Sets the status of the data pack
            :param status: the status to set

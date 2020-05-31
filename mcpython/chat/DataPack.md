***DataPack.py - documentation - last updated on 6.6.2020 by uuk***
___

    class DataPackStatus extends enum.Enum
        
        Enum for the loading-status of an data-pack


        variable INACTIVE - status for every new created datapack

        variable ACTIVATED - the datapack is active

        variable DEACTIVATED - the datapack is deactivated (by the user)

        variable ERROR - the datapack has an error in it and can not be loaded for that reason

        variable UNLOADED - the datapack was unloaded and must be loaded before usage

        variable SYSTEM_ERROR - during loading the datapack, an internal error occurred. This datapack can't be used anymore

    class DataPackHandler
        
        handler for data packs


        function __init__(self)

            variable self.data_packs

        function _load(self)
            
            will load all data packs


        function _load_datapack(self, directory: str)
            
            will load an given data pack
            :param directory: the directory to load from


        function reload(self)
            
            reloads all data packs


        function cleanup(self)
            
            removes all data packs from the system


        function try_call_function(self, name: str, info=None)
            
            will try to invoke an function in an datapack
            :param name: the name of the function
            :param info: the info-object to use
            WARNING: will only invoke ONE function/tag from the datapacks, not all


    variable datapackhandler

    class DataPack
        
        class for an single data pack


        function __init__(self, directory: str)
            
            will create an new DataPack-object
            :param directory: where the datapack is located


            variable self.directory

            variable self.function_table

            variable self.status

            variable self.name

            variable self.access

            variable self.description

        function load(self)
            
            will load the data pack


        function unload(self)
            
            will unload the datapack


        function set_status(self, status: DataPackStatus)
            
            sets the status of the data pack
            :param status: the status to set

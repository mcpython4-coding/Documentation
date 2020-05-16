***DataPack.py - documentation - last updated on 16.5.2020 by uuk***
___

    class DataPackStatus extends enum.Enum

        variable INACTIVE - status for every new created datapack

        variable ACTIVATED - the datapack is active

        variable DEACTIVATED - the datapack is deactivated (by the user)

        variable ERROR - the datapack has an error in it and can not be loaded for that reason

        variable UNLOADED - the datapack was unloaded and must be loaded before usage

        variable SYSTEM_ERROR - during loading the datapack, an internal error occurred. This datapack can't be used anymore

    class DataPackHandler

        function __init__(self)

            variable self.data_packs

        function _load(self)

        function _load_datapack(self, directory)

        function reload(self)

        function cleanup(self)

        function try_call_function(self, name: str, info=None)

    variable datapackhandler

    class DataPack

        function __init__(self, directory: str)

            variable self.directory

            variable self.function_table

            variable self.status

            variable self.name

            variable self.access

            variable self.description

        function load(self)

        function unload(self)

        function set_status(self, status: DataPackStatus)
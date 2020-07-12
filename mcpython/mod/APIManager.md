***APIManager.py - documentation - last updated on 12.7.2020 by uuk***
___

    class APIManager
        
        Simple way of handling API's for different mods.
        Any mod shipping an API should call manager.addAPIType(<name>).registerAPIShipment(<name>, <module of your api>, <version of the api>)
        The mod the api is for should call  manager.addAPIType(<name>).registerAPIImplementation(<name>, <module of your api>, <version of the api>, *<extra compatible versions>)
        The system will auto-detect any incompatibility and stop mod loading when needed.
        WARNING: do NOT ly about your api version. It will only load ONE api file of each version if the api implementation is not provided. So you may end up
            using the code of another's mod
        WARNING: if an api-implementing mod is present, all packages are re-linked there (if the api is compatible).
        The system will auto-add an IS_IMPLEMENTED-flag into every API file set to if the implementing mod is provided
        The system will auto-add an API_VERSION representing the API version of the file
        Use than to retrieve the API module the following:
            manager.getAPI(<name>, <version>)
        It will auto-import the needed file. Do not directly import it!!!!


        function __init__(self)

            variable self.apis

            variable self.api_shipments

            variable self.api_implementations

            variable self.api_cache

        function addAPIType(self, name: str)
            
            Will add an new API name into the system
            :param name: the name of the api


        function isAPIProvided(self, name)

        function registerAPIShipment(self, name: str, module: str, version: tuple)

        function registerAPIImplementation(self, name: str, module: str, version: tuple, *compatible_versions)

        function getAPI(self, name: str, version: tuple)

        function check_compatibility_and_load(self)

    variable manager
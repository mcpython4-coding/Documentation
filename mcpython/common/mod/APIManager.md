***APIManager.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class APIManager
        
        Simple way of handling API's for different mods.
        Any mod shipping an API should call manager.addAPIType(<name>).registerAPIShipment(<name>, <module of your api>, <version of the api>)
        The mod the api is for should call  manager.addAPIType(<name>).registerAPIImplementation(<name>, <module of your api>, <version of the api>, *<extra compatible versions>)
        The system will auto-detect any incompatibility and stop mod loading when needed.
        WARNING: do NOT ly about your api version. It will only load ONE api file of each version if the api implementation is not provided. So you may end up
            using the code of another's mod
        WARNING: if an api-implementing mod is present, all packages are re-linked there (if the api is compatible).
        WARNING: DO NOT SHIP AN IMPLEMENTATION FOR AN API FOR ANOTHER MOD! THIS WILL CAUSE REAL PROBLEMS WITH HANDLING THE STUFF IN THE BACKGROUND!
        The system will auto-add an IS_IMPLEMENTED-flag into every API file set to if the implementing mod is provided
        The system will auto-add an API_VERSION representing the API version of the file
        Use than to retrieve the API module the following:
            manager.getAPI(<name>, <version>)
        It will auto-import the needed file. Do not directly import it!!!!
        MDK setup (plans):
            - MDK setup can be based on an list of API's which are injected into IDE and read. Compiled in minimum code features.
            - MDK should auto-generate API annotations
            - MDK should be compiled to an mod-zip-file without documentation, etc
            - MDK should be able to compile against source's, api's and compiled mod's
            - MDK should do compile code with some configuration files for reading information
            todo: is there an way that we can define the result of "mcpython.mod.APIManager.manager.getAPI(...)" as an special file? Currently,
                the IDE is not able to detect the api content otherwise.


        function __init__(self)

            variable self.apis - list of api names

            variable self.api_shipments

            variable self.api_implementations

            variable self.api_cache

        function add_api_type(self, name: str)
            
            Will add an new API name into the system
            :param name: the name of the api


        function is_api_provided(self, name)

        function register_api_shipment(self, name: str, module: str, version: tuple)

        function register_api_implementation(
                self, name: str, module: str, version: tuple, *compatible_versions
                ):

            variable self.api_implementations[name]

        function get_api(self, name: str, version: tuple)

        function check_compatibility_and_load(self)

    variable manager

    class ImplementableFeature
        
        API internal class holding an function which is not implemented in the API, but is part of it as an reference.
        Can be configured to not raise an exception when not implemented


        function __init__(self, raises_exception_on_not_implemented=True, return_value=None)

            variable self.implementation_function

            variable self.raises_exception

            variable self.return_value

        function __call__(self, *args, **kwargs)

        function implementation(self, function: typing.Callable)
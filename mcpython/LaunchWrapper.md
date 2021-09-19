***LaunchWrapper.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class LaunchWrapper
        
        Class for launching the game in a certain configuration
        Loads all needed part and executed the loading task cycle.


        function __init__(self)

            variable self.is_client

            variable self.launch_config

            variable shared.launch_wrapper

        function check_py_version(self)

        function set_client(self)

        function set_server(self)

        function full_launch(self)
            
            Method to launch everything at ones
            General layout:
            - logger & header
            - argv
            - modloader file lookup
            - modloader file information lookup
            - modloader loader lookup
            - modloader mixin parse


            variable shared.IS_CLIENT

                variable shared.CLIENT_NETWORK_HANDLER

                variable shared.SERVER_NETWORK_HANDLER

        function parse_argv(self)

                variable shared.ENABLE_MOD_LOADER

                variable shared.ENABLE_DATAPACK_LOADER

                variable shared.ENABLE_RESOURCE_PACK_LOADER

            variable current_arg: typing.Optional[str]

            variable arg_collector: typing.List[str]

                    variable current_arg

                    variable self.launch_config[e.removeprefix("-")]

                    variable current_arg

        function is_flag_arrival(self, flag: str)

        function get_flag_status(self, flag: str, default=None)

        function setup(self)
            
            Setup general stuff which does not take long to complete
            Loads first modules into memory and launches registry setup


        function setup_registries(self)
            
            Helper functions for loading the modules which create registries and do similar stuff


            @shared.mod_loader("minecraft", "special:exit")
            function exit()

        function setup_opengl(self)
            
            Helper function for OpenGL setup
            Loads also the needed API
            todo: move more rendering setup code here


        function print_header(self)
            
            Prints an header describing the program name and its version
            todo: include some more information about the system


            variable version

        function setup_files(self)
            
            Setup for certain files in the system.


                variable shared.invalidate_cache

        function launch(self)
            
            Launches the game in the current configuration
            Starts the main cycle with pyglet
            Loads the mods (finally!)
            todo: move state selection here


            variable shared.world

        function error_clean(self)
            
            Helper function for cleaning up in an half-inited environment
            (save)
            Will enforce cleanup when possible


        function clean(self)
            
            Helper function for normal cleanup (not save, will hard-crash in some cases)
            MAY crash on non-fully stable systems
            Also invokes the event for closing the game, stops the world generation process, ...

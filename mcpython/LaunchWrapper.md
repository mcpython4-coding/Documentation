***LaunchWrapper.py - documentation - last updated on 22.5.2021 by uuk***
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

            variable self.__side_prepared

        function prepare_client(self)
            
            Prepares a client setup
            Sets up the OpenGL driver backend
            Spawns a window


            variable self.__side_prepared

            variable shared.IS_CLIENT

            variable shared.NO_WINDOW

            variable shared.CLIENT_NETWORK_HANDLER

        function prepare_server(self)
            
            Prepares a sever
            Spawns a fake "window"
            WARNING: currently, also initializes the OpenGL driver


            variable self.__side_prepared

            variable shared.IS_CLIENT

            variable shared.NO_WINDOW

            variable shared.SERVER_NETWORK_HANDLER

        function inject_sys_argv(self, argv: typing.List[str])
            
            Helper function for loading the sys.argv config into the game
            todo: all sys.argv parsing belongs here, with a general parser for options not specified


                    variable shared.ENABLE_MOD_LOADER

                    variable shared.ENABLE_DATAPACK_LOADER

                    variable shared.ENABLE_RESOURCE_PACK_LOADER

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

        function load_mods(self)
            
            Do ModLoader initial stuff
            Looks for mods in the path only when shared.ENABLE_MOD_LOADER is True


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

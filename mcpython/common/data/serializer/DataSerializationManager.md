***DataSerializationManager.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class DataSerializationService extends  mcpython.common.data.abstract.AbstractFileWalkingReloadListenerInstanceBased 
        
        Special system for wrapping ISerializer's around ReloadListener's


        function __init__(
                self,
                name: str,
                path_group: typing.Union[str, re.Pattern],
                data_deserializer=None,
                data_serializer=None,
                re_run_on_reload=False,
                on_bake=None,
                on_dedicated_server=True,
                ):
            
            Constructor of the Service
            :param name: the name of the serializer
            :param path_group: the path group to use, as a Pattern-able or a re.Pattern
            :param data_deserializer: a data deserializer taking binary data and outputting some cool stuff for later use
            :param data_serializer: the other way round
            :param re_run_on_reload: re-load stuff when not on first load?
            :param on_bake:
            :param on_dedicated_server: run on dedicated server


            variable self.name

            variable self.PATTERN

            variable self.path_group

            variable self.serializer: typing.List[typing.Type[ISerializer]]

            variable self.on_deserialize

            variable self.on_unload

            variable self.data_deserializer

            variable self.data_serializer

            variable self.re_run_on_reload

            variable self.on_bake

            variable self.on_dedicated_server

        function register_listener(self)

        function register_serializer(self, serializer: typing.Type[ISerializer])

        function on_reload(self, is_first_load=False)

        function load_file(self, file: str, is_first_load=False)

                    variable data

                        variable obj

        function on_unload(self)
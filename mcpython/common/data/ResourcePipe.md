***ResourcePipe.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ResourcePipeHandler

        function __init__(self)

            variable self.reload_handlers

            variable self.bake_handlers

            variable self.data_processors

            variable self.listeners: typing.List[typing.Type[AbstractReloadListener]]

        function register_listener(self, listener: typing.Type[AbstractReloadListener])
            
            Used internally to add new namespaces to the loading system


                variable namespace

        function register_mapper(
                self,
                mapper: typing.Callable[[str, str], None | typing.Awaitable],
                on_dedicated_server=True,
                ):
            
            To use in "stage:resources:pipe:add_mapper"


        function register_reload_listener(self, listener)

        function register_bake_listener(self, listener)

        function register_data_processor(self, listener)

    variable handler

    function load()
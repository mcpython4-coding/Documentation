***ResourcePipe.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    function recipe_mapper(modname, pathname)

    function model_mapper(modname, pathname)

    function tag_mapper(modname, pathname)

    function language_mapper(modname, pathname)

    function loot_table_mapper(modname, pathname)

    class ResourcePipeHandler

        function __init__(self)

            variable self.reload_handlers

            variable self.bake_handlers

        function register_for_mod(self, providing_mod: str, namespace: str = None)
            
            Used internally to add new namespaces to the loading system


        function register_mapper(
                self, mapper: typing.Callable[[str, str], None], on_dedicated_server=True
                ):
            
            To use in "stage:resources:pipe:add_mapper"


        function register_reload_listener(self, listener)

        function register_bake_listener(self, listener)

        function reload_content(self)

    variable handler

    function load()
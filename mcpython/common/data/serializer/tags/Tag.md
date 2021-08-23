***Tag.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Tag
        
        Class holding a single tag
        Simply is an intelligent list/set structure
        At its own does nothing, loading occurs from the tag handler


        function __init__(self, master, name: str, entries: typing.List[str] = None)
            
            Will create a new tag instance from an list of entries
            :param master: the tag group to use; Use None if not used
            :param name: the name of the tag
            :param entries: the entries to use, or None if empty


            variable self.entries

            variable self.master

            variable self.name

            variable self.load_tries

        function get_dependencies(self) -> typing.List[str]
            
            Will return a list of tags these tag links to
            todo: use some dependency resolving for the order of inits


        function build(self)
            
            Will build the tag


                        variable self.entries
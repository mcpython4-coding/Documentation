***Tag.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class Tag
        
        class holding an single tag


        static
        function from_data(master, tagname: str, data: dict)
            
            will create an new tag from data
            :param master: the group to use
            :param tagname: the name of the tag
            :param data: the data to use
            :return the tag instance


        function __init__(self, master, name: str, entries: list)
            
            will create an new tag instance from an list of entries
            :param master: the tag group to use
            :param name: the name of the tag
            :param entries: the entries to use


            variable self.entries

            variable self.master

            variable self.name

            variable self.load_tries

        function get_dependencies(self) -> list
            
            will return an list of tags these tag links to
            :return the list


        function build(self)
            
            will build the tag

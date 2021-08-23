***TagGroup.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class TagGroup
        
        class for holding an group of tags. e.g. all items


        function __init__(self, name: str)
            
            creates an new tag group
            :param name: the name of the group


            variable self.name

            variable self.tags

            variable self.cache

        function add_from_data(self, name: str, data: dict, replace=True)
            
            Will insert more data into the tag system
            :param name: the tag name to set
            :param data: the data to inject
            :param replace: if the existing tag should be removed
            :return:


        function build(self)
            
            Will "build" the tag group


        function get_tags_for(self, obj: str, cache=False) -> typing.List[str]
            
            Will return all tags for an given object
            :param obj:
            :param cache: if data should be cached


        function provides_object_tag(self, obj: str, tag_name: str) -> bool
            
            Checks if the object has an given tag
            :param obj: the object to check
            :param tag_name: the tag to check for


        function provides_object_tags(self, obj: str, tags: typing.List[str]) -> bool
            
            Returns if the given object is in all of the given tag names
            :param obj: the object to check
            :param tags: the list of tag names to check


        function provides_object_any_tag(self, obj: str, tags: typing.List[str]) -> bool
            
            Returns if the given object is in any of the given tag names
            :param obj: the object to check
            :param tags: the list of tag names to check

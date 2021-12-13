***TagHandler.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class TagHandler
        
        Handler for handling tags


        function __init__(self)
            
            Creates an new TagHandler instance


            variable self.tag_groups - name -> tag group

            variable self.tag_locations

        function from_data(self, tag_group: str, tag_name: str, data: dict, replace=True)
            
            Will inject certain data
            :param tag_group: the group to use
            :param tag_name: the name of the tag
            :param data: the data to inject
            :param replace: if data should be replaced or not
            :return:


        function add_locations(self, locations: list)
            
            Will add possible tag locations for later loading
            :param locations: the locations to add

            
            Will reload all tag-related data

            
            Will load the tags
            :param direct_call: if build now or in the loading stage for it


                        variable data

                    variable s

                    variable modname

                    variable name - }:{}".format(

        function get_tag_for(
                self, name: str, group: str, or_else_none=False
                ) -> typing.Optional[mcpython.common.data.serializer.tags.Tag.Tag]:
            
            Will return the tag by name and group
            :param name: the name to use
            :param group: the group to use
            :param or_else_none: return None if tag not found?
            :return: the tag instance
            :raises ValueError: when the tag is not found


        function get_entries_for(self, name: str, group: str) -> typing.List[str]
            
            Will return the tag by name and group
            :param name: the name to use
            :param group: the group to use
            :return: the tag instance


        function get_tags_for_entry(
                self, identifier: str, group: str
                ) -> typing.List[mcpython.common.data.serializer.tags.Tag.Tag]:
            
            Will return an list of all tag instances these instance does occur in
            :param identifier: the identifier to search for
            :param group: the group to search in
            :return: an list of Tag-instances


            variable taglist

        function has_entry_tag(self, identifier: str, group: str, tag_name: str) -> bool
            
            Check if an given tag has an entry in it
            :param identifier: the entry to check
            :param group: the group to check for
            :param tag_name: the tag name to check for
            :return: if the identifier is in the given tag


    variable shared.tag_handler
        
        Adds tags from an given scope for an given namespace where loc is the name of the namespace
        :param loc: the namespace
        WARNING: when adding outside normal build period, errors may occur

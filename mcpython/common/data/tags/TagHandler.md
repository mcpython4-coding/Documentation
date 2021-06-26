***TagHandler.py - documentation - last updated on 9.2.2021 by uuk***
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
        
        handler for handling tags


        function __init__(self)
            
            creates an new TagHandler instance


            variable self.taggroups - name -> taggroup

            variable self.taglocations

        function from_data(self, taggroup: str, tagname: str, data: dict, replace=True)
            
            will inject certain data
            :param taggroup: the group to use
            :param tagname: the name of the tag
            :param data: the data to inject
            :param replace: if data should be replaced or not
            :return:


        function add_locations(self, locations: list)
            
            will add possible tag locations for later loading
            :param locations: the locations to add


        function reload(self)
            
            will reload all tag-related data


        function load_tags(self, direct_call=False)
            
            will load the tags
            :param direct_call: if build now or in the loading stage for it


        function get_tag_for(self, name: str, group: str) -> mcpython.common.data.tags.Tag.Tag
            
            will return the tag by name and group
            :param name: the name to use
            :param group: the group to use
            :return: the tag instance
            :raises ValueError: when the tag is not found


        function get_entries_for(self, name: str, group: str) -> list
            
            will return the tag by name and group
            :param name: the name to use
            :param group: the group to use
            :return: the tag instance


        function get_tags_for_entry(self, identifier: str, group: str) -> list
            
            will return an list of all tag instances these instance does occure in
            :param identifier: the identifier to search for
            :param group: the group to search in
            :return: an list of Tag-instances


        function has_entry_tag(self, identifier: str, group: str, tag_name: str) -> bool
            
            check if an given tag has an entry in it
            :param identifier: the entry to check
            :param group: the group to check for
            :param tag_name: the tag name to check for
            :return: if the identifier is in the given tag


    variable shared.tag_handler

    function add_from_location(loc: str)
        
        adds tags from an given scope for an given namespace where loc is the name of the namespace
        :param loc: the namespace
        WARNING: when adding outside normal build period, errors may occur


    @shared.mod_loader("minecraft", "stage:tag:group", info="adding tag group locations")
    function load_default_tags()
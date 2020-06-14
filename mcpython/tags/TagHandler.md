***TagHandler.py - documentation - last updated on 14.6.2020 by uuk***
___

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


        function get_tag_for(self, name: str, group: str) -> mcpython.tags.Tag.Tag
            
            will return the tag by name and group
            :param name: the name to use
            :param group: the group to use
            :return: the tag instance
            :raises ValueError: when the tag is not found


        function get_tags_for_entry(self, identifier: str, group: str) -> list
            
            will return an list of all tag instances these instance does occure in
            :param identifier: the identifier to search for
            :param group: the group to search in
            :return: an list of Tag-instances


        function has_entry_tag(self, identifier: str, group: str, tagname: str) -> bool
            
            check if an given tag has an entry in it
            :param identifier: the entry to check
            :param group: the group to check for
            :param tagname: the tag name to check for
            :return: if the identifier is in the given tag


    variable G.taghandler

    function add_from_location(loc: str)
        
        adds tags from an given scope for an given namespace where loc is the name of the namespace
        :param loc: the namespace
        WARNING: when adding outside normal build period, errors may occur


    @G.modloader("minecraft", "stage:tag:group", "adding tag group locations")
    function on_group_add()
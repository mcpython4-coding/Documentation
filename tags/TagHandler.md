***TagHandler.py - documentation - last updated on 14.5.2020 by uuk***
___

    class TagHandler
        function __init__(self)
        function from_data(self, taggroup: str, tagname: str, data: dict, replace=True)
        function add_locations(self, locations: list)
        function reload(self)
        function load_tags(self, direct_call=False)
        function get_tag_for(self, name: str, group: str) -> tags.Tag.Tag
        function get_tags_for_entry(self, identifier: str, group: str) -> list
        function has_entry_tag(self, identifier: str, group: str, tagname: str) -> bool

    variable G.taghandler

    function add_from_location(loc: str)
        
        adds tags from an given scope for an given namespace where loc is the name of the namespace
        :param loc: the namespace
        WARNING: when adding outside normal build period, errors may occur
        

    @G.modloader("minecraft", "stage:tag:group", "adding tag group locations") function on_group_add()
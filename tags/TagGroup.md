***TagGroup.py - documentation - last updated on 16.5.2020 by uuk***
___

    class TagGroup

        function __init__(self, name: str)

            variable self.name

            variable self.tags

            variable self.cache

        function add_from_data(self, tagname: str, data: dict, replace=True)

        function build(self)

        function get_tags_for(self, obj, cache=False) -> list

        function provides_object_tag(self, obj, tag_name: str) -> bool

        function provides_object_any_tag(self, obj, taglist: list) -> bool
***TagGroup.py - documentation - last updated on 14.6.2020 by uuk***
___

    class TagGroup
        
        class for holding an group of tags. e.g. all items


        function __init__(self, name: str)
            
            creates an new tag group
            :param name: the name of the group


            variable self.name

            variable self.tags

            variable self.cache

        function add_from_data(self, tagname: str, data: dict, replace=True)
            
            will insert
            :param tagname: the tag name to set
            :param data: the data to inject
            :param replace: if the existing tag should be removed
            :return:


        function build(self)
            
            will "build" the tag group


        function get_tags_for(self, obj, cache=False) -> list
            
            will return all tags for an given object
            :param obj:
            :param cache: if data should be cached


        function provides_object_tag(self, obj, tag_name: str) -> bool
            
            checks if the object has an given tag
            :param obj: the object to check
            :param tag_name: the tag to check for


        function provides_object_any_tag(self, obj, taglist: list) -> bool
            
            return if the given object is in any of the given tag names
            :param obj: the object to check
            :param taglist: the list of tag names to check

***TagGroup.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class TagTargetHolder

        function __init__(self, name: str)

            variable self.name

        function register_class(
                self, cls: typing.Type[mcpython.common.data.tags.ITagTarget.ITagTarget]
                ):

        function update(self, group: "TagGroup")

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

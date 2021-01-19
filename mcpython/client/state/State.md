***State.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class State extends IRegistryContent
        
        base class


        variable IS_MOUSE_EXCLUSIVE

        variable CONFIG_LOCATION - default location: data/{mod}/states/{name}.json

        static
        function is_mouse_exclusive(cls):  # todo: make attribute
                return cls.IS_MOUSE_EXCLUSIVE
                
                def __init__(self):

        function __init__(self)

            variable self.part_dict

            variable self.parts - todo: remove

            variable self.eventbus

        function activate(self)

        function deactivate(self)

        function bind_to_eventbus(self)

        function get_parts(self) -> list
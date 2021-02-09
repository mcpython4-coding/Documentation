***State.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
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
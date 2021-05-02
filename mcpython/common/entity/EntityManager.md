***EntityManager.py - documentation - last updated on 2.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class EntityManager
        
        Handler for entities in the current world


        function __init__(self)

            variable self.registry

        function add_entity_cls(self, registry, entity_cls)

        function spawn_entity(
                self,
                name: typing.Union[str, typing.Any],
                position,
                *args,
                dimension=None,
                uuid=None,
                check_summon=False,
                **kwargs
                ):

                    variable dimension

                    variable dimension

                variable entity_cls

                variable entity

                variable entity

                variable entity.uuid

            variable self.entity_map[entity.uuid]

        function tick(self, dt: float)

                    variable child

                        variable child.position

                        variable child

        function clear(self)

    variable shared.entity_manager

    function load()
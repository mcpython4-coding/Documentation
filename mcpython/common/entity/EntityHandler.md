***EntityHandler.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class EntityHandler
        
        Handler for entities in the current world


        function __init__(self)

            variable self.registry

        function add_entity_cls(self, registry, entity_cls)

        function spawn_entity(
                self,
                name,
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

                variable entity.uuid

            variable self.entity_map[entity.uuid]

        function tick(self, dt: float)

                    variable child

                        variable child.position

                        variable child

    variable shared.entity_handler

    function load()
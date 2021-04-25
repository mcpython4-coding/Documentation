***NetherPortal.py - documentation - last updated on 25.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class NetherPortalBlock extends mcpython.common.block.AbstractBlock.AbstractBlock
        
        Class for the nether portal block
        Uses the entity no collision collide system


        variable NAME

        variable NO_COLLISION

        variable SOLID

        variable HARDNESS

        variable DEFAULT_FACE_SOLID

        function __init__(self)

            variable self.axis

        function get_model_state(self) -> dict

        function set_model_state(self, state: dict)

        variable DEBUG_WORLD_BLOCK_STATES

        function on_block_update(self)

        function check_valid_surrounding(self)

        function check_valid_block(self, position: tuple, chunk=None)

            variable block

        function on_no_collision_collide(self, entity, previous: bool)

                variable entity.in_nether_portal_since

                variable entity.in_nether_portal_since
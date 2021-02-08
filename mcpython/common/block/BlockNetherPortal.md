***BlockNetherPortal.py - documentation - last updated on 8.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
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

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
***BlockNetherPortal.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class NetherPortalBlock extends mcpython.common.block.AbstractBlock.AbstractBlock
        
        Class for the nether portal block


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

        function on_no_collision_collide(self, player, previous: bool)

                variable player.in_nether_portal_since

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
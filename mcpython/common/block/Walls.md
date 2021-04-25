***Walls.py - documentation - last updated on 25.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractWall extends mcpython.common.block.AbstractBlock.AbstractBlock,  ABC

        variable DEFAULT_FACE_SOLID

        variable DEBUG_WORLD_BLOCK_STATES
            todo: up is not always allowed / depends on the configuration of the other stuff!

        function __init__(self)

            variable self.connections

        function on_block_added(self)

        function get_model_state(self) -> dict

        function on_block_update(self)

            variable dim

            variable block_north

            variable block_east

            variable block_south

            variable block_west

            variable self.connections["east"]

            variable self.connections["south"]

            variable self.connections["west"]

            variable self.connections["north"]

            variable self.connections["up"] - for next calculation, this must be False

            variable self.connections["up"]

            variable upper_block

                variable self.connections["up"]

        function set_model_state(self, state: dict)

    function create_wall_class(name: str)
        
        Constructor helper for creating a new wall class
        For internal usage only!


        class GeneratedWall extends AbstractWall

            variable NAME

    function load()
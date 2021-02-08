***BlockWall.py - documentation - last updated on 8.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class IWall extends mcpython.common.block.AbstractBlock.AbstractBlock

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


    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
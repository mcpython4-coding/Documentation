***BlockWall.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class IWall extends mcpython.common.block.AbstractBlock.AbstractBlock

        variable DEFAULT_FACE_SOLID

        function __init__(self)

            variable self.connections

        function on_block_added(self)

        function get_model_state(self) -> dict

        function on_block_update(self)

            variable dim

            variable block_north: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_east: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_south: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_west: mcpython.common.block.AbstractBlock.AbstractBlock

            variable self.connections["east"]

            variable self.connections["south"]

            variable self.connections["west"]

            variable self.connections["north"]

            variable self.connections["up"] - for next calculation, this must be False

            variable self.connections["up"]

            variable upper_block: mcpython.common.block.AbstractBlock.AbstractBlock

                variable self.connections["up"]

        function set_model_state(self, state: dict)

        static
        function get_all_model_states() -> list

    class RedSandstoneWall extends IWall

        variable NAME

    class SandstoneWall extends IWall

        variable NAME

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
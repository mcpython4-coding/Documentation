***BlockWall.py - documentation - last updated on 26.7.2020 by uuk***
___

    class IWall extends mcpython.block.Block.Block

        function __init__(self, *args, **kwargs)

            variable self.connections

        function get_model_state(self) -> dict

        function on_block_update(self)

            variable block_north: mcpython.block.Block.Block

            variable block_east: mcpython.block.Block.Block

            variable block_south: mcpython.block.Block.Block

            variable block_west: mcpython.block.Block.Block

            variable self.connections["east"]

            variable self.connections["south"]

            variable self.connections["west"]

            variable self.connections["north"]

            variable self.connections["up"] - for next calculation, this must be False

            variable self.connections["up"]

            variable upper_block: mcpython.block.Block.Block

                variable self.connections["up"]

        function set_model_state(self, state: dict)

        static
        function get_all_model_states() -> list

    class RedSandstoneWall extends IWall

        variable NAME

    class SandstoneWall extends IWall

        variable NAME

    @G.modloader("minecraft", "stage:block:load")
    function load()
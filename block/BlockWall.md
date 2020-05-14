***BlockWall.py - documentation - last updated on 14.5.2020 by uuk***
___

    class IWall extends block.Block.Block

        function __init__(self, *args, **kwargs)

            variable self.connections

            variable self.face_solid

        function get_model_state(self) -> dict

            variable state

        function on_block_update(self)

            variable block_north: block.Block.Block

            variable block_east: block.Block.Block

            variable block_south: block.Block.Block

            variable block_west: block.Block.Block

            variable self.connections["east"]

            variable self.connections["south"]

            variable self.connections["west"]

            variable self.connections["north"]

            variable self.connections["up"] - for next calculation, this must be False

            variable self.connections["up"]

            variable upper_block: block.Block.Block

                variable self.connections["up"]

        function set_model_state(self, state: dict)

                variable self.connections[key]

        static function get_all_model_states() -> list

            variable states

    @G.registry class AndesiteWall extends IWall

        variable NAME

    @G.registry class BrickWall extends IWall

        variable NAME

    @G.registry class CobblestoneWall extends IWall

        variable NAME

    @G.registry class DioriteWall extends IWall

        variable NAME

    @G.registry class EndStoneBrickWall extends IWall

        variable NAME

    @G.registry class GraniteWall extends IWall

        variable NAME

    @G.registry class MossyCobblestoneWall extends IWall

        variable NAME

    @G.registry class MossyStoneBrickWall extends IWall

        variable NAME

    @G.registry class NetherBrickWall extends IWall

        variable NAME

    @G.registry class PrismarineWall extends IWall

        variable NAME

    @G.registry class PrismarineWall extends IWall

        variable NAME

    @G.registry class RedNetherBrickWall extends IWall

        variable NAME

    @G.registry class RedSandstoneWall extends IWall

        variable NAME

    @G.registry class SandstoneWall extends IWall

        variable NAME

    @G.registry class StoneBrickWall extends IWall

        variable NAME
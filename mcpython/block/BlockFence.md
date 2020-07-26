***BlockFence.py - documentation - last updated on 26.7.2020 by uuk***
___

    class IFence extends mcpython.block.Block.Block
        
        Base class for every fence-like block. Expects


        variable FENCE_TYPE_NAME: set - the type list of the fences

        variable BBOX - the bounding box
            todo: add bounding-box

        function __init__(self, *args, **kwargs)
            
            will create the fence


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

        function set_model_state(self, state: dict)

        static
        function get_all_model_states() -> list

        function connects_to(self, face: mcpython.util.enums.EnumSide, blockinstance: mcpython.block.Block.Block)

        variable BLOCK_ITEM_GENERATOR_STATE

    class IWoodenFence extends IFence
        
        Base class for every wooden fence; used to set the wooden fence flag for all children at ones


        variable FENCE_TYPE_NAME

    class AcaciaFence extends IWoodenFence

        variable NAME

    class BirchFence extends IWoodenFence

        variable NAME

    class DarkOakFence extends IWoodenFence

        variable NAME

    class JungleFence extends IWoodenFence

        variable NAME

    class OakFence extends IWoodenFence

        variable NAME

    class SpruceFence extends IWoodenFence

        variable NAME

    class CrimsonFence extends IFence

        variable FENCE_TYPE_NAME

        variable NAME

    class WarpedFence extends IFence

        variable FENCE_TYPE_NAME

        variable NAME

    class NetherBrickFence extends IFence

        variable NAME

        variable FENCE_TYPE_NAME

    @G.modloader("minecraft", "stage:block:load")
    function load()
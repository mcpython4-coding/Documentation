***BlockFence.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IFence extends mcpython.common.block.AbstractBlock.AbstractBlock,  ABC
        
        Abstract base class for every fence-like block


        variable FENCE_TYPE_NAME
            The type list of the fences; same types are able to connect to each other, not same types not

        variable BBOX
            the bounding box todo: add the real bounding box

        variable DEBUG_WORLD_BLOCK_STATES
            the debug world states, constructed by a builder, using all possible combinations

        variable DEFAULT_FACE_SOLID

        function __init__(self)

            variable self.connections

        function on_block_added(self)

        function get_model_state(self) -> dict

        function on_block_update(self)

            variable block_north: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_east: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_south: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_west: mcpython.common.block.AbstractBlock.AbstractBlock

            variable self.connections["east"]

            variable self.connections["south"]

            variable self.connections["west"]

            variable self.connections["north"]

        function set_model_state(self, state: dict)

        function connects_to(
                self,
                face: mcpython.util.enums.EnumSide,
                instance: mcpython.common.block.AbstractBlock.AbstractBlock,
                ):

        variable BLOCK_ITEM_GENERATOR_STATE
            the state the block item generator should use, this kinda looks nice

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

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
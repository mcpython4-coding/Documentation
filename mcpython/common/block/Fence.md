***Fence.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractFence extends mcpython.common.block.AbstractBlock.AbstractBlock,  ABC
        
        Abstract base class for every fence-like block


        variable FENCE_TYPE_NAME
            The type list of the fences; same types are able to connect to each other, not same types not

        variable BBOX
            the bounding box todo: add the real bounding box

        variable DEBUG_WORLD_BLOCK_STATES
            the debug world states, constructed by a builder, using all possible combinations

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        function __init__(self)

            variable self.connections

        function get_model_state(self) -> dict

            variable block_north: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_east: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_south: mcpython.common.block.AbstractBlock.AbstractBlock

            variable block_west: mcpython.common.block.AbstractBlock.AbstractBlock

            variable self.connections["east"]

            variable self.connections["south"]

            variable self.connections["west"]

            variable self.connections["north"]

                variable self.connections[key]

        function connects_to(
                self,
                face: mcpython.util.enums.EnumSide,
                instance: mcpython.common.block.AbstractBlock.AbstractBlock,
                ):

        variable BLOCK_ITEM_GENERATOR_STATE
            the state the block item generator should use, this kinda looks nice

    class AbstractFenceGate extends mcpython.common.block.AbstractBlock.AbstractBlock,  ABC
        
        todo: implement behaviour


        variable DEBUG_WORLD_BLOCK_STATES

        function __init__(self)

            variable self.facing

            variable self.in_wall

            variable self.open

        function get_model_state(self) -> dict

                    variable self.facing

                variable self.in_wall

                variable self.open

        variable BLOCK_ITEM_GENERATOR_STATE

    class AbstractWoodenFence extends AbstractFence
        
        Base class for every wooden fence; used to set the wooden fence flag for all children at ones


        variable FENCE_TYPE_NAME

    class BirchFence extends AbstractWoodenFence

        variable NAME

    class DarkOakFence extends AbstractWoodenFence

        variable NAME

    class JungleFence extends AbstractWoodenFence

        variable NAME

    class OakFence extends AbstractWoodenFence

        variable NAME

    class SpruceFence extends AbstractWoodenFence

        variable NAME

    class AcaciaFence extends AbstractWoodenFence

        variable NAME

    class CrimsonFence extends AbstractFence

        variable FENCE_TYPE_NAME

        variable NAME

    class WarpedFence extends AbstractFence

        variable FENCE_TYPE_NAME

        variable NAME

    class NetherBrickFence extends AbstractFence

        variable NAME

        variable FENCE_TYPE_NAME
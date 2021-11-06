***FluidBlock.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IFluidBlock extends mcpython.common.block.AbstractBlock.AbstractBlock,  ABC
        
        Base class for fluid blocks
        Users need to simply extend this and set the UNDERLYING_FLUID property to their fluid instance
        todo: implement source / flow logic
        todo: implement renderer


        variable UNDERLYING_FLUID

        variable FLUID_RENDERER

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        variable NO_ENTITY_COLLISION

        variable CUSTOM_WALING_SPEED_MULTIPLIER

        variable IS_BREAKABLE

        static
        function __init_subclass__(cls, **kwargs)

        function __init__(self)

            variable self.is_flowing

            variable self.flow_direction

            variable self.height

        function on_block_added(self)

        function write_to_network_buffer(self, buffer: WriteBuffer)

        function read_from_network_buffer(self, buffer: ReadBuffer)

    class WaterFluidBlock extends IFluidBlock

        variable NAME

        variable UNDERLYING_FLUID

        variable WATER_COLOR
            todo: make biome based

        variable WaterFluidBlock.FLUID_RENDERER.color

    class LavaFluidBlock extends IFluidBlock

        variable NAME

        variable UNDERLYING_FLUID
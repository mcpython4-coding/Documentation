***AbstractFluid.py - documentation - last updated on 27.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractFluid extends mcpython.common.event.api.IRegistryContent,  ABC
        
        Abstract class defining fluid behaviour
        This is the stuff referenced by FluidStacks


        variable TYPE

        variable TEXTURE_FLOW: str
            The texture of the fluid, for rendering
            Should be set to something meaningful for the fluid renderer

        variable TEXTURE_STILL: str

        variable IS_FINITE
            Property of fluid blocks: are they creating infinite sources?

        variable CREATE_FLOW_STREAM
            Property of fluid blocks: are they creating a flow stream from the source?

        variable MOVE_SOURCE_BLOCK_ALONG_FLOW
            Property of fluid block: is the source block moving along the flow?

        variable DEFAULT_FLUID_TEMPERATURE: float
            Property for some mods; the temperature, in K

        variable FLUID_BLOCK_NAME: typing.Optional[str]
            The block name of the IFluidBlock for this fluid. If None, no fluid block is arrival

        variable CRITICAL_AMOUNT
            A FluidStack size which is "critical", that means that this class wants to be informed about it
            Set to -1 if the smallest amount is critical

        variable CAN_BE_CRITICAL_ON_CONTACT
            Set this to detect fluids touching with each other by the on_fluids_touching function
            This can be used by e.g. lava for cobble gen

        variable SOLIDIFICATION_POINT
            When the fluid solidifies, in K; Only for inter-mod information

        variable SOLIDIFIES_TO
            What does it solidify to?

        static
        function __init_subclass__(cls, **kwargs)

                variable block_registry

                    variable cls.FLUID_BLOCK_NAME

        static
        function get_flow_rate_at(
                cls,
                dimension: mcpython.engine.world.AbstractInterface.IDimension,
                position: typing.Tuple[int, int, int],
                ) -> int:
            
            How many ticks it take to flow one block further
            This function is only used when defining a FluidBlock with this fluid
            :param dimension: the dimension in
            :param position: the position at
            :return: the flow rate


        static
        function on_critical_amount_reached(cls, fluid_stack)
            
            Called when a FluidStack of this item gets bigger than CRITICAL_AMOUNT
            todo: more meta information!
            :param fluid_stack: the fluid stack in


        static
        function on_fluids_touching(
                cls,
                other: typing.Type["AbstractFluid"],
                dimension: mcpython.engine.world.AbstractInterface.IDimension,
                position_this: typing.Optional[typing.Tuple[float, float, float]],
                position_that: typing.Optional[typing.Tuple[float, float, float]],
                is_fluid_block=(True, True),
                ):
            
            Called when this fluid is touching another one and CAN_BE_CRITICAL_ON_CONTACT is True
            :param other: the other fluid type
            :param dimension:the dimension in
            :param position_this: optional: were we are in the dimension
            :param position_that: optional: were the other fluid is in this dimension
            :param is_fluid_block: this and that are fluid blocks [the position is a pointer to a fluid block]?

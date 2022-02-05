***BlockFactory.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable block_factory_builder

    function set_log(instance: FactoryBuilder.IFactory)

    function set_fall_able(instance: FactoryBuilder.IFactory)

    function set_slab(instance: FactoryBuilder.IFactory)

    function set_wall(instance: FactoryBuilder.IFactory)

    function set_fence(instance: FactoryBuilder.IFactory, *types: str)

    function set_fence_gate(instance: FactoryBuilder.IFactory)

    function set_fluid_block(instance: FactoryBuilder.IFactory)

    function set_all_direction_orientable(instance: FactoryBuilder.IFactory)

    function set_horizontal_orientable(instance: FactoryBuilder.IFactory)

    function set_button(instance: FactoryBuilder.IFactory)

    function set_flower_like(instance: FactoryBuilder.IFactory)

    function set_strength(
            instance: FactoryBuilder.IFactory,
            hardness: float | typing.Tuple[float, float],
            blast_resistance: float = None,
            ):

        variable instance.config_table["hardness"]

        variable instance.config_table["blast_resistance"]

    function set_assigned_tools(instance: FactoryBuilder.IFactory, *tools, tool_level=None)

        variable instance.config_table["assigned_tools"]

    function set_all_side_solid(instance: FactoryBuilder.IFactory, solid: bool)

    function set_side_solid(instance: FactoryBuilder.IFactory, side: EnumSide, solid: bool)

    function set_default_model_state(
            instance: FactoryBuilder.IFactory, state: typing.Union[dict, str]
            ):

            variable state

        variable instance.config_table["default_model_state"]

    function build_class(
            cls: typing.Type[mcpython.common.block.AbstractBlock.AbstractBlock],
            instance: FactoryBuilder.IFactory,
            ):

        variable configs

        variable name

            variable name

        class ModifiedClass extends cls

            variable NAME

            variable HARDNESS

            variable BLAST_RESISTANCE

            variable MINIMUM_TOOL_LEVEL

            variable ASSIGNED_TOOLS

            variable IS_BREAKABLE

                variable IS_BREAKABLE

            variable DEFAULT_FACE_SOLID

            variable CUSTOM_WALING_SPEED_MULTIPLIER

            variable BLOCK_ITEM_GENERATOR_STATE

            variable IS_SOLID

            variable CAN_CONDUCT_REDSTONE_POWER

            variable CAN_MOBS_SPAWN_ON

            variable CAN_MOBS_SPAWN_IN

            variable ENABLE_RANDOM_TICKS

            variable NO_ENTITY_COLLISION

            variable ENTITY_FALL_MULTIPLIER

            variable DEBUG_WORLD_BLOCK_STATES

            variable FENCE_TYPE_NAME

    function build_class_default_state(
            cls: typing.Type[mcpython.common.block.AbstractBlock.AbstractBlock],
            instance: FactoryBuilder.IFactory,
            ):

        variable is_super_base

        variable bases

        variable configs

        class ModifiedClass extends cls

            function __init__(self)

            function get_inventories(self)

            function get_provided_slot_lists(self, side: mcpython.util.enums.EnumSide)

            function get_model_state(self) -> dict

            function get_view_bbox(self)

            function get_collision_bbox(self)

            function inject_redstone_power(
                    self, side: mcpython.util.enums.EnumSide, level: int, call_update=True
                    ):

                variable self.injected_redstone_power[side.index]

            function get_redstone_output(self, side: mcpython.util.enums.EnumSide) -> int

            function get_redstone_source_power(self, side: mcpython.util.enums.EnumSide)

    variable BlockFactory
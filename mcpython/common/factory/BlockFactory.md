***BlockFactory.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable block_factory_builder

    function set_log(instance: FactoryBuilder.IFactory)

    function set_fall_able(instance: FactoryBuilder.IFactory)

    function set_slab(instance: FactoryBuilder.IFactory)

    function set_wall(instance: FactoryBuilder.IFactory)

    function set_horizontal_orientable(instance: FactoryBuilder.IFactory)

    function set_strength(
            instance: FactoryBuilder.IFactory, hardness: float, blast_resistance: float = None
            ):

        variable instance.config_table["hardness"]

        variable instance.config_table["blast_resistance"]

    function set_assigned_tools(instance: FactoryBuilder.IFactory, *tools, tool_level=None)

    function set_all_side_solid(instance: FactoryBuilder.IFactory, solid: bool)

    function set_default_model_state(
            instance: FactoryBuilder.IFactory, state: typing.Union[dict, str]
            ):

            variable state

        variable instance.config_table["default_model_state"]

    function build_class(
            cls: typing.Type[mcpython.common.block.AbstractBlock.AbstractBlock],
            instance: FactoryBuilder.IFactory,
            ):

        variable name

            variable name

        class ModifiedClass extends cls

            variable NAME

            variable HARDNESS

            variable BLAST_RESISTANCE

            variable MINIMUM_TOOL_LEVEL

            variable ASSIGNED_TOOLS

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

    function build_class_default_state(
            cls: typing.Type[mcpython.common.block.AbstractBlock.AbstractBlock],
            instance: FactoryBuilder.IFactory,
            ):

        variable is_super_base

        variable bases

        variable configs

        class ModifiedClass extends cls

            function __init__(self)

            function set_creation_properties(self, *args, **kwargs)

            function on_block_added(self, *args, **kwargs)

            function on_block_remove(self, *args, **kwargs)

            function on_random_update(self, *args, **kwargs)

            function on_block_update(self, *args, **kwargs)

            function on_redstone_update(self, *args, **kwargs)

            function on_player_interaction(self, *args, **kwargs)

            function on_no_collision_collide(self, *args, **kwargs)

            function get_save_data(self)

            function dump_data(self)

            function load_data(self, data)

            function inject(self, data: bytes)

            function get_item_saved_state(self)

            function set_item_saved_state(self, state)

            function get_inventories(self)

            function get_provided_slot_lists(self, side: mcpython.util.enums.EnumSide)

            function get_model_state(self) -> dict

            function set_model_state(self, state: dict)

            function get_view_bbox(self)

            function get_collision_bbox(self)

            function on_request_item_for_block(
                    self, itemstack: mcpython.common.container.ItemStack.ItemStack
                    ):

            function inject_redstone_power(self, side: mcpython.util.enums.EnumSide, level: int)

            function get_redstone_output(self, side: mcpython.util.enums.EnumSide) -> int

            function get_redstone_source_power(self, side: mcpython.util.enums.EnumSide)

    variable BlockFactory
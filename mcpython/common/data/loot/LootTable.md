***LootTable.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class LootTableTypes extends enum.Enum

        variable UNSET

        variable EMPTY

        variable ENTITY

        variable BLOCK

        variable CHEST

        variable FISHING

        variable GIFT

        variable ADVANCEMENT_REWARD

        variable GENERIC

        variable BARTER

    class LootTablePoolEntryType extends enum.Enum

        variable UNSET

        variable ITEM

        variable TAG

        variable LOOT_TABLE

        variable GROUP

        variable ALTERNATIVES

        variable SEQUENCE

        variable DYNAMIC

        variable EMPTY

    class LootTableHandler

        function __init__(self)

            variable self.loot_tables

            variable self.relink_table

            variable self.mod_names_to_load

        function reload(self)

        function shuffle_data(self)

        function __getitem__(self, item)

        function roll(self, name: str, *args, relink=True, **kwargs) -> list
            
            will roll the loot table
            :param name: the name of the loot table
            :param args: args send to every part
            :param relink: if relinks should be followed or not
            :param kwargs: kwargs send to every part
            :return: an list of item stacks
            kwarg-options:
                - block=<Block instance>: an block parsed on
                - damage_source=<DamageSource instance>: an damage source
                - this_entity=<Entity instance>: an entity generated for
                - killer_entity=<Entity instance>:  the entity killed the this_entity
                - position=<tuple of length 3>: the position executed at


        function get_drop_for_block(self, block, player=None, relink=True)

        function for_mod_name(self, modname: str, path_name: str = None, immediate=False)

        function _add_load(self, mod, path: str, immediate=False)

        function from_file(self, file: str)

        static
        function parse_function(
                cls, data: dict
                ) -> mcpython.common.data.loot.LootTableFunction.ILootTableFunction:

            variable name

        static
        function parse_condition(
                cls, data: dict
                ) -> mcpython.common.data.loot.LootTableCondition.ILootTableCondition:

            variable name

    variable handler

    class LootTablePoolEntry

        static
        function from_data(cls, pool, data: dict)

        function __init__(self, entry_type=LootTablePoolEntryType.UNSET)

            variable self.pool

            variable self.entry_type

            variable self.conditions

            variable self.name

            variable self.children: typing.List["LootTablePoolEntry"]

            variable self.expand

            variable self.functions

            variable self.weight

            variable self.quality

        function roll(self, *args, **kwargs)

    class LootTablePool

        static
        function from_data(cls, table, data: dict)

        function __init__(self)

            variable self.conditions

            variable self.functions

            variable self.roll_range

            variable self.bonus_roll_range

            variable self.entries

            variable self.entry_weights

            variable self.table

        function roll(self, *args, **kwargs)

    class LootTable

        static
        function from_file(cls, file: str, name=None)

        static
        function from_data(cls, data: dict, name: str)

        function __init__(self, table_type=LootTableTypes.UNSET)

            variable self.table_type

            variable self.pools

        function roll(self, *args, **kwargs)
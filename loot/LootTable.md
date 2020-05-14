***LootTable.py - documentation - last updated on 14.5.2020 by uuk***
___

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

        function __getitem__(self, item)

        function roll(self, name: str, *args, **kwargs) -> list

                variable name

        function for_mod_name(self, modname, directoryname=None)

            variable modinstance

        function _add_load(self, modinstance, path)

        function from_file(self, file: str)

        function parse_function(self, data: dict) -> loot.LootTableFunction.ILootTableFunction

            variable name

        function parse_condition(self, data: dict) -> loot.LootTableCondition.ILootTableCondition

            variable name

        function get_drop_for_block(self, block, player=None)

            variable table_name

    variable handler

    class LootTablePoolEntry

        static function from_data(cls, pool, data: dict)

            variable obj

            variable obj.pool

                variable obj.conditions

                variable obj.functions

                variable obj.name

                variable obj.children

                variable obj.expand

                variable obj.weight

                variable obj.quality

        function __init__(self, entry_type=LootTablePoolEntryType.UNSET)

            variable self.pool

            variable self.entry_type

            variable self.conditions

            variable self.name

            variable self.children

            variable self.expand

            variable self.functions

            variable self.weight

            variable self.quality

        function roll(self, *args, **kwargs)

            variable items

                    variable item

                    variable item

    class LootTablePool

        static function from_data(cls, table, data: dict)

            variable obj

            variable obj.table

                variable obj.conditions

                variable obj.functions

                variable obj.entries

                variable obj.entry_weights

                    variable obj.roll_range

                    variable obj.roll_range

        function __init__(self)

            variable self.conditions

            variable self.functions

            variable self.roll_range

            variable self.bonus_roll_range

            variable self.entries

            variable self.entry_weights

            variable self.table

        function roll(self, *args, **kwargs)

            variable items

            variable i

            variable done

                variable entry

                variable item

    class LootTable

        static function from_file(cls, file: str, name=None)

                variable s

                variable name

        static function from_data(cls, data: dict, name: str)

            variable obj

            variable handler.loot_tables[name]

        function __init__(self, table_type=LootTableTypes.UNSET)

            variable self.table_type

            variable self.pools

        function roll(self, *args, **kwargs)

            variable data

    function init()
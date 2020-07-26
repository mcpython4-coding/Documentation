***LootTableGenerator.py - documentation - last updated on 26.7.2020 by uuk***
___

    class ILootTableCondition

        function serialize(self)

    class ILootTableFunction

        function serialize(self)

    class ApplyBonus extends ILootTableFunction

        function __init__(self, enchantment: str, formula: str = "uniform_bonus_count", extra=None, probability=None,
                bonus_multiplier=None, conditions=None):

        function serialize(self)

    class CopyName extends ILootTableFunction

        function serialize(self)

    class NBTCopyOperation

        function __init__(self, nbt_source: str, nbt_target: str = None, op="merge")

            variable self.nbt_source

            variable self.nbt_target

            variable self.op

        function serialize(self)

    class CopyNBT extends ILootTableFunction

        function __init__(self, source: str, *operations: NBTCopyOperation)

            variable self.source

            variable self.operations

        function addOperation(self, operation: NBTCopyOperation)

        function serialize(self)

    class CopyState extends ILootTableFunction

        function __init__(self, block: str, *properties: str)

            variable self.copy_properties

            variable self.block

        function addProperty(self, *properties: str)

        function serialize(self)

    class EnchantRandomly extends ILootTableFunction

        function __init__(self, *enchantments: str)

            variable self.enchantments

        function addEnchantment(self, *enchanments: str)

        function serialize(self)

    class ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.weight

            variable self.quality

            variable self.conditions

            variable self.functions

        function addCondition(self, condition: ILootTableCondition)

        function addFunction(self, function: ILootTableFunction)

        function serialize(self) -> typing.Dict[str, typing.Any]

    class ItemLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.item_name

        function setItemName(self, name: str)

        function serialize(self)

    class TagLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1, expand=False)

            variable self.tag_name

            variable self.expand

        function setTagName(self, name: str)

        function serialize(self)

    class LootTableLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.loot_table_name

        function setLootTable(self, name: str)

        function serialize(self)

    class GroupLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.children

        function addChild(self, child: ILootTableEntry)

        function serialize(self)

    class AlternativesLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.children

        function addChild(self, child: ILootTableEntry)

        function serialize(self)

    class SequenceLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.children

        function addChild(self, child: ILootTableEntry)

        function serialize(self)

    class DynamicLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.ref_name

        function setRefName(self, name: str)

        function serialize(self)

    class LootTablePool

        function __init__(self, rolls: typing.Union[int, typing.Tuple[int, int]] = 1, bonus_rolls: typing.Union[int, typing.Tuple[int, int]] = 1)

            variable self.rolls

            variable self.bonus_rolls

            variable self.conditions

            variable self.functions

            variable self.entries

        function addCondition(self, condition: ILootTableCondition)

        function addFunction(self, function: ILootTableFunction)

        function addEntry(self, entry: ILootTableEntry)

        function serialize(self)

    class LootTableGenerator extends mcpython.datagen.Configuration.IDataGenerator

        function __init__(self, config, name)

            variable self.name

            variable self.type

            variable self.pools

        function setType(self, t)

        function addPool(self, pool: LootTablePool)

        function generate(self)
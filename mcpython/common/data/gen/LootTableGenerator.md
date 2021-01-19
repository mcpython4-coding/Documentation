***LootTableGenerator.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class ILootTableCondition extends IDataGenerator,  ABC

    class ILootTableFunction extends IDataGenerator,  ABC

    class ApplyBonus extends ILootTableFunction

        function __init__(
                self,
                enchantment: str,
                formula: str = "uniform_bonus_count",
                extra=None,
                probability=None,
                bonus_multiplier=None,
                conditions=None,
                ):

            variable formula: str

            variable self.enchantment

            variable self.formula

            variable self.extra

            variable self.probability

            variable self.bonus_multiplier

            variable self.conditions

        function dump(self, generator: DataGeneratorInstance)

    class CopyName extends ILootTableFunction

        function dump(self, generator: DataGeneratorInstance)

    class NBTCopyOperation

        function __init__(self, nbt_source: str, nbt_target: str = None, op="merge")

            variable self.nbt_source

            variable self.nbt_target

            variable self.op

        function dump(self, generator: DataGeneratorInstance)

    class CopyNBT extends ILootTableFunction

        function __init__(self, source: str, *operations: NBTCopyOperation)

            variable self.source

            variable self.operations

        function addOperation(self, operation: NBTCopyOperation)

        function dump(self, generator: DataGeneratorInstance)

    class CopyState extends ILootTableFunction

        function __init__(self, block: str, *properties: str)

            variable self.copy_properties

            variable self.block

        function addProperty(self, *properties: str)

        function dump(self, generator: DataGeneratorInstance)

    class EnchantRandomly extends ILootTableFunction

        function __init__(self, *enchantments: str)

            variable self.enchantments

        function addEnchantment(self, *enchanments: str)

        function dump(self, generator: DataGeneratorInstance)

    class ILootTableEntry extends IDataGenerator

        function __init__(self, weight=1, quality=1)

            variable self.weight

            variable self.quality

            variable self.conditions

            variable self.functions

        function addCondition(self, condition: ILootTableCondition)

        function addFunction(self, function: ILootTableFunction)

        function dump(self, generator: DataGeneratorInstance)

    class ItemLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.item_name

        function setItemName(self, name: str)

        function dump(self, generator: DataGeneratorInstance)

    class TagLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1, expand=False)

            variable self.tag_name

            variable self.expand

        function setTagName(self, name: str)

        function dump(self, generator: DataGeneratorInstance)

    class LootTableLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.loot_table_name

        function setLootTable(self, name: str)

        function dump(self, generator: DataGeneratorInstance)

    class GroupLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.children

        function addChild(self, child: ILootTableEntry)

        function dump(self, generator: DataGeneratorInstance)

    class AlternativesLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.children

        function addChild(self, child: ILootTableEntry)

        function dump(self, generator: DataGeneratorInstance)

    class SequenceLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.children

        function addChild(self, child: ILootTableEntry)

        function dump(self, generator: DataGeneratorInstance)

    class DynamicLootTableEntry extends ILootTableEntry

        function __init__(self, weight=1, quality=1)

            variable self.ref_name

        function setRefName(self, name: str)

        function dump(self, generator: DataGeneratorInstance)

    class LootTablePool extends IDataGenerator

        function __init__(
                self,
                rolls: typing.Union[int, typing.Tuple[int, int]] = 1,
                bonus_rolls: typing.Union[int, typing.Tuple[int, int]] = 1,
                ):

            variable self.rolls

            variable self.bonus_rolls

            variable self.conditions

            variable self.functions

            variable self.entries

        function addCondition(self, condition: ILootTableCondition)

        function addFunction(self, function: ILootTableFunction)

        function addEntry(self, entry: ILootTableEntry)

        function dump(self, generator: DataGeneratorInstance)

    class LootTableGenerator extends IDataGenerator

        function __init__(self, config, name)

            variable self.name

            variable self.type

            variable self.pools

        function setType(self, t)

        function addPool(self, pool: LootTablePool)

        function dump(self, generator: DataGeneratorInstance)

        function get_default_location(self, generator: "DataGeneratorInstance", name: str)
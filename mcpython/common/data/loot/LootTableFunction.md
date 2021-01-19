***LootTableFunction.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class ILootTableFunction extends mcpython.common.event.Registry.IRegistryContent

        variable TYPE

        function __init__(self, data: dict)

            variable self.data

        function apply(self, items: list, *args, **kwargs)

    variable loot_table_function_registry

    @shared.registry class ApplyBonus extends ILootTableFunction

        variable NAME

        function __init__(self, data: dict)

            variable self.enchantment

            variable self.formula

            variable self.parameters

        function apply(self, items: list, *args, **kwargs)

    @shared.registry class CopyName extends ILootTableFunction

        variable NAME

        function __init__(self, data: dict)

            variable self.source

        function apply(self, items: list, *args, **kwargs)

    @shared.registry class CopyNBT extends ILootTableFunction

        variable NAME

    @shared.registry class CopyState extends ILootTableFunction

        variable NAME

    @shared.registry class EnchantRandomly extends ILootTableFunction

        variable NAME

    @shared.registry class EnchantWithLevels extends ILootTableFunction

        variable NAME

    @shared.registry class ExplorationMap extends ILootTableFunction

        variable NAME

    @shared.registry class ExplosionDecay extends ILootTableFunction

        variable NAME

    @shared.registry class FurnaceSmelt extends ILootTableFunction

        variable NAME

        function apply(self, items: list, *args, **kwargs)

    @shared.registry class FillPlayerHead extends ILootTableFunction

        variable NAME

    @shared.registry class LimitCount extends ILootTableFunction

        variable NAME

    @shared.registry class LootingEnchant extends ILootTableFunction

        variable NAME

    @shared.registry class SetAttributes extends ILootTableFunction

        variable NAME

    @shared.registry class SetContents extends ILootTableFunction

        variable NAME

    @shared.registry class SetCount extends ILootTableFunction

        variable NAME

        function apply(self, items: list, *args, **kwargs)

    @shared.registry class SetDamage extends ILootTableFunction

        variable NAME

    @shared.registry class SetLore extends ILootTableFunction

        variable NAME

    @shared.registry class SetName extends ILootTableFunction

        variable NAME

    @shared.registry class SetNBT extends ILootTableFunction

        variable NAME

    @shared.registry class SetStewEffect extends ILootTableFunction

        variable NAME
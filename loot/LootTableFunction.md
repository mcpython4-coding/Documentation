***LootTableFunction.py - documentation - last updated on 16.5.2020 by uuk***
___

    class ILootTableFunction extends event.Registry.IRegistryContent

        variable TYPE

        function __init__(self, data: dict)

            variable self.data

        function apply(self, items: list, *args, **kwargs)

    variable loottablefunctionregistry

    @G.registry class ApplyBonus extends ILootTableFunction

        variable NAME

        function __init__(self, data: dict)

            variable self.enchantment

            variable self.formula

            variable self.parameters

        function apply(self, items: list, *args, **kwargs)

    @G.registry class CopyName extends ILootTableFunction

        variable NAME

        function __init__(self, data: dict)

            variable self.source

        function apply(self, items: list, *args, **kwargs)

    @G.registry class CopyNBT extends ILootTableFunction

        variable NAME

    @G.registry class CopyState extends ILootTableFunction

        variable NAME

    @G.registry class EnchantRandomly extends ILootTableFunction

        variable NAME

    @G.registry class EnchantWithLevels extends ILootTableFunction

        variable NAME

    @G.registry class ExplorationMap extends ILootTableFunction

        variable NAME

    @G.registry class ExplosionDecay extends ILootTableFunction

        variable NAME

    @G.registry class FurnaceSmelt extends ILootTableFunction

        variable NAME

        function apply(self, items: list, *args, **kwargs)

    @G.registry class FillPlayerHead extends ILootTableFunction

        variable NAME

    @G.registry class LimitCount extends ILootTableFunction

        variable NAME

    @G.registry class LootingEnchant extends ILootTableFunction

        variable NAME

    @G.registry class SetAttributes extends ILootTableFunction

        variable NAME

    @G.registry class SetContents extends ILootTableFunction

        variable NAME

    @G.registry class SetCount extends ILootTableFunction

        variable NAME

        function apply(self, items: list, *args, **kwargs)

    @G.registry class SetDamage extends ILootTableFunction

        variable NAME

    @G.registry class SetLore extends ILootTableFunction

        variable NAME

    @G.registry class SetName extends ILootTableFunction

        variable NAME

    @G.registry class SetNBT extends ILootTableFunction

        variable NAME

    @G.registry class SetStewEffect extends ILootTableFunction

        variable NAME
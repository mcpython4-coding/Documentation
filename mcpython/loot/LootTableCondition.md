***LootTableCondition.py - documentation - last updated on 18.6.2020 by uuk***
___

    class ILootTableCondition extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        function __init__(self, data: dict)

            variable self.data

        function check(self, source, *args, **kwargs) -> bool

    variable loottableconditionregistry

    @G.registry class Alternative extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.conditions

        function check(self, source, *args, **kwargs) -> bool

    @G.registry class BlockStateProperty extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.name

            variable self.state

        function check(self, source, *args, block=None, **kwargs) -> bool

    @G.registry class DamageSourceProperties extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.source

        function check(self, source, *args, damage_source=None, **kwargs) -> bool

    @G.registry class EntityProperties extends ILootTableCondition

        variable NAME

    @G.registry class EntityScores extends ILootTableCondition

        variable NAME

    @G.registry class Inverted extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.term

        function check(self, source, *args, **kwargs) -> bool

    @G.registry class KilledByPlayer extends ILootTableCondition

        variable NAME

    @G.registry class LocationCheck extends ILootTableCondition

        variable NAME

    @G.registry class MatchTool extends ILootTableCondition

        variable NAME

    @G.registry class RandomChance extends ILootTableCondition

        variable NAME

        function check(self, source, *args, **kwargs) -> bool

    @G.registry class RandomChanceWithLooting extends RandomChance

        variable NAME

    @G.registry class Reference extends ILootTableCondition

        variable NAME

    @G.registry class SurvivesExplosion extends ILootTableCondition

        variable NAME

        function check(self, source, *args, **kwargs) -> bool: return True
                
                
                @G.registry
                class TableBonus(ILootTableCondition):

    @G.registry class TableBonus extends ILootTableCondition

        variable NAME

    @G.registry class TimeCheck extends ILootTableCondition

        variable NAME

    @G.registry class ToolEnchantment extends ILootTableCondition

        variable NAME

    @G.registry class WeatherCheck extends ILootTableCondition

        variable NAME
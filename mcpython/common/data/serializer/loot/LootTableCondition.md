***LootTableCondition.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ILootTableCondition extends mcpython.common.event.Registry.IRegistryContent

        variable TYPE

        function __init__(self, data: dict)

            variable self.data

        function check(self, source, *args, **kwargs) -> bool

    variable loot_table_condition_registry

    @shared.registry class Alternative extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.conditions

        function check(self, source, *args, **kwargs) -> bool

    @shared.registry class BlockStateProperty extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.name

            variable self.state

        function check(self, source, *args, block=None, **kwargs) -> bool

    @shared.registry class DamageSourceProperties extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.source

        function check(self, source, *args, damage_source=None, **kwargs) -> bool

    @shared.registry class EntityProperties extends ILootTableCondition

        variable NAME

    @shared.registry class EntityScores extends ILootTableCondition

        variable NAME

    @shared.registry class Inverted extends ILootTableCondition

        variable NAME

        function __init__(self, data)

            variable self.term

        function check(self, source, *args, **kwargs) -> bool

    @shared.registry class KilledByPlayer extends ILootTableCondition

        variable NAME

    @shared.registry class LocationCheck extends ILootTableCondition

        variable NAME

    @shared.registry class MatchTool extends ILootTableCondition

        variable NAME

    @shared.registry class RandomChance extends ILootTableCondition

        variable NAME

        function check(self, source, *args, **kwargs) -> bool

    @shared.registry class RandomChanceWithLooting extends RandomChance

        variable NAME

    @shared.registry class Reference extends ILootTableCondition

        variable NAME

    @shared.registry class SurvivesExplosion extends ILootTableCondition

        variable NAME

        function check(self, source, *args, **kwargs) -> bool

    @shared.registry class TableBonus extends ILootTableCondition

        variable NAME

    @shared.registry class TimeCheck extends ILootTableCondition

        variable NAME

    @shared.registry class ToolEnchantment extends ILootTableCondition

        variable NAME

    @shared.registry class WeatherCheck extends ILootTableCondition

        variable NAME
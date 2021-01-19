***GameRule.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class GameRuleDataType

        static
        function is_valid_value(cls, data: str)

        function copy(self)

        function save(self)
            
            :return: an json-able representation of this type


        function load(self, data)
            
            loads from previous saved data the gamerule
            :param data: the data saved


    class GameRuleTypeBoolean extends GameRuleDataType

        static
        function is_valid_value(cls, data: str)

        function __init__(self, data: str)

            variable data

            variable self.status

        function copy(self)

        function save(self)

        function load(self, data)

    class GameRuleTypeInt extends GameRuleDataType

        static
        function is_valid_value(cls, data: str)

        function __init__(self, data: str)

            variable self.status

        function copy(self)

        function save(self)

        function load(self, data)

    class GameRule extends mcpython.common.event.Registry.IRegistryContent

        variable TYPE

        variable VALUE_TYPE

        variable DEFAULT_VALUE

        function __init__(self, world)

            variable self.status

            variable self.world

        function set_status(self, value: str)

    variable gamerule_registry

    @shared.registry class GameRuleDoImmediateRespawn extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleDoTileDrops extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleFallDamage extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleKeepInventory extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleNaturalRegeneration extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleRandomTickSpeed extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleShowCoordinates extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleShowDeathMessages extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleSpawnRadius extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleSpectatorsGenerateChunks extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    @shared.registry class GameRuleHitTestSteps extends GameRule

        variable NAME

        variable VALUE_TYPE

        variable DEFAULT_VALUE

    class GameRuleHandler

        function __init__(self, world)

            variable self.table

                variable self.table[gamerule]
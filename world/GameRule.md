***GameRule.py - documentation - last updated on 14.5.2020 by uuk***
___

    class GameRuleDataType
        static function is_valid_value(cls, data: str)
        function copy(self)
        function save(self)
            
            :return: an json-able representation of this type
            

        function load(self, data)
            
            loads from previous saved data the gamerule
            :param data: the data saved
            


    class GameRuleTypeBoolean extends GameRuleDataType
        static function is_valid_value(cls, data: str)
        function __init__(self, data: str)
        function copy(self)
        function save(self)
        function load(self, data)

    class GameRuleTypeInt extends GameRuleDataType
        static function is_valid_value(cls, data: str)
        function __init__(self, data: str)
        function copy(self)
        function save(self)
        function load(self, data)

    class GameRule extends event.Registry.IRegistryContent

        variable TYPE


        variable VALUE_TYPE


        variable DEFAULT_VALUE

        function __init__(self, world)
        function set_status(self, value: str)

    variable gamerule_registry


    @G.registry class GameRuleDoImmediateRespawn extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE - todo: change to false when correct DeathScreen is implemented


    @G.registry class GameRuleDoTileDrops extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleFallDamage extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleKeepInventory extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleNaturalRegeneration extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleRandomTickSpeed extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleShowCoordinates extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleShowDeathMessages extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleSpawnRadius extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleSpectatorsGenerateChunks extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    @G.registry class GameRuleHitTestSteps extends GameRule

        variable NAME


        variable VALUE_TYPE


        variable DEFAULT_VALUE


    class GameRuleHandler
        function __init__(self, world)
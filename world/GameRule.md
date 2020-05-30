***GameRule.py - documentation - last updated on 30.5.2020 by uuk***
___

    class GameRuleDataType

        static
        function is_valid_value(cls, data: str): raise NotImplementedError()
                
                def copy(self): raise NotImplementedError()
                
                def save(self):

        function copy(self): raise NotImplementedError()
                
                def save(self):

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

        function save(self): return self.status
                
                def load(self, data): self.status = data
                
                
                class GameRuleTypeInt(GameRuleDataType):

        function load(self, data): self.status = data
                
                
                class GameRuleTypeInt(GameRuleDataType):

    class GameRuleTypeInt extends GameRuleDataType

        static
        function is_valid_value(cls, data: str)

        function __init__(self, data: str)

            variable self.status

        function save(self): return self.status
                
                def load(self, data): self.status = data
                
                
                class GameRule(event.Registry.IRegistryContent):

        function load(self, data): self.status = data
                
                
                class GameRule(event.Registry.IRegistryContent):

    class GameRule extends event.Registry.IRegistryContent

        variable TYPE

        variable VALUE_TYPE

        variable DEFAULT_VALUE

        function __init__(self, world)

            variable self.status

            variable self.world

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

            variable self.table

                variable self.table[gamerule]
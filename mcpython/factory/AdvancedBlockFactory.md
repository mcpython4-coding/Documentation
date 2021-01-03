***AdvancedBlockFactory.py - documentation - last updated on 24.6.2020 by uuk***
___

    @deprecation.deprecated("dev4-2", "a1.4.0") class IAdvancedBlockFactoryMode extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        variable REQUIRED_SETTINGS

        variable OPTIONAL_SETTINGS

        @deprecation.deprecated("dev4-2", "a1.4.0")
        static
        function work(cls, factory_instance, settings: dict)

    variable advanced_block_factory_mode_registry

    @G.registry @deprecation.deprecated("dev4-2", "a1.4.0") class FullCube extends IAdvancedBlockFactoryMode

        variable NAME

        variable REQUIRED_SETTINGS

        variable OPTIONAL_SETTINGS

        @deprecation.deprecated("dev4-2", "a1.4.0")
        static
        function work(cls, factory_instance, settings: dict)

    @G.registry @deprecation.deprecated("dev4-2", "a1.4.0") class SlabBlock extends IAdvancedBlockFactoryMode

        variable NAME

        variable REQUIRED_SETTINGS

        variable OPTIONAL_SETTINGS

        @deprecation.deprecated("dev4-2", "a1.4.0")
        static
        function work(cls, factory_instance, settings: dict)

    @deprecation.deprecated("dev4-2", "a1.4.0") class SimpleBlockFactoryHelper extends mcpython.factory.BlockFactory.BlockFactory
        
        representation of an BlockFactory linked to an AdvancedBlockFactory for returning back to the AdvancedBlockFactory


        @deprecation.deprecated("dev4-2", "a1.4.0")
        function __init__(self, master)

            variable self.master

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function getMaster(self)

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function finish(self, register=True)

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function default_finish(self)

    @deprecation.deprecated("dev4-2", "a1.4.0") class AdvancedBlockFactory
        
        factory class for blocks without the data FILES located. Generating when needed


        @deprecation.deprecated("dev4-2", "a1.4.0")
        function __init__(self)

            variable self.name

            variable self.block_factory

            variable self.mode

            variable self.settings

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function set_name(self, name: str)

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function getSimpleFactory(self)

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function setMode(self, name: str)

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function setModelConfig(self, key, value)

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function finish(self)

        @deprecation.deprecated("dev4-2", "a1.4.0")
        function finish_up(self)
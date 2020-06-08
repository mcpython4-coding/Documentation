***AdvancedBlockFactory.py - documentation - last updated on 8.6.2020 by uuk***
___

    class IAdvancedBlockFactoryMode extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        variable REQUIRED_SETTINGS

        variable OPTIONAL_SETTINGS

        static
        function work(cls, factory_instance, settings: dict)

    variable advanced_block_factory_mode_registry

    @G.registry class FullCube extends IAdvancedBlockFactoryMode

        variable NAME

        variable REQUIRED_SETTINGS

        variable OPTIONAL_SETTINGS

        static
        function work(cls, factory_instance, settings: dict)

    @G.registry class SlabBlock extends IAdvancedBlockFactoryMode

        variable NAME

        variable REQUIRED_SETTINGS

        variable OPTIONAL_SETTINGS

        static
        function work(cls, factory_instance, settings: dict)

    class SimpleBlockFactoryHelper extends mcpython.factory.BlockFactory.BlockFactory
        
        representation of an BlockFactory linked to an AdvancedBlockFactory for returning back to the AdvancedBlockFactory


        function __init__(self, master)

            variable self.master

        function getMaster(self)

        function finish(self, register=True)

        function default_finish(self)

    class AdvancedBlockFactory
        
        factory class for blocks without the data FILES located. Generating when needed


        function __init__(self)

            variable self.name

            variable self.block_factory

            variable self.mode

            variable self.settings

        function setName(self, name: str)

        function getSimpleFactory(self)

        function setMode(self, name: str)

        function setModelConfig(self, key, value)

        function finish(self)

        function finish_up(self)
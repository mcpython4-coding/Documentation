***FactoryBuilder.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class FactoryBuilder
        
        This system is for building classes for building other classes.
        It contains base classes for creating custom class-builder segments
        and default classes for them.
        You can do nearly anything with it what you want
        Performance-wise this is no critical section as it is only called during launch.
        Only critical is the IFactoryClassBuilder class modifying the target class of the builder,
        which is than send to the system


        class IFactoryClassModifier extends ABC

            static
            function apply(
                    cls,
                    builder: "FactoryBuilder",
                    target: typing.Type["FactoryBuilder.IFactory"],
                    ) -> typing.Type["FactoryBuilder.IFactory"]:

        class IFactoryConfigurator extends ABC

            function __init__(self, config_name: str)

                variable self.config_name

            function prepare(self, instance: "FactoryBuilder.IFactory")

            function get_configurable_target(self) -> typing.Any

        class InnerDefaultAttributeHelper extends IFactoryConfigurator

            function __init__(self, name: str, attr_name: str, value: typing.Callable)

                variable self.attr_name

                variable self.value

            function prepare(self, instance: "FactoryBuilder.IFactory")

            function get_configurable_target(self) -> typing.Any

            function configure(self)

        class AnnotationFactoryConfigurator extends IFactoryConfigurator

            function __init__(self, config_name: str)

                variable self.pool

            function __call__(self, target: typing.Callable)

            function get_configurable_target(self) -> typing.Any

            function configure(self, *args, **kwargs)

        class SetterFactoryConfigurator extends IFactoryConfigurator

            function __init__(
                    self, func_name: str, attr_name: str, assert_type=object, default_value=None
                    ):

                variable self.attr_name

                variable self.assert_type

                variable self.default_value

            function get_configurable_target(self) -> typing.Any

            function configure(self, instance, *args)

        class FunctionAnnotator extends IFactoryConfigurator

            function __init__(self, config_name: str, attr_name: str)

                variable self.attr_name

            function get_configurable_target(self) -> typing.Any

            function configure(self, instance, value=None)

        class FunctionStackedAnnotator extends IFactoryConfigurator

            function __init__(self, config_name: str, attr_name: str)

                variable self.attr_name

            function prepare(self, instance: "FactoryBuilder.IFactory")

            function get_configurable_target(self) -> typing.Any

            function configure(self, instance, value=None)

        class IFactoryClassBuilder extends ABC

            function prepare(self, instance: "FactoryBuilder.IFactory")

            function apply(
                    self,
                    cls: typing.Type["FactoryBuilder.IFactory.IBuildFactoryContent"],
                    instance: "FactoryBuilder.IFactory",
                    ) -> typing.Type["FactoryBuilder.IFactory.IBuildFactoryContent"]:

        class AnnotationFactoryClassBuilder extends IFactoryClassBuilder

            function __init__(self)

                variable self.pool

            function __call__(self, function)

            function apply(
                    self,
                    cls: typing.Type["FactoryBuilder.IFactory.IBuildFactoryContent"],
                    instance: "FactoryBuilder.IFactory",
                    ) -> typing.Type["FactoryBuilder.IFactory.IBuildFactoryContent"]:

                    variable cls

        class IFactoryCopyOperation extends ABC

            function operate(
                    self, old: "FactoryBuilder.IFactory", new: "FactoryBuilder.IFactory"
                    ):

        class DefaultFactoryCopyOperation extends IFactoryCopyOperation

            function __init__(self, key: str, operation=lambda e: copy.deepcopy(e))

                variable self.key

                variable self.operation

            function operate(
                    self, old: "FactoryBuilder.IFactory", new: "FactoryBuilder.IFactory"
                    ):

                    variable new.config_table[self.key]

        class IFactory extends ABC
            
            This is the core class for the system
            It manages all the cool stuff during factoring your class instance


            class IBuildFactoryContent extends ABC

            function __init__(self, master: "FactoryBuilder", *args, **kwargs)

            function __getattr__(self, item)

            function __setattr__(self, key, value)

            function set_template(self)

            function reset_template(self, all_templates=False)

            function set_to_template(self, pop=False)

            function copy(self) -> "FactoryBuilder.IFactory"

            function add_base_class(self, cls)

            function __copy__(self)

            function copy_from(self, other: "FactoryBuilder.IFactory")

            function finish(self)

                class BuildTarget extends FactoryBuilder.IFactory.IBuildFactoryContent

                    class BuildTarget extends BuildTarget,  base

                    variable BuildTarget

        function __init__(
                self,
                name: str,
                base_class: typing.Type[mcpython.common.event.Registry.IRegistryContent],
                do_with_results=shared.registry.__call__,
                ):

            variable self.name

            variable self.base_classes

            variable self.do_with_results

            variable self.factory_class: typing.Optional[FactoryBuilder.IFactory]

            variable self.factory_class_modifiers

            variable self.configurators: typing.List[FactoryBuilder.IFactoryConfigurator]

            variable self.class_builders: typing.List[FactoryBuilder.IFactoryClassBuilder]

            variable self.copy_operation_handlers

            variable self.dirty

        function register_modifier(self, modifier: typing.Type[IFactoryClassModifier])

        function register_configurator(self, configurator: IFactoryConfigurator)

        function register_class_builder(self, builder: IFactoryClassBuilder)

        function register_copy_operation_handler(self, handler: IFactoryCopyOperation)

        function __call__(self, *args, **kwargs) -> IFactory

        function create_class(self) -> typing.Type[IFactory]

            class Factory extends FactoryBuilder.IFactory

                function __init__(s, *args, **kwargs)

                variable Factory

        function build_configuration_table(self)

                variable self.config_access_table[

        function register_direct_copy_attributes(self, *attributes, operation=copy.deepcopy)
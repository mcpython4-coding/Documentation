***Registry.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Registry extends AbstractRegistry
        
        One registry for one object-type
        Holds information about it and does some magic to handle it
        Supports "XY" in registry and registry["XY"], but no write this way


        function __init__(
                self,
                name: str,
                registry_type_names: list,
                phase: typing.Optional[str] = None,
                injection_function=None,
                allow_argument_injection=False,
                class_based=True,
                dump_content_in_saves=True,
                register_to_shared_registry=True,
                sync_via_network=True,
                registry_sync_package_class=None,
                ):

            variable phase: typing.Optional[str]

            variable self.name

            variable self.phase

            variable self.registry_type_names

            variable self.injection_function

            variable self.allow_argument_injection

            variable self.entries

            variable self.full_entries

            variable self.class_based

            variable self.dump_content_in_saves

            variable self.sync_via_network

            variable self.registry_sync_package_class

                variable shared.registry.registries[name]

        function __contains__(self, item)

        function __getitem__(self, item)

        function is_valid(self, obj: IRegistryContent)

        function register(
                self,
                obj: typing.Union[IRegistryContent, typing.Type[IRegistryContent]],
                overwrite_existing=True,
                ):
            
            Registers an obj to this registry
            When locked, a RuntimeError is raised
            When an object with the name exists, and overwrite_existing is False, a RuntimeError is raised
            When the object does not extend IRegistryContent, a ValueError is raised
            When the object NAME-attribute is not set, a ValueError is raised


            variable self.entries[obj.NAME]

            variable self.full_entries[obj.NAME]

                variable self.full_entries[obj.NAME.split(":")[-1]]

        function entries_iterator(self) -> typing.Iterable[IRegistryContent]

        function elements_iterator(self) -> typing.Iterable[IRegistryContent]

        function lock(self)

        function unlock(self)

        function is_valid_key(self, key: str)

        function get(self, key: str, default=False)

        function create_deferred(self, mod_name: str, *args, **kwargs)

    class RegistryInjectionHolder

        function __init__(self, *args, **kwargs):  # todo: do something with the args and kwargs!
                self.args = args
                self.kwargs = kwargs
                self.injectable = None
                
                def __call__(self, obj):

            variable self.args

            variable self.kwargs

            variable self.injectable

        function __call__(self, obj)

    class RegistryHandler

        function __init__(self)

            variable self.registries

        function __call__(self, obj)

        function get_by_name(self, name: str) -> typing.Optional[Registry]

        function register(self, *args, **kwargs)

        function delayed_register(self, mod: str, phase: str)

        function create_deferred(self, registry: str, mod_name: str)

        function print_content(self, registry: str, namespace=None)

            variable r

                    variable element

    variable shared.registry
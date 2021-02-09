***Registry.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IRegistryContent extends mcpython.common.data.tags.ITagTarget.ITagTarget

        variable NAME

        variable TYPE

        static
        function on_register(cls, registry)

        variable INFO - can be used to display any special info in e.g. /registryinfo-command

        static
        function compressed_info(cls)

    class Registry

        function __init__(
                self,
                name: str,
                registry_type_names: list,
                phase: str,
                injection_function=None,
                allow_argument_injection=False,
                class_based=True,
                dump_content_in_saves=True,
                ):

            variable self.name

            variable self.phase

            variable self.registry_type_names

            variable self.injection_function

            variable self.allow_argument_injection

            variable self.entries

            variable self.full_entries

            variable self.locked

            variable self.class_based

            variable self.dump_content_in_saves

        function __contains__(self, item)

        function __getitem__(self, item)

        function is_valid(self, obj: IRegistryContent)

        function register(self, obj: IRegistryContent, override_existing=True)
            
            Registers an obj to this registry


            variable self.entries[obj.NAME]

            variable self.full_entries[obj.NAME]

                variable self.full_entries[obj.NAME.split(":")[-1]]

        function entries_iterator(self) -> typing.Iterable[IRegistryContent]

        function lock(self)

        function unlock(self)

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

        function __call__(self, *args, **kwargs)

        function get_by_name(self, name: str) -> typing.Optional[Registry]

        function register(self, *args, **kwargs)

        function async_register(self, mod: str, phase: str)

        function create_deferred(self, registry: str, mod_name: str)

    variable shared.registry

    class DeferredRegistryPipe

        function __init__(self, registry: Registry, modname: str)

            variable self.registry

            variable self.modname

        function run_later(self, lazy: typing.Callable[[], IRegistryContent])
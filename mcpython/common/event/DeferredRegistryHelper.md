***DeferredRegistryHelper.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class DeferredRegistry
        
        Base class for deferred registries


        function __init__(
                self, registry: AbstractRegistry, modname: str = "minecraft", base_factory=None
                ):

            variable self.registry

            variable self.modname

            variable self.base_factory

        function register_later(self, lazy: typing.Callable[[], IRegistryContent])

        function create_later(self, factory_instance)

        function create_named(self, name: str, factory_instance)

                variable name
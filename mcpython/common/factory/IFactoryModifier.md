***IFactoryModifier.py - documentation - last updated on 2.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IFactoryModifier

        function __init__(self)

            variable self.subscriber

        function on_apply(
                self,
                target: typing.Callable[
                [typing.Any, mcpython.common.event.Registry.IRegistryContent],
                mcpython.common.event.Registry.IRegistryContent,
                ],
                ):

        function apply(
                self,
                factory,
                instance: mcpython.common.event.Registry.IRegistryContent,
                ) -> mcpython.common.event.Registry.IRegistryContent:

                variable instance
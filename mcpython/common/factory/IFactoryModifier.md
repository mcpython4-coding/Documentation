***IFactoryModifier.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class IFactory

    class IFactoryModifier

        function __init__(self)

            variable self.subscriber

        function on_apply(
                self,
                target: typing.Callable[
                [IFactory, mcpython.common.event.Registry.IRegistryContent],
                mcpython.common.event.Registry.IRegistryContent,
                ],
                ):

        function apply(
                self,
                factory: IFactory,
                instance: mcpython.common.event.Registry.IRegistryContent,
                ) -> mcpython.common.event.Registry.IRegistryContent:

                variable instance
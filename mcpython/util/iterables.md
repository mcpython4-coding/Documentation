***iterables.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Stream

        static
        function from_iterator(cls, iterator: typing.Iterator)

        static
        function from_iterable(cls, iterable: typing.Iterable)

        function __init__(self, source: typing.Iterator)

            variable self.source

            variable self.operations

            variable self.stream_able

        function copy(self)

        function for_each(self, function: typing.Callable[[int, typing.Any], None])

        function for_each_store(self, function: typing.Callable[[int, typing.Any], typing.Any])

        function filter(self, function: typing.Callable[[int, typing.Any], bool])

        function slice(self, start: int, end: int, step: int)

        function merge(self, stream: "Stream")

        function sum(
                self, function: typing.Callable[[int, typing.Any], typing.Any] = lambda i, e: e
                ):

        function mul(
                self,
                function: typing.Callable[[int, typing.Any], typing.Any] = lambda i, e: e,
                default=1,
                ):

            function step(i, element)

            variable step.count

        function as_iterator(self) -> typing.Iterator

        function raw_iterator(self) -> typing.Iterator

        function execute_operation_on(self, element, i, op, args)

        function build(self)

        function as_list(self) -> typing.List
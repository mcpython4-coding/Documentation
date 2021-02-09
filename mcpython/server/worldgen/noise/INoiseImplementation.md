***INoiseImplementation.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IOctaveMerger

        static
        function pre_merge(
                cls,
                implementation: "INoiseImplementation",
                position,
                *generators: typing.Callable
                ) -> float:

        static
        function merge(cls, implementation: "INoiseImplementation", values) -> float

    class EQUAL_MERGER extends IOctaveMerger

        static
        function merge(cls, implementation: "INoiseImplementation", values)

    class GEO_EQUAL_MERGER extends IOctaveMerger

        static
        function merge(cls, implementation: "INoiseImplementation", values)

    class INNER_MERGE extends IOctaveMerger

        static
        function pre_merge(
                cls,
                implementation: "INoiseImplementation",
                position,
                *generators: typing.Callable
                ):

                variable implementation.merger_config

            variable value

                variable value

    class INoiseImplementation

        variable NAME

        function __init__(
                self,
                dimensions: int,
                octaves: int,
                scale: float,
                merger: IOctaveMerger = EQUAL_MERGER,
                ):

            variable merger: IOctaveMerger

            variable self.seed

            variable self.dimensions

            variable self.octaves

            variable self.scale

            variable self.merger

            variable self.merger_config

        function set_seed(self, seed: int)

        function calculate_position(self, position) -> float

        function calculate_area(
                self, start: typing.Tuple, end: typing.Tuple
                ) -> typing.Iterator[typing.Tuple[typing.Tuple, float]]:
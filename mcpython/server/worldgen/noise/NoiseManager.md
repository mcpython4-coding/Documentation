***NoiseManager.py - documentation - last updated on 3.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class NoiseImplementationWrapper extends INoiseImplementation

        function __init__(
                self,
                dimensions: int,
                octaves: int,
                scale: float,
                merger: IOctaveMerger = EQUAL_MERGER,
                ):

            variable merger: IOctaveMerger

            variable self.instance: typing.Optional[INoiseImplementation]

        function create_instance(self, cls: typing.Type[INoiseImplementation])

        function set_seed(self, seed: int)

        function calculate_position(self, position) -> float

        function calculate_area(
                self, start: typing.Tuple, end: typing.Tuple
                ) -> typing.Iterator[typing.Tuple[typing.Tuple, float]]:

    class NoiseManager

        function __init__(self)

            variable self.default_implementation: typing.Optional[str]

        function register_implementation(
                self, implementation: typing.Type[INoiseImplementation]
                ):

                variable self.default_implementation

            variable self.instances[implementation.NAME]

        function set_noise_implementation(self, name: str = None)

        function register_optional_implementation(self, package: str, cls_name: str)

        function create_noise_instance(
                self,
                ref_name: str,
                dimensions: int,
                octaves: int = 1,
                scale=1,
                merger: IOctaveMerger = EQUAL_MERGER,
                ) -> INoiseImplementation:

            variable instance

        function recalculate_noises(self)

        function calculate_part_seed(self, part: str)

            variable d

            variable mapped

            variable self.default_implementation

    variable manager
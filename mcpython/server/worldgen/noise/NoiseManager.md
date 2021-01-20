***NoiseManager.py - documentation - last updated on 20.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
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

        function serialize_seed_map(self) -> dict

        function deserialize_seed_map(self, data: dict)

    variable manager
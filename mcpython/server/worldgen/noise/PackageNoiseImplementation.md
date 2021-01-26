***PackageNoiseImplementation.py - documentation - last updated on 26.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class NoiseImplementation extends INoiseImplementation
        
        Noise implementation using the noise library


        variable NAME

        function __init__(self, *args, **kwargs)

            variable self.noises: typing.List[typing.Optional[int]]

        function set_seed(self, seed: int)

        function calculate_position(self, position) -> float
***OpenSimplexImplementation.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function create_getter(noise: opensimplex.OpenSimplex)

    class OpenSimplexImplementation extends INoiseImplementation
        
        Default noise implementation.
        todo: cache create_getter() results


        variable NAME

        function __init__(self, *args, **kwargs)

            variable self.noises: typing.List[typing.Optional[opensimplex.OpenSimplex]]

        function set_seed(self, seed: int)

        function calculate_position(self, position) -> float

            variable position
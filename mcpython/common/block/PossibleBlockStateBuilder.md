***PossibleBlockStateBuilder.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class PossibleBlockStateBuilder

        function __init__(self)

            variable self.states

            variable self.combination_stack

        function combinations(self)

        function add_comby(self, key: str, *states)

        function add_comby_bool(self, key: str)

        function add_comby_side(self, key: str)

        function add_comby_side_horizontal(self, key: str)

        function build_combys(self)

        function add_state(self, state)

        function build(self)
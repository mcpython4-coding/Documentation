***annotation.py - documentation - last updated on 28.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable TESTS

    class TestSetting

        function __init__(self, priority=0)

            variable self.priority

            variable self.run_helper

            variable self.target

        function no_result(self)

            variable self.run_helper

        function run_helper(self, func, *args, **kwargs)

        function expect_exception(self, exception)

            function run(func, args, kwargs)

            variable self.run_helper

        function expects_output(self, compare)

            variable self.run_helper

        function expects_output_check_func(self, check: typing.Callable[[typing.Any], bool])

            variable self.run_helper

        function __call__(self, func)

        function run(self)

        function __repr__(self)
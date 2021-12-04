***TestManager.py - documentation - last updated on 28.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class TestStage

        function __init__(self, manager: "TestManager", name: str, fail_on_single=False)

            variable self.manager

            variable self.name

            variable self.fail_on_single

            variable self.tests

        function add_module(self, module: str)

        function add_module_with_annotations(self, module: str)

        function run(self) -> bool

                    variable result

                    variable result

    class TestManager

        function __init__(self)

            variable self.tests: typing.List[TestStage]

        function stage(self, name: str, fail_on_single=False) -> TestStage

        function run(self)
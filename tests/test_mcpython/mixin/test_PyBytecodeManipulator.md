***test_PyBytecodeManipulator.py - documentation - last updated on 9.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class TestFunctionPatcher extends TestCase

        function test_apply_patches_simple(self)

            variable value

            class Test

                function wadd(self, x, y=1)

            variable test_obj
                Create an object of that class so we can be sure that it updates existing object-binds

            variable obj
                Apply a small patch to the function, replacing the + with a - in the code

            variable obj.code_string[12:13]

            variable value

        function test_library_mixin_with_constant(self)

            function test()

            variable replacement_code

            variable image

            variable obj

            variable replacement_code[1]

            variable obj.code_string

        function test_body_replacement(self)

            function a()

            function b()

            variable obj
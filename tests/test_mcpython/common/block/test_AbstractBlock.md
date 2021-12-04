***test_AbstractBlock.py - documentation - last updated on 16.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class TestAbstractBlock extends TestCase

        function test_module_import(self)

        function test_network_serializer(self)

            class TestBlock extends mcpython.common.block.AbstractBlock.AbstractBlock

                variable NAME

                variable model_state_set

                function get_model_state(self) -> dict

                function set_model_state(s, state: dict)

            variable buffer

            variable block

            variable block
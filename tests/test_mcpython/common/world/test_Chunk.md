***test_Chunk.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable test_block

    class FakeDim

        function get_world_height_range(self)

        function get_name(self)

        function get_block(self, position)

    class TestChunk extends TestCase

        function test_module_import(self)

        function test_entity_iterator(self)

            variable instance

            variable e

        function test_mark_dirty(self)

            variable instance

        function test_get_dimension(self)

            variable instance

        function test_get_position(self)

            variable instance

        function test_exposed_faces(self)

            variable instance

        function test_is_position_blocked(self)

            variable instance

        function test_add_block_by_str(self)

            variable dim

            variable instance

            variable b

        function test_add_block_by_instance(self)

            variable dim

            variable instance

            variable b

        function test_add_block_out_of_bounds(self)

            variable dim

            variable instance

        function test_add_block_non_integer(self)

            variable dim

            variable instance

        function test_add_block_air_via_None(self)

            variable dim

            variable instance

        function test_add_block_air_via_name(self)

            variable dim

            variable instance

        function test_add_block_air_via_namespaced_name(self)

            variable dim

            variable instance

        function test_add_block_invalid_name(self)

            variable dim

            variable instance

        function test_remove_block_by_position(self)

            variable dim

            variable instance

        function test_remove_block_by_instance(self)

            variable dim

            variable instance

            variable b

        function test_safe_removal_when_not_in_world(self)

            variable dim

            variable instance
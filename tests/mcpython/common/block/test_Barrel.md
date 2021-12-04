***test_Barrel.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class FakeInventoryHandler

        variable SHOWN

        static
        function add(cls, inventory)

        static
        function show(cls, inventory)

    class FakeCraftingHandler

        function __call__(self, *args, **kwargs)

    class FakeWorld

        static
        function get_dimension_by_name(cls, name: str)

        static
        function get_chunk_for_position(cls, position)

        static
        function exposed_faces(cls, position)

        static
        function mark_position_dirty(cls, position)

        static
        function get_active_dimension(cls)

    class TestBarrel extends TestCase

        function test_module_import(self)

        function test_on_block_added(self)

            variable shared.inventory_handler

            variable instance

            variable instance.position

            variable instance.set_to

            variable instance.set_to

            variable shared.world

        function test_on_player_interaction(self)

            variable shared.inventory_handler

            variable FakeInventoryHandler.SHOWN

            variable instance

            variable FakeInventoryHandler.SHOWN

        function test_model_state_serialization(self)

            variable shared.inventory_handler

            variable instance

            variable state
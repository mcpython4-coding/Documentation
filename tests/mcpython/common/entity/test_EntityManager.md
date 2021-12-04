***test_EntityManager.py - documentation - last updated on 23.8.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable shared.IS_TEST_ENV

    class BaseTestEntity

        function __init__(self, position=(0, 0, 0), child=None)

            variable self.uuid

            variable self.position

            variable self.parent

            variable self.child

            variable self.nbt_data

            variable self.dimension

            variable self.entity_height

        static
        function teleport(cls, position, force_chunk_save_update=False)

        static
        function tick(cls, dt: float)

        static
        function kill(cls, *_, **__)

    class TestEntityManager extends TestCase

        function __init__(self, func=None)

            variable self.entity_manager_instance

        function ensure_setup(self)

            variable self.entity_manager_instance

        function test_module_import(self)

        function test_add_entity_cls(self)

            variable shared.IS_CLIENT

            variable successful_callback

            class TestEntity extends BaseTestEntity

                static
                function init_renderers(cls)

            variable shared.IS_TEST_ENV

            variable shared.IS_TEST_ENV

        function test_spawn_entity_from_class(self)

            variable teleport_success

            class TestEntity extends BaseTestEntity

                static
                function teleport(cls, position, force_chunk_save_update=False)

            variable instance

        function test_tick(self)

            variable ticked

            class TestEntity extends BaseTestEntity

                static
                function tick(cls, dt: float)

            variable instance

        function test_tick_kill(self)

            variable killed

            class TestEntity extends BaseTestEntity

                static
                function kill(cls)

            variable instance

        function test_tick_child_handling(self)
            
            Checks if passenger handling works as it is expected
            Spawns to entities, links them and ticks the handler ones


            variable parent

            variable child

            variable parent.child

            variable child.parent

        function test_clear(self)

            variable instance
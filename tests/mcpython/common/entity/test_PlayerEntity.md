***test_PlayerEntity.py - documentation - last updated on 23.8.2021 by uuk***
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

    class FakeMod

        class eventbus

            static
            function subscribe(cls, *_, **__)

    class FakeModloader

        function __init__(self)

            variable self.finished

        function __call__(self, *args, **kwargs)

        function __getitem__(self, item)

    class TestPlayerEntity extends TestCase

        function test_module_import(self)

        function test_constructor(self)

            variable shared.IS_CLIENT

            variable shared.mod_loader

            variable instance

        function test_set_gamemode(self)

            variable shared.IS_CLIENT

            variable shared.mod_loader

            variable instance

        function test_set_active_inventory_slot(self)

            variable shared.IS_CLIENT

            variable shared.mod_loader

            variable instance

        function test_on_inventory_cleared(self)

            variable shared.IS_CLIENT

            variable shared.mod_loader

            variable instance

            variable instance.xp

            variable instance.xp_level
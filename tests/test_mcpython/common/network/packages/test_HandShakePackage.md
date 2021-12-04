***test_HandShakePackage.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class FakeWorld

        static
        function add_player(cls, *_, **__)

    class FakeModLoader

        variable mods

        static
        function add_to_add(cls, mod)

    class FakeMod

        variable name

        variable version

        variable server_only

    class TestClient2ServerHandshake extends TestCase

        function test_module_import(self)

        function test_setup(self)

            variable mcpython.common.config.VERSION_ID

            variable package

        function test_serialize(self)

            variable mcpython.common.config.VERSION_ID

            variable package

            variable buffer

            variable package2

        function test_handle_inner_compatible(self)

            variable handshake_back

            function answer(p)

            variable shared.world

            variable shared.mod_loader

            variable package

            variable package.answer

        function test_handle_inner_incompatible(self)

            variable handshake_back

            function answer(p)

            variable shared.world

            variable shared.mod_loader

            variable package

            variable package.answer

    class TestServer2ClientHandshake extends TestCase

        function test_setup_deny(self)

            variable shared.mod_loader

            variable FakeModLoader.mods

            variable package

        function test_setup_accept(self)

            variable shared.mod_loader

            variable FakeModLoader.mods

            variable package

        function test_serialize_deny(self)

            variable shared.mod_loader

            variable FakeModLoader.mods

            variable package

            variable buffer

            variable package

        function test_serialize_accept(self)

            variable shared.mod_loader

            variable FakeModLoader.mods

            variable package

            variable buffer

            variable package

        function test_handle_inner(self)
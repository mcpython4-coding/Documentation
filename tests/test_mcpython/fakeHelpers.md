***fakeHelpers.py - documentation - last updated on 10.1.2022 by uuk***
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

            variable cls.SHOWN

    class FakeCraftingHandler

        function __call__(self, *args, **kwargs)

    class FakeWorld

        variable entities

        variable dimension

        variable position

        static
        function get_dimension_by_name(cls, name: str)

        static
        function get_chunk_for_position(cls, position)

        static
        function exposed_faces(cls, position)

        static
        function exposed_faces_list(cls, position)

        static
        function exposed_faces_flag(cls, block)

        static
        function mark_position_dirty(cls, position)

        static
        function get_active_dimension(cls)

        static
        function get_name(cls)

        static
        function get_dimension(cls)

        static
        function get_dimension_id(cls)

    variable FakeWorld.dimension
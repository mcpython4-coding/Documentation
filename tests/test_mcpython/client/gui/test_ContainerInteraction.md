***test_ContainerInteraction.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable shared.IS_CLIENT

    variable shared.IS_TEST_ENV

    variable test_item

    variable test_item_2

    class FakeWindow

        variable mouse_position

        static
        function get_size(cls)

    class Inventory extends ContainerRenderer

        function add_slot(self, slot: Slot)

    class ContainerInteraction extends TestCase

        function setUp(self) -> None

        function tearDown(self) -> None

        function test_key_forward(self)

            variable invoked

            function test(x, y, button, modifiers)

                variable invoked

            variable s

            variable s.on_button_press

            variable shared.window.mouse_position

        function test_key_forward_not_hit(self)

            variable invoked

            function test(x, y, button, modifiers)

                variable invoked

            variable s

            variable s.on_button_press

            variable shared.window.mouse_position

        function test_left_pickup(self)

            variable shared.window.mouse_position

            variable self.interaction_manager.moving_itemstack

        function test_left_exchange(self)

            variable shared.window.mouse_position

            variable self.interaction_manager.moving_itemstack

        function test_right_pickup_half(self)

            variable shared.window.mouse_position

            variable self.interaction_manager.moving_itemstack
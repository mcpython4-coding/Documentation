***test_ContainerInteraction.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


        variable HAS_VISUAL

        variable HAS_VISUAL

        variable shared.IS_TEST_ENV

        variable shared.IS_CLIENT

        variable test_item

        variable test_item_2

        class FakeWindow

            variable mouse_position

            static
            function get_size(cls)

        class Inventory extends ContainerRenderer

            function add_slot(self, slot: Slot)

    @skipUnless(HAS_VISUAL, "rendering backend is needed") class ContainerInteraction extends TestCase

        function setUp(self) -> None

            variable self.interaction_manager

            variable shared.window

        function tearDown(self) -> None

            variable inventory

            variable invoked

            function test(x, y, button, modifiers)

                variable invoked

            variable shared.IS_CLIENT

            variable s

            variable s.on_button_press

            variable shared.window.mouse_position

            variable inventory

            variable invoked

            function test(x, y, button, modifiers)

                variable invoked

            variable shared.IS_CLIENT

            variable s

            variable s.on_button_press

            variable shared.window.mouse_position

            variable inventory

            variable shared.IS_CLIENT

            variable s

            variable shared.window.mouse_position

            variable self.interaction_manager.moving_itemstack

            variable inventory

            variable shared.IS_CLIENT

            variable s

            variable shared.window.mouse_position

            variable self.interaction_manager.moving_itemstack

            variable inventory

            variable shared.IS_CLIENT

            variable s

            variable shared.window.mouse_position

            variable self.interaction_manager.moving_itemstack
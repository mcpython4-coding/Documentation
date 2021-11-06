***AbstractItemRenderer.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractItemRenderer

        variable INVENTORY_RENDERING_MODE
            Possible: 2d and 3d

        function prepare_item_type_for_rendering(self, item_cls)

        function add_item_to_batch_for_inventory(
                self,
                slot,
                itemstack,
                batch: pyglet.graphics.Batch,
                offset: typing.Tuple[int, int],
                ):

        function remove_item_from_inventory(self, slot, itemstack, batch: pyglet.graphics.Batch)

        function add_item_to_world(
                self,
                slot,
                itemstack,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                ):

        function update_item_in_world(self, slot, itemstack, batch: pyglet.graphics.Batch)

        function remove_item_from_world(self, slot, itemstack, batch: pyglet.graphics.Batch)

        function add_hand_held_item(
                self,
                slot,
                itemstack,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                ):

        function update_hand_held_item(self, slot, itemstack, batch: pyglet.graphics.Batch)

        function remove_hand_held_item(self, slot, itemstack, batch: pyglet.graphics.Batch)
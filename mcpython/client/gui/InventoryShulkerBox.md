***InventoryShulkerBox.py - documentation - last updated on 20.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class InventoryShulkerBox extends mcpython.client.gui.InventoryChest.InventoryChest
        
        Class for the shulker box inventory
        Simply disables shulkerbox like items in the slots of the inventory


        function __init__(self)

                variable self.custom_name

            variable slots

                variable slot.disallowed_item_tags - inecraft:shulkerbox_like_items"]
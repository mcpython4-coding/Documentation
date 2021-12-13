***Chest.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable BBOX

    class Chest extends  IHorizontalOrientableBlock,  mcpython.client.rendering.blocks.ChestRenderer.IChestRendererSupport,  
        
        The Chest block class


        variable now: datetime - now

        variable is_christmas: bool
            if Christmas is today

        variable NAME: str

        variable MODEL_FACE_NAME

        variable HARDNESS

        variable ASSIGNED_TOOLS

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

            variable CHEST_BLOCK_RENDERER

            variable CHEST_BLOCK_RENDERER_CHRISTMAS

                    variable self.face_info.custom_renderer

                    variable self.face_info.custom_renderer

        function __init__(self)
            
            Creates a new BlockChest block


            variable self.inventory

            variable self.loot_table_link

            variable self.loot_table_link

                variable self.loot_table_link

        function can_open_inventory(self) -> bool
            
            Checks if the inventory can be opened
            :return: if the block can be opened


            variable instance

                    variable self.loot_table_link

        function get_inventories(self)

        function get_provided_slot_lists(self, side)

        function get_view_bbox(self)

        static
        function set_block_data(cls, instance, block)

        function on_request_item_for_block(self, itemstack)

                variable dimension

        static
        function modify_block_item(cls, factory)

    class TrappedChest extends Chest

        variable NAME
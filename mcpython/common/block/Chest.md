***Chest.py - documentation - last updated on 9.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


        class IChestRendererSupport

    variable BBOX
        the bounding box of the chest

    class Chest extends  IHorizontalOrientableBlock,  IChestRendererSupport,  SimpleInventoryWrappingContainer,  
        
        The Chest block class


        variable now: datetime
            now, for deciding to render the Christmas variant or not

        variable IS_CHRISTMAS: bool
            If Christmas is today, or not

        variable NAME: str

        variable MODEL_FACE_NAME

        variable HARDNESS

        variable ASSIGNED_TOOLS

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

            variable CHEST_BLOCK_RENDERER

            variable CHEST_BLOCK_RENDERER_CHRISTMAS

                variable cls.CHEST_BLOCK_RENDERER

                variable cls.CHEST_BLOCK_RENDERER_CHRISTMAS

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

        function get_view_bbox(self)

        static
        function set_block_data(cls, instance, block)

                variable itemstack.item.inventory

                variable dimension

        static
        function modify_block_item(cls, factory)

    class TrappedChest extends Chest

        variable NAME
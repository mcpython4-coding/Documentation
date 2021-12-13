***Barrel.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Barrel extends IAllDirectionOrientableBlock
        
        Class for the Barrel-Block
        Barrels are container blocks, with one front face


        variable NAME

        variable DEBUG_WORLD_BLOCK_STATES

        variable HARDNESS

        variable ASSIGNED_TOOLS

        function __init__(self)

            variable self.opened: bool
                if the barrel is open

            variable self.inventory
                the inventory instance

        function get_inventories(self)

        function get_provided_slot_lists(self, side)

        function set_model_state(self, state: dict)

                variable self.opened

        function get_model_state(self) -> dict

        static
        function set_block_data(cls, item, block)

        function on_request_item_for_block(self, itemstack)

                variable dimension
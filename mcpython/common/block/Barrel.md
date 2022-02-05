***Barrel.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Barrel extends IAllDirectionOrientableBlock,  SimpleInventoryWrappingContainer
        
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

                variable dimension

                variable self.opened

        function get_model_state(self) -> dict

                variable itemstack.item.inventory

        static
        function set_block_data(cls, item, block)
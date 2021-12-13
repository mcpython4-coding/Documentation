***Furnace.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class Furnace extends IHorizontalOrientableBlock
        
        Class for the furnace block


        variable FURNACE_RECIPES
            the list of recipe groups to use for this furnace

        variable NAME: str

        variable DEBUG_WORLD_BLOCK_STATES

        variable HARDNESS

        variable ASSIGNED_TOOLS

        function __init__(self)
            
            Creates a furnace block


            variable self.active

            variable self.inventory

        function get_model_state(self) -> dict

        function set_model_state(self, state: dict)

        function get_inventories(self)

        function get_provided_slot_lists(self, side)

                variable dimension

    class BlastFurnace extends Furnace

        variable NAME: str

        variable FURNACE_RECIPES

    class Smoker extends Furnace

        variable NAME: str

        variable FURNACE_RECIPES
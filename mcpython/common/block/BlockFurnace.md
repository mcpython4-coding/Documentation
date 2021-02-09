***BlockFurnace.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class BlockFurnace extends  mcpython.common.block.IHorizontalOrientableBlock.IHorizontalOrientableBlock 
        
        class for the furnace block


        variable FURNACE_RECIPES: list

        variable NAME: str

        variable DEBUG_WORLD_BLOCK_STATES

        function __init__(self)
            
            creates an furnace block in the world


            variable self.active

            variable self.inventory

        function get_model_state(self) -> dict

        function set_model_state(self, state: dict)

        function on_player_interaction(self, player, button, modifiers, exact_hit) -> bool

        function get_inventories(self)

        function get_provided_slot_lists(self, side)

        function on_block_remove(self, reason)

    class BlastFurnace extends BlockFurnace

        variable NAME: str

        variable FURNACE_RECIPES: list

    class Smoker extends BlockFurnace

        variable NAME: str

        variable FURNACE_RECIPES: list

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
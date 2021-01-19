***BlockBarrel.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class BlockBarrel extends AbstractBlock.AbstractBlock
        
        class for the Barrel-Block


        variable NAME: str - the name of the block

        variable DEBUG_WORLD_BLOCK_STATES

        variable HARDNESS

        variable ASSIGNED_TOOLS

        function __init__(self)
            
            Creates an new BlockBarrel-class


            variable self.opened: bool - if the barrel is open

            variable self.inventory

            variable self.facing: str - the direction the block faces to

        function on_block_added(self)

        function on_player_interaction(
                self, player, button: int, modifiers: int, hit_position: tuple
                ):

        function get_inventories(self)

        function get_provided_slot_lists(self, side)

        function set_model_state(self, state: dict)

        function get_model_state(self) -> dict

        static
        function set_block_data(cls, item, block)

        function on_request_item_for_block(self, itemstack)

        function on_block_remove(self, reason)

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
***BlockChest.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    variable BBOX

    class BlockChest extends AbstractBlock.AbstractBlock
        
        The Chest block class


        variable now: datetime - now

        variable is_christmas: bool

        variable NAME: str - the name of the chest

        variable IS_SOLID

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable ASSIGNED_TOOLS

        variable DEBUG_WORLD_BLOCK_STATES

        variable DEFAULT_FACE_SOLID

        function __init__(self)
            
            Creates an new BlockChest


            variable self.front_side

            variable self.inventory

            variable self.loot_table_link

        function on_block_added(self)

        function can_open_inventory(self) -> bool
            
            Checks if the inventory can be opened
            :return: if the block can be opened


        function on_player_interaction(
                self, player, button: int, modifiers: int, hit_position: tuple
                ):

                    variable self.loot_table_link

        function get_inventories(self)

        function get_provided_slot_lists(self, side)

        function set_model_state(self, state: dict)

        function get_model_state(self) -> dict

        function get_view_bbox(self)

        static
        function set_block_data(cls, instance, block)

        function on_request_item_for_block(self, itemstack)

        function on_block_remove(self, reason)

        static
        function modify_block_item(cls, factory)

        function get_save_data(self)

        function load_data(self, data)

                variable self.loot_table_link

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
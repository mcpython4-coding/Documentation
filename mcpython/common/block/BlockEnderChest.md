***BlockEnderChest.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class BlockEnderChest extends AbstractBlock.AbstractBlock
        
        class for the ender chest


        variable NAME

        variable DEFAULT_FACE_SOLID

        variable HARDNESS

        variable MINIMUM_TOOL_LEVEL

        variable ASSIGNED_TOOLS

        function __init__(self)

            variable self.front_side

            variable self.inventory

        function on_block_added(self)

        function on_player_interaction(
                self, player, button: int, modifiers: int, hit_position: tuple
                ):

        function get_inventories(self)

        function get_provided_slots(self, side)

        function set_model_state(self, state: dict)

        function get_model_state(self) -> dict

        variable DEBUG_WORLD_BLOCK_STATES

        function get_view_bbox(self)

        function on_block_remove(self, reason)

    @shared.mod_loader("minecraft", "stage:block:load")
    function load()
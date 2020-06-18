***player.py - documentation - last updated on 18.6.2020 by uuk***
___

    @globals.registry class Player extends mcpython.entity.Entity.Entity

        variable RENDERER

        variable NAME

        variable SUMMON_ABLE

        variable GAMEMODE_DICT: dict

        function __init__(self, name="unknown", dimension=None)

            variable self.name: str

            variable self.gamemode: int

            variable self.hearts: int

            variable self.hunger: int

            variable self.xp: int

            variable self.xp_level: int

            variable self.armor_level

            variable self.armor_toughness

            variable self.fallen_since_y

            variable self.inventories: dict

            variable self.inventory_order: list - an ([inventoryindexname: str], [reversed slots: bool}) list

            variable self.iconparts

            variable self.active_inventory_slot: int

        function hotkey_get_position(self)

        function toggle_gamemode(self)

        function create_inventories(self)

            variable hotbar

            variable self.inventories['main']

            variable self.inventories['chat']

            variable self.inventories["enderchest"]

            variable self.inventories["crafting_table"]

        function load_xp_icons(self)

        function set_gamemode(self, gamemode: int or str)

        function get_needed_xp_for_next_level(self) -> int

        function add_xp(self, xp: int)

        function add_xp_level(self, xp_levels: int)

        function pick_up(self, itemstack: mcpython.gui.ItemStack.ItemStack) -> bool
            
            adds the item onto the itemstack
            :param itemstack: the itemstack to add
            :return: either successful or not


                variable inventory

                variable slots

                            variable m

                            variable delta

                variable inventory

                variable slots

        function set_active_inventory_slot(self, slot: int)

        function get_active_inventory_slot(self)

        function kill(self, test_totem=True)

        function _get_position(self)

        function _set_position(self, position)

        function damage(self, hearts: int, check_gamemode=True, reason=None)
            
            damage the player and removes the given amount of hearts (two hearts are one full displayed hart)


        function reset_moving_slot(self)

        function set_to_spawn_point(self)

        function tell(self, msg: str)

        function draw(self, position=None, rotation=None, full=None)

        function __del__(self)

        function __str__(self)
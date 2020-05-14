***player.py - documentation - last updated on 14.5.2020 by uuk***
___

    @globals.registry class Player extends entity.Entity.Entity

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

            variable self.iconparts

        function set_gamemode(self, gamemode: int or str)

            variable gamemode

                variable globals.window.flying

                variable globals.window.flying

                variable globals.window.flying

            variable self.gamemode

        function get_needed_xp_for_next_level(self) -> int

        function add_xp(self, xp: int)

                    variable xp

        function add_xp_level(self, xp_levels: int)

        function pick_up(self, itemstack: gui.ItemStack.ItemStack) -> bool
            
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

            variable self.active_inventory_slot

        function get_active_inventory_slot(self)

        function kill(self, test_totem=True)

                    variable self.hearts

                    variable self.hunger

                    variable self.hearts

                    variable self.hunger

            variable sector

            variable self.position

            variable self.active_inventory_slot

            variable globals.window.dy

            variable self.xp
                todo: drop xp

            variable self.xp_level

            variable self.hearts

            variable self.hunger

            variable globals.window.flying

            variable self.armor_level

            variable self.armor_toughness

            variable sector

        function _get_position(self)

        function _set_position(self, position)

            variable self.position

        function damage(self, hearts: int, check_gamemode=True, reason=None)
            
            damage the player and removes the given amount of hearts (two hearts are one full displayed hart)


            variable hearts

        function reset_moving_slot(self)

        function tell(self, msg: str)

        function draw(self, position=None, rotation=None, full=None)

            variable old_position

            variable rotation_whole

        function __del__(self)
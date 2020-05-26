***player.py - documentation - last updated on 26.5.2020 by uuk***
___

    @globals.registry class Player extends entity.Entity.Entity
        
        entity class for the player


        variable RENDERER - the renderer for the entity

        variable NAME: str - the entity name

        variable SUMMON_ABLE: bool - we can't summon the player by using "/summon minecraft:player"

        function __init__(self, name: str = "unknown", dimension=None)
            
            will create an new Player-entity instance
            :param name: the name of the player
            :param dimension: the dimension in or None for the active dimension
            WARNING: dimension will get NOT optional in the future


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

        @globals.EnumSide.CLIENT function hotkey_get_position(self)
            
            hotkey implementation for copying the player position to the clipboard
            :return:


        @globals.EnumSide.SERVER function toggle_gamemode(self)
            
            will toggle between gamemode 1 and 3 when in one of these gamemodes


        @globals.EnumSide.CLIENT function create_inventories(self)
            
            create the player inventories


            variable hotbar

            variable self.inventories['main']

            variable self.inventories['chat']

            variable self.inventories["enderchest"]

            variable self.inventories["crafting_table"]

        @globals.EnumSide.CLIENT function load_xp_icons(self)
            
            will load the icons needed


        @globals.EnumSide.SERVER function set_gamemode(self, gamemode: int or str)
            
            will set the gamemode of the player
            :param gamemode: the gamemode to set


        @globals.EnumSide.SERVER function teleport(self, position=None, dimension=None, force_chunk_save_update=False)
            
            called when the entity should be teleported
            :param position: the position to teleport to
            :param dimension: to which dimension-id to teleport to, if None, no dimension change is used
            :param force_chunk_save_update: if the system should force to update were player data is stored


        @globals.EnumSide.SERVER function get_needed_xp_for_next_level(self) -> int
            
            will return the xp needed for the next xp level


        @globals.EnumSide.SERVER function add_xp(self, xp: int)
            
            will add xp to the player's xp level
            :param xp: the xp to add


        @globals.EnumSide.SERVER function add_xp_level(self, xp_levels: int)
            
            add an amount of xp levels
            :param xp_levels:
            :return:


        @globals.EnumSide.SERVER function pick_up(self, itemstack: gui.ItemStack.ItemStack) -> bool
            
            adds the item onto the itemstack
            :param itemstack: the itemstack to add
            :return: either successful or not


                variable inventory

                variable slots

                            variable m

                            variable delta

                variable inventory

                variable slots

        @globals.EnumSide.CLIENT function set_active_inventory_slot(self, slot: int)

        @globals.EnumSide.CLIENT function get_active_inventory_slot(self)

        @globals.EnumSide.SERVER function kill(self, test_totem: bool = True)
            
            will kill the player
            :param test_totem: if an totem check should be made


        function _get_position(self)

        function _set_position(self, position)

        @globals.EnumSide.SERVER function damage(self, hearts: int, check_gamemode=True, reason=None)
            
            damage the player and removes the given amount of hearts (two hearts are one full displayed hart)


        @globals.EnumSide.CLIENT function reset_moving_slot(self)

        function tell(self, msg: str)

        @globals.EnumSide.CLIENT function draw(self, position=None, rotation=None, full=None)

        function __del__(self)
***PlayerEntity.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @shared.registry class PlayerEntity extends mcpython.common.entity.AbstractEntity.AbstractEntity

        variable RENDERER

        static
        function init_renderers(cls)

        variable NAME

        variable SUMMON_ABLE

        variable GAMEMODE_DICT: dict

        function __init__(self, name="unknown", dimension=None)

            variable self.name: str - the name of the player

            variable self.gamemode: int - the current gamemode

            variable self.hearts: int

            variable self.hunger: int

            variable self.xp: int

            variable self.xp_level: int

            variable self.armor_level

            variable self.armor_toughness

            variable self.in_nether_portal_since

            variable self.should_leave_nether_portal_before_dim_change

            variable self.flying - are we currently flying?

            variable self.fallen_since_y - how far did we fall?

            variable self.active_inventory_slot: int
                which slot is currently selected

            variable self.inventory_hotbar

            variable self.inventory_main

            variable self.inventory_enderchest

            variable self.inventory_chat

            variable self.inventory_crafting_table

            variable self.inventory_order

        function hotkey_get_position(self)

        function toggle_gamemode(self)
            
            Toggles between gamemode 1 and 3, used internally for the hotkey F3+N


        function create_inventories(self)
            
            Helper method for setting up the player inventory
            todo: can we re-use inventories from previous players?


            variable self.inventory_hotbar

            variable self.inventory_main

            variable self.inventory_chat

            variable self.inventory_enderchest

            variable self.inventory_crafting_table

            variable self.inventory_order

        function set_gamemode(self, gamemode: typing.Union[int, str])
            
            Sets the player gamemodes and the assigned properties


                    variable self.flying

                    variable self.flying

                    variable self.flying

                variable self.gamemode

        function get_needed_xp_for_next_level(self) -> int

        function add_xp(self, xp: int)

        function add_xp_level(self, xp_levels: int)

        function pick_up_item(
                self,
                itemstack: typing.Union[
                mcpython.common.container.ItemStack.ItemStack, mcpython.client.gui.Slot.Slot
                ],
                ) -> bool:
            
            Adds the item onto the itemstack
            :param itemstack: the itemstack to add
            :return: either successful or not


                variable itemstack

                variable slots

                            variable m

                            variable delta

                variable slots

        function set_active_inventory_slot(self, slot: int)
            
            Sets the active inventory slot by ID (0-8)


        function get_active_inventory_slot(self)
            
            Gets the slot of the selected slot


        function kill(
                self,
                drop_items=True,
                kill_animation=True,
                damage_source: mcpython.common.entity.DamageSource.DamageSource = None,
                test_totem=True,
                force=False,
                ):

                variable a
                    todo: add effects of totem
                    todo: add list to player of possible slots with possibility of being callable

                variable b

                    variable self.hearts

                    variable self.hunger

            variable sector

            variable self.active_inventory_slot

            variable shared.window.dy

            variable self.xp
                todo: drop parts of the xp

            variable self.xp_level

            variable self.hearts

            variable self.hunger

            variable self.flying - todo: add event for this

            variable self.armor_level

            variable self.armor_toughness

            variable sector

        function _get_position(self)

        function _set_position(self, position)

        function damage(self, hearts: int, check_gamemode=True, reason=None)
            
            Damage the player and removes the given amount of hearts (two hearts are one full displayed hart)


        function reset_moving_slot(self)

        function move_to_spawn_point(self)

        function tell(self, msg: str)

        function draw(self, position=None, rotation=None, full=None)

        function __str__(self)

        function on_inventory_cleared(self)

        function teleport(self, position, dimension=None, force_chunk_save_update=False)

        function get_inventories(self) -> list
***PlayerEntity.py - documentation - last updated on 14.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @shared.registry class PlayerEntity extends mcpython.common.entity.AbstractEntity.AbstractEntity

        variable RENDERER

        static
        function init_renderers(cls)

        variable NAME

        variable SUMMON_ABLE

        variable GAMEMODE_DICT: dict

        variable BOUNDING_BOX

        function __init__(self, name="unknown", dimension=None)

            variable self.is_in_init

            variable self.name: str - the name of the player

            variable self.gamemode: int - the current gamemode

            variable self.hearts: int

            variable self.hunger: float

            variable self.xp: int

            variable self.xp_level: int

            variable self.armor_level: float

            variable self.armor_toughness: float

            variable self.in_nether_portal_since: typing.Optional[float]

            variable self.should_leave_nether_portal_before_dim_change

            variable self.flying
                are we currently flying?

            variable self.fallen_since_y: float
                how far did we fall?

            variable self.strafe
                Strafing is moving lateral to the direction you are facing,
                e.g. moving to the left or right while continuing to face forward.
                
                First element is -1 when moving forward, 1 when moving back, and 0
                otherwise. The second element is -1 when moving left, 1 when moving
                right, and 0 otherwise.

            variable self.active_inventory_slot: int
                which slot is currently selected

            variable self.inventories_created
                the different parts of the player inventory
                todo: use only containers here

            variable self.inventory_hotbar

            variable self.inventory_main

            variable self.inventory_enderchest

            variable self.inventory_chat

            variable self.inventory_crafting_table

            variable self.inventory_order

            variable self.is_in_init

        function get_jump_speed(self)

        function get_collision_box(self)

        function get_motion_vector(self) -> tuple
            
            Returns the current motion vector indicating the velocity of the
            player.
            :return: vector: Tuple containing the velocity in x, y, and z respectively.
            todo: integrate into player movement


        function __repr__(self)

        function write_to_network_buffer(self, buffer: WriteBuffer)

        function read_from_network_buffer(self, buffer: ReadBuffer)

            variable self.name

            variable self.gamemode

            variable self.hearts

            variable self.hunger

            variable self.xp

            variable self.xp_level

            variable self.armor_level

            variable self.armor_toughness

            variable self.flying

            variable self.fallen_since_y

            variable self.active_inventory_slot

        function create_update_package(self) -> PlayerUpdatePackage

                variable package.gamemode

        function write_update_package(self, package: PlayerUpdatePackage)

        function send_update_package_when_client(self)

        function send_update_package_when_server(self, update_flags=-1)

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

        function init_creative_tabs(self)

        function set_gamemode(self, gamemode: typing.Union[int, str])
            
            Sets the player game-modes and the assigned properties
            todo: something better here?


                    variable self.flying

                    variable self.flying

                    variable self.flying

                variable self.gamemode

        function get_needed_xp_for_next_level(self) -> int
            
            :return: the xp amount needed to reach the next xp level


        function add_xp(self, xp: int)

        function add_xp_level(self, xp_levels: int)

        function clear_xp(self)

        function pick_up_item(
                self,
                itemstack: typing.Union[
                mcpython.common.container.ResourceStack.ItemStack,
                mcpython.client.gui.Slot.Slot,
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
            Clamped in the range when out of range


        function get_active_inventory_slot(self)
            
            Gets the slot of the selected slot


        function kill(
                self,
                drop_items=True,
                kill_animation=True,
                damage_source: mcpython.common.entity.DamageSource.DamageSource = None,
                test_totem=True,
                force=False,
                internal=False,
                ):

                variable a
                    todo: add effects of totem
                    todo: add list to player of possible slots with possibility of being callable
                    todo: add tag for this functionality

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

        function teleport_to_spawn_point(self)

            variable h

                variable h

            variable self.position

        function tell(self, msg: str)

        function draw(self, position=None, rotation=None, full=None)

            variable rotation_whole

        function __str__(self)

        function on_inventory_cleared(self)

        function teleport(self, position, dimension=None, force_chunk_save_update=False)

        function get_inventories(self) -> list
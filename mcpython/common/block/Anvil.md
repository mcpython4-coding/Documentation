***Anvil.py - documentation - last updated on 6.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractAnvil extends IFallingBlock.IFallingBlock
        
        Base class for all anvils
        Mods are allowed to implement this for their own anvils
        todo: add inventory & enable saving of it (with data fixer for it)


        variable NETWORK_BUFFER_SERIALIZER_VERSION

        variable HARDNESS

        variable BLAST_RESISTANCE

        variable ASSIGNED_TOOLS

        variable DEBUG_WORLD_BLOCK_STATES

        variable BREAK_CHANCE

        variable BREAKS_BLOCK_RESIST

        variable BROKEN_BLOCK

        variable IS_SOLID

        variable DEFAULT_FACE_SOLID

        function __init__(self)

            variable self.opened: bool - if the barrel is open

            variable self.inventory - todo: add anvil inventory

            variable self.broken_count

        function on_block_added(self)

        function on_anvil_use(self)

        function write_to_network_buffer(self, buffer: WriteBuffer)

        function read_from_network_buffer(self, buffer: ReadBuffer)

            variable self.broken_count
                self.inventory.read_from_network_buffer(buffer)

            variable self.facing

        function on_player_interaction(
                self, player, button: int, modifiers: int, hit_position: tuple, itemstack
                ):
                
            if button == mouse.RIGHT and not modifiers & (
                key.MOD_SHIFT | key.MOD_ALT | key.MOD_CTRL
            ):
                shared.inventory_handler.show(self.inventory)
                return True
            else:


        function get_inventories(self)

        function get_provided_slot_lists(self, side)

        function set_model_state(self, state: dict)

                    variable self.facing

                    variable self.facing

        function get_model_state(self) -> dict

        static
        function set_block_data(cls, item, block)

        function on_request_item_for_block(self, itemstack)

        function on_block_remove(self, reason)

    class Anvil extends AbstractAnvil

        variable NAME

        variable BREAK_CHANCE

        variable BROKEN_BLOCK

    class ChippedAnvil extends AbstractAnvil

        variable NAME

        variable BREAK_CHANCE

        variable BROKEN_BLOCK

    class DamagedAnvil extends AbstractAnvil

        variable NAME

        variable BREAK_CHANCE
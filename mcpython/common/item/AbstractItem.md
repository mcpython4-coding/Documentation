***AbstractItem.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    class AbstractItem extends mcpython.common.event.Registry.IRegistryContent

        variable TYPE

        variable STACK_SIZE

        variable HAS_BLOCK

        variable ITEM_NAME_COLOR

        static
        function get_used_texture_files(
                cls,
                ):  # WARNING: will be removed during item rendering update; todo: make attribute
                return [cls.get_default_item_image_location()]
                
                @staticmethod
                def get_default_item_image_location() -> str:  # WARNING: will be removed during item rendering update
                raise NotImplementedError()
                
                def __init__(self):

        static
        function get_default_item_image_location() -> str:  # WARNING: will be removed during item rendering update
                raise NotImplementedError()
                
                def __init__(self):

        function __init__(self)

            variable self.stored_block_state

            variable self.can_destroy

            variable self.can_be_set_on

        function check_can_be_set_on(self, block, player)

        function check_can_destroy(self, block, player)

        function __eq__(self, other)

        function on_clean(self, itemstack)

        function on_copy(self, old_itemstack, new_itemstack)

        function get_active_image_location(
                self,
                ):  # WARNING: will be removed during item rendering update
                return self.get_default_item_image_location()
                
                def get_block(self) -> str:

        function get_block(self) -> str

        function on_player_interact(self, player, block, button, modifiers) -> bool
            
            called when the player tries to use the item
            :param player: the player interacting
            :param block: the block in focus, may be None
            :param button: the button used
            :param modifiers: the modifiers used
            :return: if default logic should be interrupted
            todo: add an exact_hit-parameter


        function on_block_broken_with(self, itemstack, player, block)

        function on_set_from_item(self, block)

        function get_data(self)

        function set_data(self, data)

        function get_tooltip_provider(self)

        function get_additional_tooltip_text(self, stack, renderer) -> list
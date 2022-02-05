***AbstractItem.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractItem extends  mcpython.common.event.api.IRegistryContent,  ICapabilityContainer,  IBufferSerializeAble,  ABC,  

        variable VERSION

        variable TYPE

        variable CAPABILITY_CONTAINER_NAME

        variable STACK_SIZE

        variable HAS_BLOCK

        variable ITEM_NAME_COLOR

        variable BOUND_ITEM_RENDERER
            Attribute storing an AbstractItemRenderer instance for rendering this item
            May only be set on client due to loading pyglet

        static
        function get_used_texture_files(
                cls,
                ):  # WARNING: will be removed during item rendering update; todo: make attribute
                return [cls.get_default_item_image_location()]
                
                @classmethod
                def get_default_item_image_location(
                cls,
                ) -> str:  # WARNING: will be removed during item rendering update
                return "assets/{}/textures/item/{}.png".format(*cls.NAME.split(":"))
                
                @classmethod
                def __init_subclass__(cls, **kwargs):

        static
        function get_default_item_image_location(
                cls,
                ) -> str:  # WARNING: will be removed during item rendering update
                return "assets/{}/textures/item/{}.png".format(*cls.NAME.split(":"))
                
                @classmethod
                def __init_subclass__(cls, **kwargs):

        static
        function __init_subclass__(cls, **kwargs)

        function __init__(self)

            variable self.stored_block_state

            variable self.can_destroy

            variable self.can_be_set_on

        function draw_in_inventory(
                self, itemstack, position: typing.Tuple[int, int], scale: float
                ):

            variable version

                    variable fixer

                    variable write

                    variable buffer

                    variable version

            variable can_destroy_flag

            variable can_be_set_on_flag

                variable self.can_destroy

                variable self.can_be_set_on

            variable can_destroy_flag

            variable can_be_set_on_flag

                variable self.can_destroy

                variable self.can_be_set_on

            variable can_destroy_flag

            variable can_be_set_on_flag

            variable can_destroy_flag

            variable can_be_set_on_flag

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
            
            Called when the player tries to use the item by pressing a mouse button
            :param player: the player interacting
            :param block: the block in focus, may be None if no block is in range
            :param button: the button used
            :param modifiers: the modifiers used
            :param itemstack: the itemstack used
            :param previous: the precious block position hit with, or None if no block was hit
            :return: if default logic should be interrupted
            todo: pass full hit info into here


        function get_tooltip_provider(self)

        function get_additional_tooltip_text(self, stack, renderer) -> list
***HoveringItemBox.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class IHoveringItemBoxDefinitionPlugin
        
        Abstract class for manipulating an existing HoveringDefinition text.
        Use addPlugin(<instance>) on the final class to register your plugin.
        Saver than replacing the entry for the item.
        Multiple plugins can co-exists. They are applied in order of registration.
        Please make sure that you look for changes before applying your changes (as you might interfere with stuff from another plugin)


        function manipulateShownText(
                self, slot: mcpython.common.container.ItemStack.ItemStack, text: list
                ):

    class IHoveringItemBoxDefinition
        
        Base class for an ToolTip text provider. Should generate out of an ItemStack an html-string-list


        variable PLUGINS

        static
        function setup(cls)
            
            Call this method on every child to set up


        function getHoveringText(
                self, itemstack: mcpython.common.container.ItemStack.ItemStack
                ) -> list:

        static
        function addPlugin(cls, plugin: IHoveringItemBoxDefinitionPlugin)

    class DefaultHoveringItemBoxDefinition extends IHoveringItemBoxDefinition
        
        Class representing an normal translate-able-configure-able tooltip with an given default style and layout
        Uses the default Item-class-methods to render certain stuff


        function __init__(
                self,
                default_style="<font color='{color}'>{text}</font>",
                localize_builder="item.{}.{}",
                ):

            variable self.localize_builder

            variable self.default_style

        function getHoveringText(
                self, itemstack: mcpython.common.container.ItemStack.ItemStack
                ) -> list:

            variable item_name

            variable raw

            variable localized_name

                variable localized_name

                variable localized_name

            variable tags

                variable block_cls

                variable tags

            variable stuff

    variable DEFAULT_ITEM_TOOLTIP
        Both of these are the default renderers for items and block-item respectively.
        Feel free to override, but use IHoveringItemBoxDefinitionPlugin were possible instead
        Everything here MUST extend IHoveringItemBoxDefinition.

    variable DEFAULT_BLOCK_ITEM_TOOLTIP

    class HoveringItemBoxProvider
        
        Class for generating these tool-tips like in mc
        Uses above IHoveringItemBoxDefinition class to generate for itemstacks


        function __init__(self)

            variable self.last_slot

            variable self.cached_text

            variable self.cached_provider

            variable self.labels

            variable self.label_batch

            variable self.bg_rectangle

        function renderFor(
                self, itemstack: mcpython.common.container.ItemStack.ItemStack, position
                ):
            
            will render the ItemBoxProvider for an given slot
            :param itemstack: the slot to render over
            :param position: the position to render at, or None if calculated from slot


                variable self.last_slot

                variable self.cached_provider

                variable self.cached_text

                    variable self.labels

                    variable text

                    variable self.labels[i].document

                    variable self.labels[i].anchor_y

                variable self.bg_rectangle.width

                variable self.bg_rectangle.height

            variable self.bg_rectangle.position

            variable y

                variable label.x

                variable label.y

        function eraseCache(self)
            
            Can be used to re-calculate the text of the tool tip

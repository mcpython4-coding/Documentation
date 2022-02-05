***HoveringItemBox.py - documentation - last updated on 5.2.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class IHoveringItemBoxDefinitionPlugin
        
        Abstract class for manipulating an existing HoveringDefinition text.
        Use addPlugin(<instance>) on the final class to register your plugin.
        Saver than replacing the entry for the item.
        Multiple plugins can co-exists. They are applied in order of registration.
        Please make sure that you look for changes before applying your changes (as you might interfere with stuff from another plugin)


        function manipulateShownText(self, slot: ItemStack, text: list)

    class IHoveringItemBoxDefinition
        
        Base class for an ToolTip text provider. Should generate out of an ItemStack an html-string-list


        variable PLUGINS

        static
        function setup(cls)
            
            Call this method on every child to set up


        function getHoveringText(self, itemstack: ItemStack) -> list

        static
        function addPlugin(cls, plugin: IHoveringItemBoxDefinitionPlugin)

    class DefaultHoveringItemBoxDefinition extends IHoveringItemBoxDefinition
        
        Class representing an normal translate-able-configure-able tooltip with an given default style and layout
        Uses the default Item-class-methods to render certain stuff
        Subclasses can safely override getAdditionalText() to insert informal text, without breaking
        mods mixin into the getHoveringText() method


        function __init__(
                self,
                default_style="<font color='{color}'>{text}</font>",
                localize_builder="item.{}.{}",
                ):

            variable self.localize_builder

            variable self.default_style

        function getAdditionalText(self, itemstack: ItemStack) -> typing.List[str]

        function getHoveringText(self, itemstack: ItemStack) -> typing.List[str]

            variable item_name

                variable raw

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
        Create a new instance for rendering 2 or more at the same time


        function __init__(self)

            variable self.last_slot

            variable self.cached_text

            variable self.cached_provider

            variable self.labels

            variable self.label_batch

            variable self.bg_rectangle

        function renderFor(self, itemstack: ItemStack, position)
            
            Will render the ItemBoxProvider for a given slot
            :param itemstack: the slot to render over
            :param position: the position to render at, or None if calculated from slot


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

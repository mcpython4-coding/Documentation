***HoveringItemBox.py - documentation - last updated on 9.7.2020 by uuk***
___

    class IHoveringItemBoxDefinitionPlugin
        
        Abstract class for manipulating an existing HoveringDefinition text.
        Use addPlugin(<instance>) on the final class to register your plugin.
        Saver than replacing the entry for the item.
        Multiple plugins can co-exists. They are applied in order of registration.
        Please make sure that you look for changes before applying your changes (as you might interfere with stuff from another plugin)


        function manipulateShownText(self, slot: mcpython.gui.ItemStack.ItemStack, text: list)

    class IHoveringItemBoxDefinition
        
        Base class for an ToolTip text provider. Should generate out of an ItemStack an html-string-list


        static
        function setup(cls)
            
            Call this method on every child to set up


        function getHoveringText(self, itemstack: mcpython.gui.ItemStack.ItemStack) -> list

        static
        function addPlugin(cls, plugin: IHoveringItemBoxDefinitionPlugin)

    class DefaultHoveringItemBoxDefinition extends IHoveringItemBoxDefinition
        
        Class representing an normal translate-able-configure-able tooltip with an given default style and layout
        Uses the default Item-class-methods to render certain stuff


        function __init__(self, default_style="<font color='{color}'>{text}</font>", localize_builder="item.{}.{}")

            variable self.localize_builder

            variable self.default_style

        function getHoveringText(self, itemstack: mcpython.gui.ItemStack.ItemStack) -> list

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

        function renderFor(self, itemstack: mcpython.gui.ItemStack.ItemStack, position)
            
            will render the ItemBoxProvider for an given slot
            :param itemstack: the slot to render over
            :param position: the position to render at, or None if calculated from slot


        function eraseCache(self)
            
            Can be used to re-calculate the text of the tool tip

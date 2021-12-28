***InventoryCreativeTab.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class ICreativeView extends mcpython.client.gui.ContainerRenderer.ContainerRenderer,  ABC
        
        Base class for a creative tab
        Comes with some helper code


        function __init__(self)

            variable self.tab_icon

            variable self.tab_icon_selected

            variable self.is_selected

            variable self.tab_slot

            variable self.icon_position

        function update_rendering(self)

        function get_icon_stack(self) -> ItemStack

        function get_view_size(self) -> typing.Tuple[int, int]

        function draw_at(self, position: typing.Tuple[int, int], hovering_slot=None)

        function draw(self, hovering_slot=None)

                    variable self.custom_name_label.text

                variable self.custom_name_label.x

                variable self.custom_name_label.y

            variable shared.state_handler.active_state.parts[0].activate_mouse

    class CreativeItemTab extends ICreativeView

        variable bg_texture: pyglet.image.AbstractImage

            variable cls.bg_texture

        function __init__(
                self, name: str, icon: ItemStack, group: ItemGroup = None, linked_tag=None
                ):

            variable self.icon

            variable self.group

            variable self.scroll_offset

            variable self.old_scroll_offset

            variable self.linked_tag

            variable self.custom_name

            variable self.scroll_bar

        function set_scrolling(self, progress: int)

        function load_from_tag(self)
            
            Helper method for reloading the content from the underlying tag
            Use only when self.linked_tag is set, otherwise, this will crash


            variable tag

        function update_rendering(self, force=False)
            
            Updates the slot content of the rendering system
            :param force: force update, also when nothing changed


            variable self.old_scroll_offset

            variable entries - todo: cache value!

            variable entries

                    variable entry
            
            Creates the slots


            function work(i)

            variable slots

        function add_item(self, item: typing.Union[ItemStack, LazyClassLoadItemstack, str])
            
            Adds an item to the underlying item group
            :param item: the item stack or the item name


                variable item

        function get_icon_stack(self) -> ItemStack

        function get_view_size(self) -> typing.Tuple[int, int]

        function draw_at(self, position: typing.Tuple[int, int], hovering_slot=None)

        function clear(self)

        function on_mouse_button_press(
                self,
                relative_x: int,
                relative_y: int,
                button: int,
                modifiers: int,
                item_stack,
                slot,
                ) -> bool:

        function __repr__(self)

        function update_shift_container(self)

    class CreativeTabSearchBar extends CreativeItemTab

            variable cls.bg_texture

        function __init__(
                self, name: str, icon: ItemStack, group: ItemGroup = None, linked_tag=None
                ):

            variable self.group: FilteredItemGroup

            variable self.search_bar

            variable self.tab_icon

            variable self.tab_icon_selected

            variable self.need_reload

            function setNeedReload()

                variable self.need_reload

    class CreativePlayerInventory extends ICreativeView

        variable TEXTURE_SIZE

        variable TEXTURE

            variable cls.TEXTURE

        function __init__(self)

            variable self.stack

            variable self.tab_icon

            variable self.tab_icon_selected

        function get_icon_stack(self) -> ItemStack

        function get_view_size(self) -> typing.Tuple[int, int]

        function draw_at(self, position: typing.Tuple[int, int], hovering_slot=None)
            
            Creates the slots


            function work(i)

        static
        function get_config_file() -> str or None

    class CreativeTabManager

        variable TAB_SIZE

        variable UPPER_TAB
            todo: make this reload-able!

        variable UPPER_TAB_SELECTED

        variable LOWER_TAB

        variable LOWER_TAB_SELECTED

            variable cls.UPPER_TAB

            variable cls.UPPER_TAB_SELECTED

            variable cls.LOWER_TAB

            variable cls.LOWER_TAB_SELECTED

        function __init__(self)

            variable self.pages: typing.List[typing.List[ICreativeView]]

            variable self.inventory_instance

            variable self.search_instance

            variable self.saved_hotbars

            variable self.current_page

            variable self.underlying_event_bus: mcpython.engine.event.EventBus.EventBus

            variable self.hovering_tab

            variable self.page_left

            variable self.page_right

            variable self.page_label

            variable self.lower_left_position

            variable self.container_size

            variable self.current_tab: typing.Optional[ICreativeView]

        function is_multi_page(self)

                variable self.current_page

                variable self.current_page

        function on_mouse_move(self, x, y, dx, dy, *_)

        function init_tabs_if_needed(self)

                variable self.search_instance

            variable tab

        function get_tab_at(self, mx, my) -> typing.Optional[ICreativeView]

            variable tabs

            variable x

        function add_tab(self, tab: ICreativeView)

        function draw_tab(self, tab: ICreativeView, x: int, y: int)

        function draw_tabs(
                self,
                lower_left_position: typing.Tuple[int, int],
                container_size: typing.Tuple[int, int],
                ):

            variable self.lower_left_position

            variable self.container_size

            variable tabs

            variable x

                variable self.page_left.active

                variable self.page_left.position

                variable self.page_right.active

                variable self.page_right.position

                variable self.page_label.text

                variable self.page_label.position

        function increase_page(self, count: int)

                variable self.current_tab.is_selected

            variable self.current_tab

            variable tab.is_selected

        function print_missing(self)

                        variable entries

    variable CT_MANAGER

    variable BuildingBlocks

    variable Decoration

    variable Redstone

    variable Transportation

    variable Miscellaneous

    variable Food

    variable Tools

    variable Weapons

    variable Brewing

    variable Test

        variable BuildingBlocks

        variable Decoration

        variable Redstone

        variable Transportation

        variable Miscellaneous

        variable Food

        variable Tools

        variable Weapons

        variable Brewing
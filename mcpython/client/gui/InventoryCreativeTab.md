***InventoryCreativeTab.py - documentation - last updated on 1.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable TAB_TEXTURE

    class CreativeTabScrollbar
        
        Creative tab scrollbar
        Feel free to re-use for other stuff
        todo: use batches


        variable SCROLLBAR_SIZE

        variable NON_SELECTED_SCROLLBAR

        variable SELECTED_SCROLLBAR

        static
        function reload(cls)

        function __init__(self, callback: typing.Callable[[int], None], scroll_until: int = 1)

            variable self.callback

            variable self.scroll_until

            variable self.currently_scrolling

            variable self.underlying_event_bus: mcpython.engine.event.EventBus.EventBus

            variable self.position

            variable self.height

            variable self.is_hovered

        function on_mouse_drag(self, x, y, dx, dy, buttons, modifiers)

        function on_mouse_move(self, x, y, dx, dy)

        function on_mouse_scroll(self, x, y, sx, sy)

        function on_key_press(self, symbol, modifiers)

        function get_scrollbar_position(self)

        function draw_at(self, lower_left: typing.Tuple[int, int], height: int)

        function activate(self)

        function deactivate(self)

        function set_max_value(self, value: int)

            variable self.scroll_until

            variable self.currently_scrolling

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

        function on_activate(self)

        function on_deactivate(self)

    class CreativeItemTab extends ICreativeView

        variable bg_texture: pyglet.image.AbstractImage

        static
        function reload(cls)

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

        function create_slot_renderers(self)
            
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

        function draw(self, hovering_slot=None)

        function clear(self)

        function on_deactivate(self)

        function on_activate(self)

        function on_mouse_button_press(
                self,
                relative_x: int,
                relative_y: int,
                button: int,
                modifiers: int,
                item_stack,
                slot,
                ) -> bool:

    class CreativeTabSearchBar extends CreativeItemTab

        static
        function reload(cls)

        function __init__(
                self, name: str, icon: ItemStack, group: ItemGroup = None, linked_tag=None
                ):

            variable self.group: FilteredItemGroup

            variable self.search_bar

            variable self.tab_icon

            variable self.tab_icon_selected

        function on_deactivate(self)

        function on_activate(self)

    class CreativePlayerInventory extends ICreativeView

        variable TEXTURE_SIZE

        variable TEXTURE

        static
        function reload(cls)

        function __init__(self)

            variable self.stack

            variable self.tab_icon

            variable self.tab_icon_selected

        function get_icon_stack(self) -> ItemStack

        function get_view_size(self) -> typing.Tuple[int, int]

        function draw_at(self, position: typing.Tuple[int, int], hovering_slot=None)

        function create_slot_renderers(self)
            
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

        static
        function reload(cls)

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

        function on_key_press(self, button, mod)

                variable self.current_page

                variable self.current_page

        function on_mouse_move(self, x, y, dx, dy, *_)

        function init_tabs_if_needed(self)

                variable self.search_instance

        function activate(self)

        function deactivate(self)

        function on_mouse_press(self, mx, my, button, modifiers)

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

        function open(self)

        function increase_page(self, count: int)

        function switch_to_tab(self, tab: ICreativeView)

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

    @shared.mod_loader("minecraft", "stage:item_groups:load")
    function init()
        
        for item in shared.registry.get_by_name("minecraft:item").entries_iterator():
            AllTestTab.add_item(ItemStack(item))

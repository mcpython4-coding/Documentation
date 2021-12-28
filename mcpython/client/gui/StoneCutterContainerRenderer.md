***StoneCutterContainerRenderer.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class StoneCutterContainerRenderer extends  mcpython.client.gui.ContainerRenderer.ContainerRenderer 
        
        Inventory class for the stone cutter
        May be shared across multiple stonecutters at client side


        variable TEXTURE

        variable TEXTURE_SIZE

        variable SCROLLBAR_TEXTURE

            variable texture

            variable size

            variable texture_main

            variable size_main

            variable texture_main

            variable cls.TEXTURE

            variable cls.TEXTURE_SIZE

            variable texture_scrollbar

            variable size_scrollbar

            variable texture_scrollbar

            variable cls.SCROLLBAR_TEXTURE

        function __init__(self)

                variable self.custom_name

            variable self.currently_selected

            variable self.previous_item

            variable self.possible_outputs

            variable self.scrollbar

        static
        function get_config_file() -> str or None

        function handle_slot_click(self, slot, button, modifiers)

                variable self.currently_selected

        function draw(self, hovering_slot=None)

        function get_interaction_slots(self)

        function update_shift_container(self)

        function update_selection_view(self, player=None)

            variable self.previous_item

                variable self.scrollbar.steps

                variable self.scrollbar.current_step

                variable self.currently_selected

            variable self.possible_outputs

            variable self.scrollbar.steps

            variable self.scrollbar.current_step

        function update_selection_slots(self)

            variable offset

                    variable i

                    variable slot

        function update_output_slot(self, player=None)
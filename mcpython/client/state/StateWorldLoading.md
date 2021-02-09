***StateWorldLoading.py - documentation - last updated on 9.2.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateWorldLoading extends State.State

        variable NAME

        function __init__(self)

            variable self.status_table

            variable self.world_size

            variable self.finished_chunks

        function load_or_generate(self, name: str)

        function load_world_from(self, name: str)

        function get_parts(self) -> list

        function on_update(self, dt)

        function activate(self)

        function deactivate(self)

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        function calculate_percentage_of_progress(self)

        function on_draw_2d_post(self)

                variable status

                    variable factor

                    variable color

                    variable color

                    variable color

    variable world_loading

    @onlyInClient()
    function create()
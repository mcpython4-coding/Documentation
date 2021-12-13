***WorldLoadingProgressState.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class WorldLoadingProgress extends AbstractState.AbstractState

        variable NAME

        function __init__(self)

            variable self.status_table

            variable self.world_size

            variable self.finished_chunks

            variable save_file

        function create_state_parts(self) -> list

                    variable c

                    variable self.status_table[chunk]

                variable shared.world.world_loaded

            variable self.parts[1].text

            variable shared.world_generation_handler.enable_generation

            variable shared.world_generation_handler.enable_generation
                todo: fix bug: something is wrong here...
                shared.world.savefile.read("minecraft:chunk", dimension=shared.world.get_active_player().dimension.id, chunk=(cx, cz),
                immediate=False)

                variable player

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

        variable world_loading
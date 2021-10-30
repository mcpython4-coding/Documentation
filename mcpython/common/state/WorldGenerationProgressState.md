***WorldGenerationProgressState.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class WorldGenerationProgress extends AbstractState.AbstractState

        variable NAME

        function __init__(self)

            variable self.status_table

            variable self.profiler

            variable self.world_gen_config

        function generate_world(self, config=None)

        function generate_from_user_input(self, state=None)

        function create_state_parts(self) -> list

        function on_update(self, dt)

            variable overworld

                variable c

                    variable self.status_table[chunk]

                    variable count

                    variable self.status_table[chunk]

        function activate(self)

            variable mcpython.server.worldgen.noise.NoiseManager.manager.default_implementation

            variable shared.world_generation_handler.enable_generation

            variable fx

            variable fy

            variable ffx

            variable ffy

            variable seed

            variable shared.world.config["seed"]

        function finish(self)

            variable overworld

                variable chunk

                variable chunk.is_ready

                variable chunk.visible

            variable player_name

                variable player_name

            variable shared.world.local_player
                todo: this is also only client code

            variable shared.world.config["enable_auto_gen"]

            variable shared.world.config["enable_world_barrier"]

                variable chunk

                variable height

                variable block_chest

                variable block_chest.loot_table_link

            variable player
                set player position

            variable shared.world.world_loaded

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        function calculate_percentage_of_progress(self)

        function create_state_renderer(self) -> typing.Any

    variable world_generation

    function create()
***StateWorldGeneration.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateWorldGeneration extends State.State

        variable NAME

        function __init__(self)

            variable self.status_table

            variable self.profiler

            variable self.world_gen_config

        function generate_world(self, config=None)

        function generate_from_user_input(self, state=None)

        function get_parts(self) -> list

        function on_update(self, dt)

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

                variable chunk

                variable chunk.is_ready

                variable chunk.visible

            variable player_name

                variable player_name

            variable shared.world.active_player
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

        function on_draw_2d_post(self)

                variable status

                    variable factor

                    variable color

                    variable color

                    variable color

    variable world_generation

    @onlyInClient()
    function create()
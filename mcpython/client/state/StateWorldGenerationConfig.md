***StateWorldGenerationConfig.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateWorldGenerationConfig extends State.State

        variable NAME

        function __init__(self)

        function get_parts(self) -> list

        function is_auto_gen_enabled(self) -> bool

        function is_world_gen_barrier_enabled(self) -> bool

        function get_world_config_name(self) -> str

        function get_seed(self) -> int

        function get_player_name(self) -> str

        function get_world_size(self)

        function get_seed_source(self)

        function on_back_press(self, x, y)

        function on_generate_press(self, x, y)

        function generate(self)

        function bind_to_eventbus(self)

        function on_key_press(self, symbol, modifiers)

        static
        function on_draw_2d_pre()

        function activate(self)

                variable part.index

            variable self.parts[4].text_pages

    variable world_generation_config

    @onlyInClient()
    function create()
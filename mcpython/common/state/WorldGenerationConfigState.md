***WorldGenerationConfigState.py - documentation - last updated on 13.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class WorldGenerationConfig extends AbstractState.AbstractState

        variable NAME

        function __init__(self)

        function create_state_parts(self) -> list

        function is_auto_gen_enabled(self) -> bool

        function is_world_gen_barrier_enabled(self) -> bool

        function get_world_config_name(self) -> str

        function get_seed(self) -> int

        function get_player_name(self) -> str

        function get_world_size(self)

        function get_seed_source(self)

            variable filename

                variable filename

        function bind_to_eventbus(self)

                variable part.index

                variable part.text

                variable part.index

            variable self.parts[4].text_pages

    variable world_generation_config

        variable world_generation_config
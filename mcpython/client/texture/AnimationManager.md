***AnimationManager.py - documentation - last updated on 18.11.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AnimationController

        function __init__(self, frames: int, timing: int)

            variable self.frames

            variable self.timing

            variable self.group

            variable self.ticks_since_change

            variable self.atlas_index

            variable self.textures

            variable self.atlases

            variable self.remaining_ticks

        function add_texture(self, image: PIL.Image, lookup: typing.List[int])

            variable atlas

            variable width

            variable pos

        function bake(self)

        function tick(self, ticks: float)

            variable self.atlas_index

            variable self.group.texture

    class AnimationManager

        function __init__(self)

            variable self.texture2controller: typing.List[AnimationController]

        function prepare_animated_texture(self, location: str) -> int

            variable texture

                variable t_location

                variable t_location

                variable t_location

            variable meta: dict

                variable meta["frames"]

            variable atlas

            variable self.texture_lookup[location]

        function get_atlas_for_spec(self, frames: int, timing: int) -> AnimationController

            variable controller

        function get_group_for_texture(self, texture: int)

        function get_position_for_texture(self, texture: int)

        function get_atlas_size_for_texture(self, texture: int)

        function tick(self, ticks: float)

        function bake(self)

    variable animation_manager
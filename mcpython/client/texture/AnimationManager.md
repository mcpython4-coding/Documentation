***AnimationManager.py - documentation - last updated on 28.12.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class AnimatedTexture extends TextureGroup

        function __init__(self, hash_texture, texture, parent=None)

            variable self.hash_texture

        function __hash__(self)

        function __eq__(self, other)

    @onlyInClient() class AnimationController
        
        Manager class for the animation group, identified by frame count and ticks needed for one frame.
        Animation controllers are shared by AnimationManager when possible.
        WARNING: This system is highly unstable currently, and may never be fully stable


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

        function add_textures(self, textures: typing.List[PIL.Image.Image])

            variable atlas

            variable pos

                variable self.textures[i]

            variable self.group

        function tick(self, ticks: float)

            variable self.atlas_index

            variable self.group.texture

    @onlyInClient() class AnimationManager
        
        Manager for any block animations
        Handles all AnimationController's, use get_atlas_for_spec() when needing your own one.
        Use prepare_animated_texture() when wanting stuff from a texture on resources.
        Use the get_...() methods to get the needed data for animations


        function __init__(self)

            variable self.texture2controller: typing.List[AnimationController]
            
            Prepares a texture for later animation; Internally loads the .mcmeta file for the image,
            and does some parsing for knowing how the animation should play
            :param location: a location to look at
            :return: the texture id, for later lookup operations


            variable texture

                variable t_location

                variable t_location

                variable t_location

            variable meta: dict

                variable meta["frames"]

            variable atlas

            variable self.texture_lookup[location]

        function prepare_texture_series_as_animation(
                self, textures: typing.List[PIL.Image.Image], timing_per_frame: int = 1
                ) -> int:
            
            Prepares a set of textures with some ticks in between for rendering as an animation
            :param textures: the textures to use
            :param timing_per_frame: how many ticks per frame to use
            :return: the animation id


            variable controller

        function get_atlas_for_spec(self, frames: int, timing: int) -> AnimationController
            
            Returns or creates the AnimationController for the given configuration
            Use prepare_texture_series_as_animation for fully registering it into the system


            variable controller

        function get_group_for_texture(self, texture: int)

        function get_position_for_texture(self, texture: int)

        function get_atlas_size_for_texture(self, texture: int)

        function tick(self, ticks: float)

        variable animation_manager
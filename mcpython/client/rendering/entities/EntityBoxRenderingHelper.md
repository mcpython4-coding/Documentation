***EntityBoxRenderingHelper.py - documentation - last updated on 19.5.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class EntityBoxInstance
        
        The box rendered for entities [in the future]


        class MutableEntityBox
            
            Mutator for the underlying VertexList
            Handles the vertex calculation


            function __init__(
                    self,
                    source: "EntityBoxInstance",
                    buffer: pyglet.graphics.vertexdomain.VertexList,
                    position,
                    rotation,
                    ):

                variable self.source

                variable self.buffer

                variable self.position

                variable self.rotation

            function update(self)

            function get_underlying(self) -> pyglet.graphics.vertexdomain.VertexList

            function delete(self)

        function __init__(
                self,
                texture_path: str,
                sheet_size: typing.Tuple[int, int],
                texture_size: typing.Tuple[int, int, int],
                box_size: typing.Tuple[float, float, float],
                ):

            variable self.texture_path

            variable self.sheet_size

            variable self.texture_size

            variable self.box_size

            variable self.texture_group: pyglet.graphics.TextureGroup

            variable self.tex_coords_cache: typing.Optional[typing.List[float]]

            variable self.rotation2vertices

        function draw(
                self,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                ):

        function add_to_batch_static(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                ) -> pyglet.graphics.vertexdomain.VertexList:

        function add_to_batch_mutable(
                self,
                batch: pyglet.graphics.Batch,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                ) -> MutableEntityBox:

            variable buffer

        function get_draw_info(
                self,
                position: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                ) -> typing.Tuple[typing.List[float], typing.List[float]]:

        function invalidate(self)
            
            Forces a recalculation of the whole cache based on initial parameters


        function calculate_texture_coords(self) -> typing.List[float]

        function calculate_default_vertices(self) -> typing.List[float]

        function get_rotated_vertices_variant(
                self, rotation: typing.Tuple[float, float, float]
                ) -> typing.List[float]:

        function calculate_vertices_variant(
                self,
                offset: typing.Tuple[float, float, float],
                rotation: typing.Tuple[float, float, float],
                ) -> typing.List[float]:
***BoundingBox.py - documentation - last updated on 25.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class AbstractBoundingBox extends ABC
        
        Abstract base class for bounding-box like classes


        function test_point_hit(
                self,
                point: typing.Tuple[float, float, float],
                boxposition: typing.Tuple[float, float, float],
                ):
            
            Tests for a collision with a single point
            :param point: the point
            :param boxposition: the offset of the box


        function draw_outline(self, position: typing.Tuple[float, float, float])
            
            Draws an outline of the box
            :param position: the offset of the box


    class BoundingBox extends AbstractBoundingBox
        
        The basic bounding box - a cube


        function __init__(
                self,
                size: typing.Tuple[float, float, float],
                relative_position: typing.Tuple[float, float, float] = (0, 0, 0),
                rotation: typing.Tuple[float, float, float] = (0, 0, 0),
                ):

            variable self.size

            variable self.relative_position

            variable self.rotation

        function test_point_hit(
                self,
                point: typing.Tuple[float, float, float],
                boxposition: typing.Tuple[float, float, float],
                ):

            variable point

        function draw_outline(self, position: typing.Tuple[float, float, float])

    class BoundingArea extends AbstractBoundingBox
        
        More options for hit-test by using an list of BoundBoxes. Has the same methods for interaction


        function __init__(self)

            variable self.bounding_boxes

        function add_box(
                self,
                size: typing.Tuple[float, float, float],
                relative_position=(0, 0, 0),
                rotation=(0, 0, 0),
                ):

        function test_point_hit(
                self,
                point: typing.Tuple[float, float, float],
                boxposition: typing.Tuple[float, float, float],
                ):

        function draw_outline(self, position: typing.Tuple[float, float, float])

    variable FULL_BLOCK_BOUNDING_BOX

    variable EMPTY_BOUNDING_BOX
***BoundingBox.py - documentation - last updated on 14.5.2020 by uuk***
___

    class BoundingBox

        function __init__(self, size, relposition=(0, 0, 0), rotation=(0, 0, 0))

            variable self.size

            variable self.relposition

            variable self.rotation

        function test_point_hit(self, point, boxposition)

        function draw_outline(self, position)

    class BoundingArea
        
        more options for hit-test by using an list of BoundBoxes. Has the same methods for interaction


        function __init__(self)

            variable self.bboxes

        function add_box(self, size, relposition=(0, 0, 0), rotation=(0, 0, 0))

        function test_point_hit(self, point, boxposition)

        function draw_outline(self, position)

    variable FULL_BLOCK_BOUNDING_BOX
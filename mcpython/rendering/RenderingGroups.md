***RenderingGroups.py - documentation - last updated on 18.6.2020 by uuk***
___

    class CollectionGroup extends pyglet.graphics.Group
        
        Group of groups


        function __init__(self, *sub_groups)

            variable self.sub_groups

        function set_state(self)

        function unset_state(self)

    class MatrixStackGroup extends pyglet.graphics.Group
        
        Group for holding an custom MatrixStack-instance


        function __init__(self, stack: mcpython.rendering.MatrixStack.MatrixStack)

            variable self.stack

        function set_state(self)

        function unset_state(self)
***ICustomBlockRenderer.py - documentation - last updated on 29.7.2020 by uuk***
___

    class ICustomBatchBlockRenderer

        function add(self, position, block, face)

        function remove(self, position, block, data, face)

    class ICustomDrawMethodRenderer

        function draw(self, position, block)

    class ICustomBlockVertexManager

        function handle(self, block, vertices, face, blockstate)
***ItemModel.py - documentation - last updated on 21.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    This project is not official by mojang and does not relate to it.


    class IItemModelLoader

        static
        function validate(cls, data: dict) -> bool

        static
        function decode(cls, data: dict, model: "ItemModel")

    class DefaultLoader extends IItemModelLoader

        static
        function validate(cls, data: dict) -> bool

        static
        function decode(cls, data: dict, model: "ItemModel")

    variable LOADERS

    class ItemModel

        static
        function from_file(cls, file: str, item: str)

        static
        function from_data(cls, data, item)

        function __init__(self, item: str)

            variable self.item

            variable self.parents

            variable self.lighting

            variable self.displays

            variable self.layers

            variable self.overrides

        function __repr__(self)

        function addParent(self, parent: str)

        function addDisplayTransform(
                self, name: str, rotation=(0, 0, 0), translation=(0, 0, 0), scale=(1, 1, 1)
                ):

            variable self.displays[name]

        function addTextureLayer(self, number: int, file: str)

        function addOverride(self, predicate, replacement: str)

        function bake(self, helper: "ItemModelHandler")

        function add_to_batch(
                self, position: tuple, batch, context: str, state: dict
                ) -> mcpython.client.rendering.BatchHelper.BatchReference:

        function draw(self, position: tuple, context: str, state: dict)
            
                ((0, 0, 0), (0, 0, 0), (1, 1, 1))
                if context not in self.displays
                else self.displays[context]


    class ItemModelHandler

        function __init__(self)

            variable self.models

            variable self.atlas

        @shared.mod_loader("minecraft", "stage:model:item:search")
        static
        function load()

        function from_data(self, data: dict, name: str)

        function from_folder(self, folder: str, modname: str)

        function bake(self)

        function add_to_batch(
                self, item_name, *args, **kwargs
                ) -> mcpython.client.rendering.BatchHelper.BatchReference:

        function draw(self, item_name, *args, **kwargs)

    variable handler
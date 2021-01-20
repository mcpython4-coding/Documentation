***IRecipe.py - documentation - last updated on 20.1.2021 by uuk***
___

    class AwaitingDependencyException extends Exception

    class IRecipe extends mcpython.common.event.Registry.IRegistryContent,  ABC
        
        Base class for recipes
        Data is matched by TYPE, than decoded by from_data() ['file' is for error messages]
        Later run the loading pipe, bake() is called which can raise AwaitingDependencyException
        when a dependency for this recipe is not ready [only waiting for bake() to be called].
        After all that, prepare() is called. This should create the needed lookups for the crafting systems
        [e.g. maps from input -> output, ...]


        variable TYPE

        variable RECIPE_TYPE_NAMES

        variable RECIPE_VIEW

        static
        function from_data(cls, data: dict, file: str)

        function __init__(self)

            variable self.name

        function get_inputs(self) -> typing.Iterable[ItemStack]

        function get_outputs(self) -> typing.Iterable[ItemStack]

        function bake(self)

        function prepare(self)
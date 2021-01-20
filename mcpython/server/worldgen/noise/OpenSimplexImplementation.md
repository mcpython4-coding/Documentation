***OpenSimplexImplementation.py - documentation - last updated on 20.1.2021 by uuk***
___

    class OpenSimplexImplementation extends INoiseImplementation
        
        Default noise implementation.


        variable NAME

        function __init__(self, *args, **kwargs)

            variable self.noises: typing.List[typing.Optional[opensimplex.OpenSimplex]]

        function set_seed(self, seed: int)

        function calculate_position(self, position) -> float
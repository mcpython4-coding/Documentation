***PackageNoiseImplementation.py - documentation - last updated on 20.1.2021 by uuk***
___

    class NoiseImplementation extends INoiseImplementation
        
        Default noise implementation.


        variable NAME

        function __init__(self, *args, **kwargs)

            variable self.noises: typing.List[typing.Optional[int]]

        function set_seed(self, seed: int)

        function calculate_position(self, position) -> float
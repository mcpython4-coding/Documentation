***KeyBinding.py - documentation - last updated on 24.6.2020 by uuk***
___

    class KeyMouseBinding
        
        class holding an key or mouse binding


        function __init__(self, name: str, group_name: str, default: typing.Union[int, typing.Iterable[int]],
                default_mod: typing.Union[int, typing.Iterable[int]] = 0):

        function applies(self, key_or_button, mod) -> bool
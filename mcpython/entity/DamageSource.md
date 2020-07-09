***DamageSource.py - documentation - last updated on 18.6.2020 by uuk***
___

    class DamageSource
        
        class direct representing an mc DamageSource


        function __init__(self, name: str = None)

            variable self.attributes

            variable self.__attributes

            variable self.type

            variable self.bypasses_armor

            variable self.bypasses_invulnerability

            variable self.bypasses_magic

            variable self.target_entity

            variable self.source_entity

            variable self.is_explosion

            variable self.is_fire

            variable self.is_magic

            variable self.is_projectile

            variable self.is_lighting

        function setAttribute(self, key, value)

        function getAttribute(self, key)

        function __eq__(self, other)
***IDataFixer.py - documentation - last updated on 11.6.2020 by uuk***
___

    @deprecation.deprecated("dev3-1", "a1.3.0") class DataFixerException extends Exception

    @deprecation.deprecated("dev3-1", "a1.3.0") class IDataFixer extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        variable TRANSFORMS

        variable PART

        variable DEPENDS

        @deprecation.deprecated("dev3-1", "a1.3.0")
        static
        function fix(cls, savefile)

    @deprecation.deprecated("dev3-1", "a1.3.0") class IGeneralDataFixer extends mcpython.event.Registry.IRegistryContent

        variable TYPE

        variable LOAD_FIXES

        variable UPGRADES_TO

    variable datafixerregistry - mcpython.event.Registry.Registry("datafixers", ["minecraft:datafixer"])

    variable generaldatafixerregistry - mcpython.event.Registry.Registry("generaldatafixers", ["minecraft:general_datafixer"])

    @deprecation.deprecated("dev3-1", "a1.3.0")
    function load_general_fixer()

    @deprecation.deprecated("dev3-1", "a1.3.0")
    function load_fixer()
***IDataFixer.py - documentation - last updated on 16.5.2020 by uuk***
___

    class DataFixerException extends Exception

    class IDataFixer extends event.Registry.IRegistryContent

        variable TYPE

        variable TRANSFORMS - from, to

        variable PART - which part it fixes, only one per part is executed

        variable DEPENDS - an list of fixer parts which should be executed first

        static function fix(cls, savefile)

    class IGeneralDataFixer extends event.Registry.IRegistryContent
        
        Every version supported by datafixer need this.
        It provides information what to fix on load and what can wait


        variable TYPE

        variable LOAD_FIXES - an list of parts to fix an or (partname, kwargs)

        variable UPGRADES_TO - which version this datafixer upgrades to

    variable datafixerregistry

    variable generaldatafixerregistry

    function load_general_fixer()

    function load_fixer()
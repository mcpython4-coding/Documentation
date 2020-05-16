***DataFixer4to5.py - documentation - last updated on 16.5.2020 by uuk***
___

    @G.registry class GeneralFix extends storage.datafixer.IDataFixer.IGeneralDataFixer

        variable NAME

        variable LOAD_FIXES

        variable UPGRADES_TO

    @G.registry class ChunkFixer extends storage.datafixer.IDataFixer.IDataFixer

        variable NAME
            NAME should be: "<version from>-<version to>:<part>"

        variable TRANSFORMS - from, to

        variable PART - which part it fixes, only one per part is executed

        static function fix(cls, savefile, dimension, region)

    @G.registry class InventoryFixer extends storage.datafixer.IDataFixer.IDataFixer

        variable NAME

        variable TRANSFORMS - from, to

        variable PART - which part it fixes, only one per part is executed

        static function fix(cls, savefile, path, file=None)
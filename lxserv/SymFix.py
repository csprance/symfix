#!/usr/bin/env python
################################################################################
#
# SymFixCmd.py
# Description: The command class used to call the symfix python module
# Usage:
# csp.symfix
# Author: Chris Sprance Entrada Interactive
#
################################################################################

import lx
import lxifc
import lxu.command
import symfix

class SymFixCmd(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)

    def cmd_Flags(self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        return True

    def cmd_Interact(self):
        pass

    def basic_Execute(self, msg, flags):
        reload(symfix)
        symfix.main()

    def cmd_Query(self, index, vaQuery):
        lx.notimpl()


lx.bless(SymFixCmd, "csp.symfix")

#!/usr/bin/env python
################################################################################
#
# SymFix.py
# Description: The class used for fixing instance mirror bug in modo
# Usage:
# csp.symfix
# Author: Chris Sprance Entrada Interactive
#
################################################################################

import lx
import lxifc
import lxu.command
import modo


class SymFix(lxu.command.BasicCommand):
    def __init__(self):
        lxu.command.BasicCommand.__init__(self)
        self.selection = list()
        self.scene = modo.Scene()
        self.user_selection = list()

    def cmd_Flags(self):
        return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        return True

    def cmd_Interact(self):
        pass

    def store_selection(self):
        '''
        Takes the user selection and stores all the selected
        meshes into a list for later use in self.selection
        '''
        self.user_selection = self.scene.selected
        self.selection = self.scene.selectedByType('mesh')

    def basic_Execute(self, msg, flags):
        # store our selection filtering out only the mesh items
        self.store_selection()
        # loop through all the selected meshes
        for mesh in self.selection:
            # set current mesh in the loop
            self.mesh = mesh
            lx.out(self.mesh)
            
    def cmd_Query(self, index, vaQuery):
        lx.notimpl()


lx.bless(SymFix, "csp.symfix")

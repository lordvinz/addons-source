#------------------------------------------------------------------------
#
# Register the Gramplet
#
#------------------------------------------------------------------------

register(GRAMPLET, 
         id="Import Gramplet", 
         name=_("Import Gramplet"), 
         description = _("Gramplet for importing text"),
         status = STABLE,
         version = '1.0.24',
         gramps_target_version = "5.0",
         height=200,
         gramplet = "ImportGramplet",
         fname="ImportGramplet.py",
         gramplet_title=_("Import"),
         help_url = "ImportGramplet",
         )
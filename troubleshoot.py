from gettext import gettext as _
import vars
import gui
import urllib.request

def apply_blacklist():
    gui.message(_("Applying safety blacklist..."))
    try:
        urllib.request.urlretrieve("https://tf2classic.org/serverlist/blacklist.php", vars.INSTALL_PATH + "/tf2classic/cfg/server_blacklist.txt")
    except:
        gui.message(_("WARNING: could not apply safety blacklist."))

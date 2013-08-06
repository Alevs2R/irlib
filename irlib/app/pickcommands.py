
import matplotlib.pyplot
import commands
import command_parser as cp
from .components import Radargram, PickWindow

class PickCommand(commands.Command):

    _type = "Pick"
    cmd = "pick"
    helpstr = """Manage event picking

    pick <cmd>

    Commands related to radar event picking are accessed by first typing "pick",
    and then the specific command. Type 'help' for a list of possibilities.
    """
    def apply(self, app, args):
        if len(args) == 0:
            print "Type 'help' or 'help pick' for instructions."
        try:
            cp.apply_command(app.command_registry, args, app)
        except KeyError:
            print "No picking command '{0}' exists".format(args[0])
        return

class PickOn(PickCommand):

    cmd = "on"
    helpstr = "\tOpen a PickWindow.\n"

    def apply(self, app, args):
        w = PickWindow(app.line)
        w.connect_radargram(app.get_appwindows(Radargram)[0])
        app.appwindows.append(w)
        return

class PickOff(PickCommand):

    cmd = "off"
    helpstr = "\tClose PickWindow and stope picking.\n"

    def apply(self, app, args):
        for w in app.get_appwindows(PickWindow):
            matplotlib.pyplot.close(w.fig)
            app.remove_appwindow(w)
            del w

class PickSave(PickCommand):

    cmd = "save"
    helpstr = "\tSave picks to 'picking/'"

    def apply(self, app, args):
        for w in app.get_appwindows(PickWindow):
            w.save_picks()

class PickSave(PickCommand):

    cmd = "load"
    helpstr = "\tLoad picks from 'picking/'"

    def apply(self, app, args):
        for w in app.get_appwindows(PickWindow):
            w.load_picks()

class PickBedAuto(PickCommand):

    cmd = "bed"
    helpstr = """"Attempt to automatically pick the bed reflection

    pick bed [<s0> <s1>]

    Optionally, constrain pick to between *s0* and *s1* samples from the "top"
    of the traces.
    """

    def apply(self, app, args):
        for w in app.get_appwindows(PickWindow):
            if len(args) > 2:
                try:
                    pickargs = [int(a) for a in args[2:]]
                except ValueError:
                    print "arguments must be integer"
                    return
            else:
                pickargs = []
            w.autopick_bed(*pickargs)

class PickDCAuto(PickCommand):

    cmd = "dc"
    helpstr = """"Attempt to automatically pick the direct wave

    pick dc [<s0> <s1>]

    Optionally, constrain pick to between *s0* and *s1* samples from the "top"
    of the traces.
    """

    def apply(self, app, args):
        for w in app.get_appwindows(PickWindow):
            if len(args) > 2:
                try:
                    pickargs = [int(a) for a in args[2:]]
                except ValueError:
                    print "arguments must be integer"
                    return
            else:
                pickargs = []
            w.autopick_dc(*pickargs)








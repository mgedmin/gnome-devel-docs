from gi.repository import Gtk
import sys

actions = [["Select", None],
           ["New", Gtk.STOCK_NEW],
           ["Open", Gtk.STOCK_OPEN],
           ["Save", Gtk.STOCK_SAVE]]

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        self.set_default_size(200, -1)
        self.set_border_width(10)

        # the data in the model, of type string
        listmodel = Gtk.ListStore(str, str)
        # there is no insert_with_values in Python, we use append
        for i in range(len(actions)):
            listmodel.append(actions[i])

        # a combobox to see the data stored in the model
        combobox = Gtk.ComboBox(model=listmodel)

        # cellrenderers
        renderer_pixbuf = Gtk.CellRendererPixbuf()
        renderer_text = Gtk.CellRendererText()
        # we pack the cell into the beginning of the combobox, allocating
        # (False) no more space than needed

        # first the image, then the text
        # it does not matter in which order they are in the model,
        # the visualization is decided by the order of the cellrenderers
        combobox.pack_start(renderer_pixbuf, False)
        combobox.pack_start(renderer_text, False)

        # there is no set_attributes() in Python
        # associates a property of the cellrenderer to a column in the model
        # used by the combobox
        combobox.add_attribute(renderer_text, "text", 0)
        combobox.add_attribute(renderer_pixbuf, "stock_id", 1)
        # the first row is the active one
        combobox.set_active(0)

        # when a row is selected, emit a signal
        combobox.connect("changed", self.on_changed)

        self.add(combobox)

    def on_changed(self, combo):
        # if the row selected is not the first one, write on the terminal
        if combo.get_active() != 0:
			print "You chose " + str(actions[combo.get_active()][0]) +"\n"
        return True


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.example.combobox_multicolumn")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)

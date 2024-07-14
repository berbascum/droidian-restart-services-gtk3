#!/usr/bin/env python3

#[HEADER_SECTION]
#[HEADER_END]


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import subprocess
import os

class AboutDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "About", parent, 0)
        self.set_default_size(400, 300)
        #
        ## Config About dialog box
        box = self.get_content_area()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_border_width(10)
        box.add(vbox)
        #
        ## TODO: Add a logo
        #image_path = "/usr/share/service_manager/logo.png"  # Assegura't que tens un logo en aquest path
        #if os.path.exists(image_path):
        #    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(image_path, 100, 100, True)
        #    logo = Gtk.Image.new_from_pixbuf(pixbuf)
        #    vbox.pack_start(logo, False, False, 0)
        #
        ## Title
        title = Gtk.Label()
        title.set_markup("<big><b>Droidian Restart Services GTK3</b></big>")
        vbox.pack_start(title, False, False, 0)
        #
        ## Description
        label_about = Gtk.Label()
        label_about.set_justify(Gtk.Justification.CENTER)
        label_about.set_markup("<i>GTK GUI to restart systemd services</i>")
        vbox.pack_start(label_about, False, False, 0)
        #
        ## Add a separator
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        vbox.pack_start(separator, False, False, 10)
        #
        ## Create label for about info
        label_about_info = Gtk.Label()
        label_about_info.set_line_wrap(True)
        label_about_info.set_justify(Gtk.Justification.LEFT)
        label_about_info.set_selectable(True)
        self.get_content_area().add(label_about_info)
        #
        ## Load about info
        about_file_path = "/usr/share/droidian-restart-services-gtk3/about.txt"
        formatted_text = "Information not available."
        if os.path.exists(about_file_path):
            with open(about_file_path, "r") as f:
                lines = f.readlines()
                formatted_text = ""
                for line in lines:
                    if not line:
                        continue
                    key, _, value = line.partition(": ")
                    if key and value:
                        # Escapar els caràcters especials en el valor abans d'afegir al markup
                        escaped_value = GLib.markup_escape_text(value)
                        formatted_text += f"<b>{key}:</b> {escaped_value}\n"
                    else:
                        # Afegir el text sense formatar si no compleix el format clau: valor
                        formatted_text += line + "\n"
        #
        # Configurar el text amb Pango markup
        label_about_info.set_markup(formatted_text)
        #
        self.show_all()

class RestartServicesWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Restart Systemd Services GTK3")
        self.set_default_size(800, 600)
        #
        ## Create the main vbox
        main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(main_vbox)
        ## Box1 top 10%
        box_top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_top.set_size_request(-1, 60) ## In pixels
        main_vbox.pack_start(box_top, False, False, 0)
        ## Box2 services 20%
        box_services = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_services.set_size_request(-1, 120)  ## In pixels
        main_vbox.pack_start(box_services, False, False, 0)
        ## Box3 info 80%
        box_info = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box_info.set_size_request(-1, 450) ## In pixels
        main_vbox.pack_start(box_info, False, False, 0)
        box_info_label = Gtk.Label(label="Information:\n\nRestart the service that you want!")
        box_info.pack_start(box_info_label, True, True, 0)
        ## Box4 misc remaining
        box_misc = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_vbox.pack_start(box_misc, True, True, 0)
        #
        ## Create restart services buttons
        ## MetworkManager
        button1 = Gtk.Button(label="Restart NetworkManager Service")
        button1.connect("clicked", self.on_restart_clicked, "NetworkManager")
        box_services.pack_start(button1, True, True, 0)
        ## ModemManager
        button2 = Gtk.Button(label="Restart ModemManager Service")
        button2.connect("clicked", self.on_restart_clicked, "ModemManager")
        box_services.pack_start(button2, True, True, 0)
        ## Bluetooth
        button3 = Gtk.Button(label="Restart Bluetooth Service")
        button3.connect("clicked", self.on_restart_clicked, "bluetooth")
        box_services.pack_start(button3, True, True, 0)
        #
        ## Create misc buttons
        ## About
        button_about = Gtk.Button(label="About")
        #button_about.connect("clicked", lambda btn: AboutDialog(win).run())
        button_about.connect("clicked", self.on_about_clicked)
        box_misc.pack_start(button_about, True, True, 0)
        ## Exit
        exit_button = Gtk.Button(label="Exit")
        exit_button.connect("clicked", Gtk.main_quit)
        box_misc.pack_start(exit_button, True, True, 0)

    def on_restart_clicked(self, widget, service_name):
        command = f"pkexec systemctl restart {service_name}"
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Service '{service_name}' restarted successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error restarting service '{service_name}': {e.stderr.decode()}")

    def on_about_clicked(self, widget):
        about_dialog = AboutDialog(self)
        about_dialog.run()
        about_dialog.destroy()

win = RestartServicesWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


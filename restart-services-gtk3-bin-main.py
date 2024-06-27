#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class RestartServicesWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Restart Systemd Services GTK3")
        self.set_default_size(800, 600)

        ## Create main vbox
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

        ## Create restart services buttons
        ## ModemManager
        button1 = Gtk.Button(label="Restart ModemManager Service")
        button1.connect("clicked", self.on_restart_clicked, "ModemManager")
        box_services.pack_start(button1, True, True, 0)
        ## Bluetooth
        button2 = Gtk.Button(label="Restart Bluetooth Service")
        button2.connect("clicked", self.on_restart_clicked, "bluetooth")
        box_services.pack_start(button2, True, True, 0)

        ## Create misc buttons
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

win = RestartServicesWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


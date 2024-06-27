#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class RestartServicesWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Restart Systemd Services GTK3")
        self.set_default_size(800, 600)

        # Create main Paned 
        main_paned = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        self.add(main_paned)

        # Create top box
        top_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_paned.pack1(top_box, resize=False, shrink=False)

        # Create sub Paned1 
        sub_paned1 = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        main_paned.pack2(sub_paned1, resize=True, shrink=False)

        # Create buttons box
        buttons_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        sub_paned1.pack1(buttons_box, resize=False, shrink=False)

        # Create buttons_box buttons
        button1 = Gtk.Button(label="Restart ModemManager Service")
        button1.connect("clicked", self.on_restart_clicked, "ModemManager")
        buttons_box.pack_start(button1, True, True, 0)

        button2 = Gtk.Button(label="Restart Bluetooth Service")
        button2.connect("clicked", self.on_restart_clicked, "bluetooth")
        buttons_box.pack_start(button2, True, True, 0)

        exit_button = Gtk.Button(label="Exit")
        exit_button.connect("clicked", Gtk.main_quit)
        buttons_box.pack_start(exit_button, True, True, 0)

        # Create info box
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        sub_paned1.pack2(info_box, resize=False, shrink=False)
        info_box_label = Gtk.Label(label="Information:\n\nRestart the service that you want!")
        info_box.pack_start(info_box_label, True, True, 0)

        # Set Paneds heights
        main_paned.set_position(int(0.05 * 600))
        sub_paned1.set_position(int(0.2 * 600))

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


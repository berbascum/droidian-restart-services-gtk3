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
        button1 = Gtk.Button(label="Restart Service 1")
        button1.connect("clicked", self.restart_service, "service1")
        buttons_box.pack_start(button1, True, True, 0)

        button2 = Gtk.Button(label="Restart Service 2")
        button2.connect("clicked", self.restart_service, "service2")
        buttons_box.pack_start(button2, True, True, 0)

        exit_button = Gtk.Button(label="Exit")
        exit_button.connect("clicked", Gtk.main_quit)
        buttons_box.pack_start(exit_button, True, True, 0)

        # Create info box
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        sub_paned1.pack2(info_box, resize=False, shrink=False)
        info_box_label = Gtk.Label(label="Information:\n\nRestart the service that woy want!")
        info_box.pack_start(info_box_label, True, True, 0)

        # Set Paneds heights
        main_paned.set_position(int(0.05 * 600))
        sub_paned1.set_position(int(0.2 * 600))

    def restart_service(self, widget, service_name):
        subprocess.run(["sudo", "systemctl", "restart", service_name])

win = RestartServicesWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


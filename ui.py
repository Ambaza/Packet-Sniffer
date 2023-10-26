import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import track

class App:
  def __init__(self):
    # Create the main window
    self.window = tk.Tk()
    self.window.title("Packet Sniffer")
    
    # Create the IP label and entry
    ip_label = tk.Label(self.window, text="IP Address:")
    ip_label.grid(row=0, column=0)
    self.ip_entry = tk.Entry(self.window)
    self.ip_entry.grid(row=0, column=1)
    
    # Create the port label and entry
    port_label = tk.Label(self.window, text="Port:")
    port_label.grid(row=1, column=0)
    self.port_entry = tk.Entry(self.window)
    self.port_entry.grid(row=1, column=1)
    
    # Create the path label and entry
    path_label = tk.Label(self.window, text="Path:")
    path_label.grid(row=2, column=0)
    self.path_entry = tk.Entry(self.window)
    self.path_entry.grid(row=2, column=1)
    
    # Create the filter label and entry
    filter_label = tk.Label(self.window, text="Filter:")
    filter_label.grid(row=3, column=0)
    self.filter_entry = tk.Entry(self.window)
    self.filter_entry.grid(row=3, column=1)
    
    # Create the start button
    start_button = tk.Button(self.window, text="Start", command=self.start)
    start_button.grid(row=4, column=0)
    
    # Create the stop button
    stop_button = tk.Button(self.window, text="Stop", command=self.stop)
    stop_button.grid(row=4, column=1)
    
    # Create the save button
    save_button = tk.Button(self.window, text="Save", command=self.save)
    save_button.grid(row=4, column=2)
    
  def start(self):
    # Get the IP, port, path, and filter data from the entries
    site_ip = self.ip_entry.get()
    site_port = self.port_entry.get()
    path = self.path_entry.get()
    filter_data = self.filter_entry.get()
    
    # Start sniffing packets
    sniff.start_sniffing(site_ip, site_port, filter_data, path)
    
  def stop(self):
    # Stop sniffing packets
    sniff.stop_sniffing()
    
  def save(self):
    # Show a file save dialog
    file_path = filedialog.asksaveasfilename(defaultextension=".pkl")
    
    # Save the POST requests to the file
    sniff.post_display.save_posts(file_path)
    
    # Show a success message
    messagebox.showinfo("Success", "POST requests saved to file.")

# Create the app and start the main loop
app = App()
app.window.mainloop()

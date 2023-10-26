import re
import pickle
from scapy.all import *

# Define the PostDisplay class to display and save the POST requests
class PostDisplay:
  def __init__(self):
    self.posts = ""
  
  def add_post(self, post_data):
    # Add the POST request to the posts string
    self.posts += "\n" + post_data

  def save_posts(self, file_path):
    # Save the POST requests to the file
    with open(file_path, "wb") as f:
      pickle.dump(self.posts, f)

# Create a global PostDisplay object
post_display = PostDisplay()

# Define a function to display packets that match the target site and port and filter data
def display_packet(packet, filter_data):
  # Check if the packet is a POST request
  if packet.haslayer(Raw) and b"POST" in bytes(packet[Raw]):
    # Check if the packet contains the filter data
    if re.search(filter_data, bytes(packet[Raw])):
      # Extract the POST data from the packet
      post_data = re.search(b"POST(.+?)HTTP", bytes(packet[Raw])).group(1)
      # Add the POST data to the PostDisplay object
      post_display.add_post(post_data)

# Define a function to start sniffing packets
def start_sniffing(site_ip, site_port, filter_data, path):
  # Define the BPF filter
  bpf_filter = "host {} and port {} and path {}".format(site_ip, site_port, path)
  
  # Start sniffing packets using the display_packet function as a callback
  sniff(filter=bpf_filter, prn=lambda packet: display_packet(packet, filter_data))

# Define a function to stop sniffing packets
def stop_sniffing():
  # Stop sniffing packets
  sniff(stop_filter=lambda packet: True)

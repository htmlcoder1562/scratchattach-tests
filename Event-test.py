import scratchattach as sa
from getpass import getpass

session = sa.login(input("What's your username?\n"), getpass("What's your password? (hidden in terminal)")) # Log in to Scratch
cloud = session.connect_scratch_cloud("project_id") # Connect Scratch's cloud
events = cloud.events()

@events.event
def on_set(activity): #Called when a cloud var is set
    print(f"Variable {activity.var} was set to the value {activity.value} at {activity.timestamp}")
    # `activity` is a sa.CloudActivity object
    # To get the user who set the variable, call activity.load_log_data() which saves the username to the activity.username attribute

@events.event
def on_del(activity):
    print(f"{activity.user} deleted variable {activity.var}")

@events.event
def on_create(activity):
    print(f"{activity.user} created variable {activity.var}")

@events.event #Called when the event listener is ready
def on_ready():
   print("Event listener ready!")

events.start()

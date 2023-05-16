# go to  https://scratch.mit.edu/projects/851418630/ and Move up and down the test2 variable and look for a message here!
import scratchattach as scratch3
ProjID=input("What is the project ID?\n")
events=scratch3.CloudEvents(ProjID)
@events.event
def on_set(event): #Called when a cloud var is set
    print(f"{event.user} set the variable {event.var} to the valuee {event.value} at {event.timestamp}\n\n")

@events.event
def on_del(event):
    print(f"{event.user} deleted variable {event.var}\n\n")

@events.event
def on_create(event):
    print(f"{event.user} created variable {event.var}\n\n")

@events.event #Called when the event listener is ready
def on_ready():
   print("\nEvent listener ready!\nNote:When cloud events change, If this is on, you will get notified. enter To leave.\n\n\n\n")

events.start()
input()
events.stop()

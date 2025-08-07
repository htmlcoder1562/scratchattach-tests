import scratchattach as scratch3
from getpass import getpass
Done=0
uname=input("What is your username?\n")
pswd=getpass("What's your password for Scratch? (Hidden in the terminal)")
ProjID=input("What is the project id?\n")
while Done==0:
    varname=input("What is the name of the cloud variable?\n")
    value=input("What is the value? note: numbers only\n")
    session=scratch3.login(uname, pswd)
    conn=session.connect_cloud(ProjID)
    for x in ["1","2"]: # Repeated twice because the variables don't always change first thing
        conn.set_var(varname, value)
    answer=input("Done? (y/n)")
    if answer=="y":
        Done=1
    conn.disconnect()
# Test this at: https://scratch.mit.edu/projects/851418630/
# If you use that, then for the project ID, use this: 851418630

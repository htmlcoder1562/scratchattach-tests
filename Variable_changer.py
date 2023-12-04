import scratchattach as scratch3
Done=0
sessionID=input("What is your Session ID? You can find it at: https://github.com/TimMcCool/scratchattach/wiki/Get-your-session-id\n")
uname=input("What is your username?\n")
while Done==0:
    ProjID=input("What is the project id?\n")
    varname=input("What is the name of the cloud variable?\n")
    value=input("What is the value? note: numbers only\n")
    session=scratch3.Session(sessionID, username=uname)
    conn=session.connect_cloud(ProjID)
    for x in ["1","2"]
        conn.set_var(varname, value)
    answer=input("Done? y/n NOT yes, no, Y, or N")
    if answer=="y":
        Done=1
    conn.disconnect()
# Test this at: https://scratch.mit.edu/projects/851418630/
# If you use that, then for the project ID, use this: 851418630
# Also must have linux.

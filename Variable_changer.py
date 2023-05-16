import scratchattach as scratch3
Uname=input("What is your Username?")
Password=input("What is your password?")
ProjID=input("What is the project id?")
varname=input("What is the name of the cloud variable?")
value=input("What is the value?")
session=scratch3.login(Uname,Password)
conn=session.connect_cloud(ProjID)
conn.set_var(varname, value)
conn.disconnect()
# Test this at: https://scratch.mit.edu/projects/851418630/
# If you use that, then for the project ID, use this: 851418630

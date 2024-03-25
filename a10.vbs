Set oShell = CreateObject("Wscript.shell")
Dim strArgs
strArgs = "cmd /c a10.bat"
oShell.Run strArgs, 0, false
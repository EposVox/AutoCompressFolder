#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Define the hotkey that will run the Python script
^!p::
    ; Check if the active window is a Windows Explorer window
    If WinActive("ahk_class CabinetWClass") {
        ; Get the path of the currently-open folder in Windows Explorer
        Send ^l
        WinGetActiveTitle, current_folder
        StringReplace, current_folder, current_folder, Explorer, , All
        StringTrimLeft, current_folder, current_folder, 1
        StringTrimRight, current_folder, current_folder, 1

        ; Run the Python script on the currently-open folder
        Run, python C:\Users\eposv\Videos\compress_videos.py "%current_folder%"
    }
from os import rename,getcwd
import os
import customtkinter
from pytube import YouTube,Playlist
from tkinter import filedialog
import subprocess


font = "Bahnschrift"

window = customtkinter.CTk()
window.geometry("400x550")
window.title("YouTube Video Downloader")


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

def down_error_playlist():
    for widget in window.winfo_children():
            widget.destroy()

    frame = customtkinter.CTkFrame(master=window,width=400,height=400)
    frame.pack(padx=10,pady=10)

    label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Error while downloading! Try Again")
    label.pack(padx=0,pady=30)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(padx=20,pady=10)

    back_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Go Back",command=down_playlist)
    back_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    exit_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Exit",command=exitApp_playlist)
    exit_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(padx=20,pady=20)

    label = customtkinter.CTkLabel(master=frame,font=(font,12),text="NOTE:\n\n>> Some major reasons for the above error include...\n1. Inconsistent network connect\n2. No network connection\n3. Bug in the code\n4. Cannot connect to pytube library\n5. Video is recently removed\n6. File Already Exists in the selected Directory\n7. Directory recently removed")
    label.pack(pady=26)

def openfile_playlist():
    subprocess.Popen("explorer "+final_path)
def confirm_playlist():
    try:
        foldername1 = foldername.replace("/","\\")+"\\"
        global final_path
        final_path=folderpath_2.replace("/","\\")+"\\"+foldername1
        for video in p_playlist.videos:
            video.streams.get_highest_resolution().download(final_path)

        for widget in window.winfo_children():
            widget.destroy()

        frame = customtkinter.CTkFrame(master=window,width=400,height=400)
        frame.pack(padx=10,pady=10)

        label = customtkinter.CTkLabel(master=frame,font=(font,24),text=f"Downloaded Successfully!")
        label.pack(padx=30,pady=40)

        open_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Open Folder",command=openfile_playlist)
        open_btn.pack(pady=15,ipadx=2,ipady=2)

        goback_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Main Menu",command=mainPage)
        goback_btn.pack(pady=15,ipadx=2,ipady=2)

        exit_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Exit",command=exitApp_playlist)
        exit_btn.pack(pady=15,ipadx=2,ipady=2)

    except:
        down_error_playlist()

def exitApp_playlist():
    window.destroy()

def submit_playlist():
    try:
        p = Playlist(entry_playlist.get())

        global p_playlist
        p_playlist = p

        global foldername
        foldername = entry_name_playlist.get()

        global folderpath_2
        folderpath_2 = folder_path_playlist

        if folder_path_playlist=="" or folder_path_playlist=="Current Directory":
            folderpath_2=os.getcwd().replace("\\","/")

        foldername1 = foldername.replace("/","\\")
        final_path=folderpath_2+"/"+foldername1

        for widget in window.winfo_children():
            widget.destroy()

        frame = customtkinter.CTkFrame(master=window,width=400,height=400)
        frame.pack(padx=10,pady=10)

        label = customtkinter.CTkLabel(master=frame,wraplength=340,font=(font,18),text=f"Title of the playlist is :\n{p.title}\n\nAnd the Selected Directory is :\n{final_path}")
        label.pack(padx=20,pady=20)

        confirm_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Confirm",command=confirm_playlist)
        confirm_btn.pack(pady=10)

        back_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Go Back",command=down_playlist)
        back_btn.pack(pady=10)
    except:
        for widget in window.winfo_children():
            widget.destroy()

        frame = customtkinter.CTkFrame(master=window,width=400,height=400)
        frame.pack(padx=10,pady=10)

        label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Error! Try Again!")
        label.pack(padx=100,pady=40)

        label = customtkinter.CTkLabel(master=frame,text="")
        label.pack(padx=20,pady=20)

        back_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Go Back",command=down_playlist)
        back_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

        exit_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Exit",command=exitApp_playlist)
        exit_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

        label = customtkinter.CTkLabel(master=frame,text="")
        label.pack(padx=20,pady=40)

        label = customtkinter.CTkLabel(master=frame,font=(font,12),text="NOTE:\n\n>> Some major reasons for the above error include...\n1. Inconsistent network connect\n2. No network connection\n3. Bug in the code\n4. Cannot connect to pytube library\n5. Video is recently removed\n6. File Already Exists in the selected Directory\n7. Directory recently removed")
        label.pack(pady=20)

def path_playlist():
    global folder_path_playlist
    folder_path_playlist = filedialog.askdirectory()

def down_playlist():
    global folder_path_playlist
    folder_path_playlist="Current Directory"

    for widget in window.winfo_children():
        widget.destroy()

    frame = customtkinter.CTkFrame(master=window,width=400,height=400)
    frame.pack(padx=10,pady=10)

    label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Enter the link of the Playlist")
    label.pack(padx=30,pady=20)

    global entry_playlist
    entry_playlist = customtkinter.CTkEntry(master=frame,font=(font,20),placeholder_text="Link",width=230)
    entry_playlist.pack(padx=20,pady=20,ipadx=2,ipady=2)

    label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Enter the name for the folder in which the files are to be stored",wraplength=340)
    label.pack(padx=30,pady=20)

    global entry_name_playlist
    entry_name_playlist = customtkinter.CTkEntry(master=frame,font=(font,20),placeholder_text="",width=230)
    entry_name_playlist.pack(padx=20,pady=20,ipadx=2,ipady=2)

    path_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Select Directory",command=path_playlist)
    path_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    path_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Continue",command=submit_playlist)
    path_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    goback_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Go Back",command=mainPage)
    goback_btn.pack(pady=15,ipadx=2,ipady=2)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(pady=10)

def down_error():
    for widget in window.winfo_children():
            widget.destroy()

    frame = customtkinter.CTkFrame(master=window,width=400,height=400)
    frame.pack(padx=10,pady=10)

    label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Error while downloading! Try Again")
    label.pack(padx=0,pady=30)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(padx=20,pady=10)

    back_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Go Back",command=down_video)
    back_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    exit_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Exit",command=exitApp)
    exit_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(padx=20,pady=20)

    label = customtkinter.CTkLabel(master=frame,font=(font,12),text="NOTE:\n\n>> Some major reasons for the above error include...\n1. Inconsistent network connect\n2. No network connection\n3. Bug in the code\n4. Cannot connect to pytube library\n5. Video is recently removed\n6. File Already Exists in the selected Directory\n7. Directory recently removed")
    label.pack(pady=26)

def openfile():
    subprocess.Popen("explorer "+folder_path2.replace("/","\\"))
def confirm():
    try:
        global folder_path2
        folder_path2 = folder_path1
        yd = yt1.streams.get_highest_resolution()
        if filename1=="":
            yd.download(folder_path1.replace("/","\\"))
        else:
            filename12 =filename1 + ".mp4"
            yd.download(folder_path1.replace("/","\\"),filename=filename12)

        for widget in window.winfo_children():
            widget.destroy()

        frame = customtkinter.CTkFrame(master=window,width=400,height=400)
        frame.pack(padx=10,pady=10)

        label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Downloaded Successfully!")
        label.pack(padx=30,pady=40)

        open_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Open File",command=openfile)
        open_btn.pack(pady=15,ipadx=2,ipady=2)

        goback_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Main Menu",command=mainPage)
        goback_btn.pack(pady=15,ipadx=2,ipady=2)

        exit_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Exit",command=exitApp)
        exit_btn.pack(pady=15,ipadx=2,ipady=2)

    except:
        down_error()

def exitApp():
    window.destroy()

def submit():
    #try:
    yt = YouTube(entry.get())

    global yt1
    yt1 = yt

    global filename1
    filename1 = entry_name.get()
    for widget in window.winfo_children():
        widget.destroy()

    frame = customtkinter.CTkFrame(master=window,width=400,height=400)
    frame.pack(padx=10,pady=10)

    global folder_path1
    if folder_path == "" or folder_path=="Current Directory":
        folder_path1=os.getcwd()
    else:
        folder_path1=folder_path

    label = customtkinter.CTkLabel(master=frame,wraplength=340,font=(font,18),text=f"Title of the video is :\n{yt.title}\n\nAnd the Selected Directory is :\n{folder_path1}\n\nDuration Of Video : {yt.length} seconds")
    label.pack(padx=20,pady=20)

    confirm_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Confirm",command=confirm)
    confirm_btn.pack(pady=10)

    back_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Go Back",command=down_video)
    back_btn.pack(pady=10)
    '''except:
        for widget in window.winfo_children():
            widget.destroy()

        frame = customtkinter.CTkFrame(master=window,width=400,height=400)
        frame.pack(padx=10,pady=10)

        label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Error! Try Again!")
        label.pack(padx=100,pady=30)

        label = customtkinter.CTkLabel(master=frame,text="")
        label.pack(padx=20,pady=10)

        back_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Go Back",command=down_video)
        back_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

        exit_btn = customtkinter.CTkButton(master=frame,font=(font,20),text="Exit",command=exitApp)
        exit_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

        label = customtkinter.CTkLabel(master=frame,text="")
        label.pack(padx=20,pady=20)

        label = customtkinter.CTkLabel(master=frame,font=(font,12),text="NOTE:\n\n>> Some major reasons for the above error include...\n1. Inconsistent network connect\n2. No network connection\n3. Bug in the code\n4. Cannot connect to pytube library\n5. Video is recently removed\n6. File Already Exists in the selected Directory\n7. Directory recently removed")
        label.pack(pady=25)'''
def path():
    global folder_path
    folder_path = filedialog.askdirectory()

def mainPage():
    for widget in window.winfo_children():
        widget.destroy()


    frame = customtkinter.CTkFrame(master=window,width=400,height=400)
    frame.pack(padx=10,pady=10)

    label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Download a Video or a Playlist?")
    label.pack(padx=20,pady=30)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(padx=20,pady=10)

    vid_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Video",command=down_video)
    vid_btn.pack(padx=10,pady=15,ipadx=2,ipady=2)

    playlist_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Playlist",command=down_playlist)
    playlist_btn.pack(padx=10,pady=15,ipadx=2,ipady=2)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(padx=20,pady=20)

    label = customtkinter.CTkLabel(master=frame, font=(font,12),text="Note:\n\n>> The Video downloads are set in a way such that the best quality available is preferred for download according to the user's network speed but in most cases the quality is set to 720p.\n>> Report any bugs to the creator, Aditya Gautam (AdiBro027#0414 on Discord OR adityascottish27@gmail.com on Gmail)",wraplength=340)
    label.pack(pady=35)

def down_video():
    global folder_path
    folder_path="Current Directory"

    for widget in window.winfo_children():
        widget.destroy()

    frame = customtkinter.CTkFrame(master=window,width=400,height=400)
    frame.pack(padx=10,pady=10)

    label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Enter the link of the Video")
    label.pack(padx=48,pady=20)

    global entry
    entry = customtkinter.CTkEntry(master=frame,font=(font,20),placeholder_text="Link",width=230)
    entry.pack(padx=20,pady=20,ipadx=2,ipady=2)

    label = customtkinter.CTkLabel(master=frame,font=(font,24),text="Enter the name for the file")
    label.pack(padx=48,pady=20)

    global entry_name
    entry_name = customtkinter.CTkEntry(master=frame,font=(font,20),placeholder_text="Leave empty for default",width=230)
    entry_name.pack(padx=20,pady=20,ipadx=2,ipady=2)

    path_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Select Directory",command=path)
    path_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    path_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Continue",command=submit)
    path_btn.pack(padx=20,pady=15,ipadx=2,ipady=2)

    goback_btn = customtkinter.CTkButton(master=frame,font=(font,18),text="Go Back",command=mainPage)
    goback_btn.pack(pady=15,ipadx=2,ipady=2)

    label = customtkinter.CTkLabel(master=frame,text="")
    label.pack(pady=10)


mainPage()
window.mainloop()

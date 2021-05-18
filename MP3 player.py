from tkinter import *
import pygame
import os



class MusicPlayer:

    def __init__(self,root):

        self.root=root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")
        #self.root.resizable(0,0)

        pygame.init()

        pygame.mixer.init()

        self.track=StringVar()
        self.status=StringVar()

        trackframe=LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=600,height=100)

        songtrack=Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold")
        songtrack.grid(row=0,column=0,padx=10,pady=5)

        
        trackstatus=Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold")
        trackstatus.grid(row=0,column=1,padx=10,pady=5)

        buttonframe=LabelFrame(self.root,text="control panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=100,width=600,height=100)

        playbtn=Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
        playbtn.grid(row=0,column=0,padx=10,pady=5)

        pausebtn=Button(buttonframe, text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
        pausebtn.grid(row=0,column=1,padx=10,pady=5)

        unpausebtn=Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
        unpausebtn.grid(row=0,column=2,padx=10,pady=5)



        stopbtn=Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
        stopbtn.grid(row=0,column=3,padx=10,pady=5)

        songsframe=LabelFrame(self.root,text="songs playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=600,y=0,width=600,height=200)

        scrol_y=Scrollbar(songsframe,orient=VERTICAL)

        self.playlist=Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)

        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_y.config(command=self.playlist.yview)

        self.playlist.pack(fill=BOTH)

        os.chdir("/Users/jagad/Music/mymusic")

        songtracks=os.listdir()

        for track in songtracks:
                 self.playlist.insert(END,track)

    def playsong(self):

        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("--playing")

        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stopsong(self):

        self.status.set("--stopped")
        pygame.mixer.music.stop()
    

    def pausesong(self):

        self.status.set("--paused")
        pygame.mixer.music.pause()

    def unpausesong(self):

        self.status.set("--playing")
        pygame.mixer.music.unpause()


root=Tk()

MusicPlayer(root)

root.mainloop()
        
                        

        
        

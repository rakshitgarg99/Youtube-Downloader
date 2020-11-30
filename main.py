from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0 #get total size container


def progress(stream, chunk, file_handle, remaining=None):
    # gets the percentage of the file that has been downloaded
    file_downloaded = (file_size - file_handle)
    per = float((file_downloaded/file_size)*100)
    dbtn.config(text = "{:00.0f} %Downloaded".format(per))

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)

        # changing button text
        dbtn.config(text="Please wait...")
        dbtn.config(state=DISABLED)

        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return


        ob = YouTube(url, on_progress_callback=progress) # creating youtube object with url

        # strms = ob.streams.all()
        # for s in strms:
        #     print(s)

        strm = ob.streams.first()
        file_size = strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        print(file_size)
        # print(strm)
        # print(strm.filesize)
        # print(strm.title)
        # print(ob.description)

        strm.download(path_to_save_video) # now downloading the video
        print("done...")
        dbtn.config(text="Start Download")
        dbtn.config(state=NORMAL)
        showinfo("Downloaded Finished", "Downloaded Successfully")
        urlField.delete(0, END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("error occured !!")


def startDownloadThread():
    #create thread
    thread = Thread(target=startDownload)
    thread.start()

# start gui building
main = Tk()

# setting the title
main.title("My Youtube downloader")

# set the icon
main.iconbitmap('play.ico')

main.geometry("500x600")

# heading icon

file = PhotoImage(file="play.png")
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

# url textfield
urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)

# download button
dbtn = Button(main, text="Start download", font=("verdana", 18), relief="ridge", command=startDownloadThread)
dbtn.pack(side=TOP, pady=10)

# video title
vTitle = Label(main, text="video title")

main.mainloop() # opening main window
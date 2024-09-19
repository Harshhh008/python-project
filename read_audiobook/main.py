import pyttsx3
import PyPDF2

with open("object_oriented_python_tutorial.pdf","rb") as book:
    readbook= PyPDF2.PdfReader(book)         #read from book
    pages = len(readbook.pages)            #read pages
    print("number of pages : ",pages)

# this code is pyttsx3 and read book
    speaker = pyttsx3.init()  # init means initialize text to speech engine

    page_number = 7

    if page_number < pages:
        page = readbook.pages[page_number]    #read page wise
        text = page.extract_text()             #extrext text

        if text:
            speaker.say(text)
            speaker.runAndWait()
        else:
            print("no text found")

    else:
        print("page is out of range")

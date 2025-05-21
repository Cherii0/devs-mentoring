
class Note:

    def __init__(self, content, author = "Adrian"):
        self.__author = author
        self.__content = content
        import datetime
        time_now = datetime.datetime.now()
        self.__create_time = str(time_now.hour) + " : " +  str(time_now.minute)

    def __str__(self):
        return f" {self.__author} : {self.__content} at {self.__create_time}"


class Notebook:

    def __init__(self):
        self.__notes = []


    def add_existing_note(self, note):
        self.__notes.append(note)


    def add_new_note(self, author, content):
        note = Note(content, author)
        self.__notes.append(note)

    def notes_number(self):
        print(f"Notebook contains {len(self.__notes)} notes")

    def describe_notes(self):

        if len(self.__notes) == 0:
            print("Notebook is empty")
            return

        print("Current notes : ")
        for note in self.__notes:
            print(f"{note}")


def main():
    notebook = Notebook()
    # empty notebook
    notebook.describe_notes()

    # adding notes
    note1 = Note(author = "Jan", content = "Clean room")
    note2 = Note(author = "Jan", content = "Feed cat")
    notebook.add_existing_note(note1)
    notebook.add_existing_note(note2)
    notebook.add_new_note(author = "Adrian", content = "Make dinner")


    # notes after adding notes
    notebook.describe_notes()

    notebook.notes_number()

if __name__ == "__main__":
    main()

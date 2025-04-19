class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def type_text(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack.clear()  # Clear redo history 

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("Nothing to redo.")

    def show_text(self):
        print(f"\nCurrent Text: '{self.text}'\n")


#  Demo interaction (CLI simulation)
def run_editor():
    editor = TextEditor()
    while True:
        print("Options: [1] Type Text  [2] Undo  [3] Redo  [4] Show Text  [5] Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            new_text = input("Enter text to type: ")
            editor.type_text(new_text)
        elif choice == '2':
            editor.undo()
        elif choice == '3':
            editor.redo()
        elif choice == '4':
            editor.show_text()
        elif choice == '5':
            print("Exiting editor.")
            break
        else:
            print("Invalid choice.")


run_editor()

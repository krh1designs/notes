import json

# List to hold notes
notes = []

# Load notes from a file if it exists
def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

# Save notes to a file
def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

# Add a new note
def add_note(title, content):
    note = {
        'title': title,
        'content': content
    }
    notes.append(note)
    print(f"Note '{title}' added.")
    save_notes()

# View all notes
def view_notes():
    if notes:
        for idx, note in enumerate(notes):
            print(f"{idx + 1}. {note['title']}: {note['content']}")
    else:
        print("No notes available.")

# Update an existing note
def update_note(index, new_title, new_content):
    if 0 <= index < len(notes):
        notes[index]['title'] = new_title
        notes[index]['content'] = new_content
        print(f"Note {index + 1} updated.")
        save_notes()
    else:
        print("Invalid note index.")

# Delete a note
def delete_note(index):
    if 0 <= index < len(notes):
        deleted_note = notes.pop(index)
        print(f"Note '{deleted_note['title']}' deleted.")
        save_notes()
    else:
        print("Invalid note index.")

# Menu to interact with the user
def show_menu():
    print("\nMenu:")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

# Main script
load_notes()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        add_note(title, content)
    elif choice == '2':
        view_notes()
    elif choice == '3':
        index = int(input("Enter note number to update: ")) - 1
        new_title = input("Enter new title: ")
        new_content = input("Enter new content: ")
        update_note(index, new_title, new_content)
    elif choice == '4':
        index = int(input("Enter note number to delete: ")) - 1
        delete_note(index)
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again.")
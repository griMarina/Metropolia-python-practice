# Chapter 10 Exercise 4: Notebook: Using list with the notebook, pickle
import time
import pickle


def main():
    try:
        notebook = open('notebook.dat', 'rb')
    except IOError:
        notebook = open('notebook.dat', 'wb')
        print('No default notebook was found, created one.')

    notes = []
    while True:
        print('\n(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit')

        selection = input('Please select one: ')
        if selection == '1':
            for note in notes:
                print(note)

        elif selection == '2':
            new_note = input('Write a new note: ')
            notes.append(f'{new_note}:::{time.strftime("%X %x")}')

        elif selection == '3':
            note_inx = int(input(
                f'The list has {len(notes)} notes.\nWhich of them will be changed?: '))
            print(notes[note_inx])
            new_note = input('Give the new note: ')
            notes.pop(note_inx)
            notes.insert(note_inx, f'{new_note}:::{time.strftime("%X %x")}')

        elif selection == '4':
            note_inx = int(input(
                f'The list has {len(notes)} notes.\nWhich of them will be deleted?: '))
            print('Deleted note', notes[note_inx-1])
            notes.pop(note_inx-1)

        elif selection == '5':
            notebook = open('notebook.dat', 'wb')
            pickle.dump(notes, notebook)
            print('Notebook shutting down, thank you.')
            break
        else:
            print('Incorrect selection')


if __name__ == '__main__':
    main()

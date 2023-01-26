# Chapter 5 Exercise 4: Notebook: Read and write to the notebook
import time

while True:
    print('(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit')
    selection = input('Please select one: ')
    if selection == '1':
        with open('notebook.txt', 'r') as f:
            content = f.read()
            print(content)
    elif selection == '2':
        with open('notebook.txt', 'a') as f:
            note_time = time.strftime("%X %x")
            new_note = input('Write a new note: ')
            f.write(f'{new_note}:::{note_time}\n')
    elif selection == '3':
        with open('notebook.txt', 'w') as f:
            print('Notes deleted.')
            f.close()
    elif selection == '4':
        print('Notebook shutting down, thank you.')
        break
    else:
        print('Incorrect selection')

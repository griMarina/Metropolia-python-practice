# Chapter 5 Exercise 4: Notebook: Read and write to the notebook
# Chapter 8 Exercise 4: Notebook: Changing the written file.

import time


def main():
    filename = 'notebook.txt'
    try:
        open(filename, 'r')
    except IOError:
        open(filename, 'w')
        print('No default notebook was found, created one.')

    while True:
        print('Now using file', filename,
              '\n(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit')

        selection = input('Please select one: ')
        if selection == '1':
            with open(filename, 'r') as f:
                content = f.read()
                print(content)
        elif selection == '2':
            with open(filename, 'a') as f:
                note_time = time.strftime("%X %x")
                new_note = input('Write a new note: ')
                f.write(new_note + ':::' + note_time + '\n')
        elif selection == '3':
            with open(filename, 'w') as f:
                print('Notes deleted.')
                f.close()
        elif selection == '4':
            filename = input('Give the name of the new file: ')
            try:
                open(filename, 'r')
            except IOError:
                open(filename, 'w')
                print('No notebook with that name detected, created one.')
        elif selection == '5':
            print('Notebook shutting down, thank you.')
            break
        else:
            print('Incorrect selection')


if __name__ == '__main__':
    main()

from tkinter import Tk, Label, Entry, Button, IntVar, Radiobutton

f2cnotes = {'C': 'D', 'B': 'Dflat', 'Bflat': 'C', 'A': 'B', 'Aflat': 'Bflat', 'G': 'A', 'Gflat': 'Aflat', 'F': 'G', 'E': 'Gflat', 'Eflat': 'F', 'D': 'E', 'Dflat': 'Eflat'}
c2fnotes = {'D': 'C', 'Dflat': 'B', 'C': 'Bflat', 'B': 'A', 'Bflat': 'Aflat', 'A': 'G', 'Aflat': 'Gflat', 'G': 'F', 'Gflat': 'E', 'F': 'Eflat', 'E': 'D', 'Eflat': 'Dflat'}

class Score:
    """Encapsulates a line of music"""

    def __init__(self, notes):
        """Creates a score object"""
        self.notes = notes

    def flute2clar(self, note):
        if note in f2cnotes:
            return f2cnotes[note]
        else:
            return note

    def clar2flute(self, note):
        if note in c2fnotes:
            return c2fnotes[note]
        else:
            return note

class MusicGui(object):
    def __init__(self, score):
        self.score = score
        self.gui = self.makeGui()

    def makeGui(self):
        root = Tk()
        root.title('Clarinet/Flute Note Transposition')

        # Label
        note_label = Label(root, text='Enter the notes you want transposed')
        note_label.grid(row=0, column=0, sticky='w')

        # Entry
        note_entry = Entry(root)
        note_entry.grid(row=1, column=0, pady=5)

        # Label
        output_label = Label(root, text='Transposed Note:')
        output_label.grid(row=2, column=0, sticky='w')

        # Entry
        output_entry = Entry(root, state='readonly')
        output_entry.grid(row=3, column=0, pady=5)

        # Radio buttons
        instrument_label = Label(root, text='What instrument are you playing?')
        instrument_label.grid(row=4, column=0, sticky='w')
        instrument_var = IntVar()
        clarinet_radio = Radiobutton(root, text='Clarinet', variable=instrument_var, value=1)
        clarinet_radio.grid(row=5, column=0, sticky='w')
        flute_radio = Radiobutton(root, text='Flute', variable=instrument_var, value=2)
        flute_radio.grid(row=6, column=0, sticky='w')

        # Transpose button
        transpose_button = Button(root, text='Transpose', command=lambda: self.processButton(note_entry, output_entry, instrument_var.get()))
        transpose_button.grid(row=7, column=0, pady=10)

        # Reset button
        reset_button = Button(root, text='Reset', command=lambda: self.resetButton(note_entry, output_entry))
        reset_button.grid(row=8, column=0)

        # Exit button
        exit_button = Button(root, text='Exit', command=root.quit)
        exit_button.grid(row=9, column=0)

        return root

    def exitButton(self):
        self.gui.quit()

    def resetButton(self, note_entry, output_entry):
        note_entry.delete(0, 'end')
        output_entry.config(state='normal')
        output_entry.delete(0, 'end')
        output_entry.config(state='readonly')

    def processButton(self, note_entry, output_entry, instrument):
        sNote = note_entry.get()
        transposed_notes = []

        if instrument == 1:  # Clarinet
            transposed_notes = [self.score.flute2clar(note) for note in sNote.split()]
        elif instrument == 2:  # Flute
            transposed_notes = [self.score.clar2flute(note) for note in sNote.split()]

        transposed_notes_str = ' '.join(transposed_notes)
        output_entry.config(state='normal')
        output_entry.delete(0, 'end')
        output_entry.insert(0, transposed_notes_str)
        output_entry.config(state='readonly')

def main():
    score = Score([])
    gui = MusicGui(score)
    gui.gui.mainloop()

if __name__ == '__main__':
    main()

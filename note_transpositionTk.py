from tkintertoy import Window

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
        self.gui = Window()
        self.gui.setTitle('Clarinet/Flute Note Transposition')
        instruments = ['Clarinet','Flute']
        self.gui.addEntry('note_in', 'Enter the notes you want transposed')
        self.gui.addLabel('output', 'Transposed Note:')
        self.gui.addRadio('instrument', 'What instrument are you playing?', instruments)
        self.gui.addButton('command', 'Transpose', self.processButton)
        self.gui.plot('note_in', row=0)
        self.gui.plot('output', row=1)
        self.gui.plot('instrument', row=2)
        self.gui.plot('Transpose', row=3, pady=10)
        return gui

    def processButton(self):
        sNote = self.gui.get('note_in')
        instrument = self.gui.get('instrument')
        transposed_notes = []

        if instrument == 'Clarinet':
            transposed_notes = [self.score.flute2clar(note) for note in sNote.split()]
        elif instrument == 'Flute':
            transposed_notes = [self.score.clar2flute(note) for note in sNote.split()]

        transposed_notes_str = ' '.join(transposed_notes)
        self.gui.set('output', transposed_notes_str)

def main():
    gui = MusicGui(Score([]))
    gui.gui.go()

if __name__ == '__main__':
    main()

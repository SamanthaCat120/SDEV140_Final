f2cnotes = {'C': 'D', 'B': 'Dflat', 'Bflat': 'C', 'A': 'B', 'Aflat': 'Bflat', 'G': 'A', 'Gflat': 'Aflat', 'F': 'G', 'E': 'Gflat', 'Eflat': 'F', 'D': 'E', 'Dflat': 'Eflat'}

def getNote():
    notes_input = input('Enter a list of notes (separated by spaces): ')
    notes_list = notes_input.split()
    key_value_pairs = [(note, f2cnotes[note]) for note in notes_list if note in f2cnotes]
    return key_value_pairs

note_pairs = getNote()
print('Transposed notes:')
for key, value in note_pairs:
    print(value)

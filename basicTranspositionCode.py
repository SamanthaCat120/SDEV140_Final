def flute2clar():
    note_mapping = {
        'C': 1,
        'C#': 2,
        'Db': 2,
        'D': 3,
        'D#': 4,
        'Eb': 4,
        'E': 5,
        'F': 6,
        'F#': 7,
        'Gb': 7,
        'G': 8,
        'G#': 9,
        'Ab': 9,
        'A': 10,
        'A#': 11,
        'Bb': 11,
        'B': 12
    }

    number_mapping = {
        1: 'C',
        2: 'C#',
        3: 'D',
        4: 'Eb',
        5: 'E',
        6: 'F',
        7: 'F#',
        8: 'G',
        9: 'Ab',
        10: 'A',
        11: 'Bb',
        12: 'B'
    }

    s_notes = input('Enter the notes listed on the music (separated by spaces): ').split()
    t_notes = []
    for note in s_notes:
        octave = 0
        if note.endswith("'"):
            octave = 1
            note = note[:-1]
        elif note.endswith(","):
            octave = -1
            note = note[:-1]
        s_note = note_mapping.get(note.upper(), 0)
        t_note = s_note - 2 + octave * 12
        t_note = number_mapping.get(t_note, '')
        t_notes.append(t_note)

    print('These are the notes you would play on the Clarinet:', ' '.join(t_notes))

flute2clar()

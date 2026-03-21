




def beat_notations(input: str) -> str:
    """
    Input: "a 1 0 1 1" Output: "a2 a4 a4
    """

    entries = input.split(' ')
    instrument: str = entries[0]
    entries = [int(i) for i in entries[1:]]
    total = len(entries)

    print(entries)
    output: list[str] = []

    
    # move from left to right
    # if we encounter a 1, start building a note
    # if we have 0, continue note, track 10 -> 2/total - 2 / 4 -> half note
    # if we have 1, stop prev note, create new note

    i = 0
    curr_note_dur = -1 # no prev note
    while i < total:
        if entries[i] == 1 and curr_note_dur == -1:
            curr_note_dur = 1
        elif entries[i] == 1:
            # add previous note, and create a new note
            temp_dur = int(total / curr_note_dur )
            """
            2 = 4/2 = half note a2
            1 = 4/1 = quarter note a4
            """
            output.append(instrument + str(temp_dur))
            curr_note_dur = 1 # new note
        elif entries[i] == 0:
            curr_note_dur += 1 # continue playing the previous note
        i += 1

    # add note frmo the end
    temp_dur = int(total / curr_note_dur )
    output.append(instrument + str(temp_dur))

    return " ".join(output)



print(beat_notations("a 1 0 1 1"))






        
    


































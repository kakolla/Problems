




def beat_notations(input: str, input2: str) -> str:
    """
    Input: "a 1 0 1 1" Output: "a2 a4 a4
    """

        
    # move from left to right
    # if we encounter a 1, start building a note
    # if we have 0, continue note, track 10 -> 2/total - 2 / 4 -> half note
    # if we have 1, stop prev note, create new note

    from collections import defaultdict
    mp = defaultdict(list) # outputs for each instrument
     
    insts = [input, input2]
    # beat notes for each instrument
    for ins_input in insts:
        entries = ins_input.split(' ')
        instrument: str = entries[0]
        entries: list[int] = [int(i) for i in entries[1:]]
        total = len(entries)

        print(entries)
        output: list[str] = []


        i = 0
        curr_note_dur = 0 # no prev note
        tmp: str = ""
        while i < total:
            if entries[i] == 1 and curr_note_dur == 0:
                curr_note_dur = 1
                tmp += str(entries[i])
            elif entries[i] == 1:
                # add previous note, and create a new note
                temp_dur = int(total / curr_note_dur )
                """
                2 = 4/2 = half note a2
                1 = 4/1 = quarter note a4
                """
                if tmp and tmp[0] == '0': 
                    # signify this is no note being played E (empty)
                    mp[instrument].append(instrument + str(temp_dur) + 'E')
                else:
                    mp[instrument].append(instrument + str(temp_dur))

                curr_note_dur = 1 # new note
                tmp = str(entries[i]) # begin with new note
            elif entries[i] == 0:
                tmp += str(entries[i])
                curr_note_dur += 1 # continue playing the previous note
            i += 1

        # add note frmo the end
        temp_dur = int(total / curr_note_dur )
        mp[instrument].append(instrument + str(temp_dur))


    # part b: timestamp instrument lists, then go thru and find overlapping timestamp
    for k,v in mp.items():
        print(k, v)

    t = 0
    times = defaultdict(list) # timestamp : notes here
    for instr, note_list in mp.items():
        # a: [a2, a4, a4]
        t = 0
        for note in note_list:
            if note[-1] != 'E': # make sure its not a no op
                times[t].append(note)
                t += 1 / int(note[-1]) # 1, 2, 4, 8
            else:
                t += 1 / int(note[-2]) # b2E - add 1/2 for no op
    print()
    for t,v in times.items():
        print(t, v)

    # stitch back times, if matching note length, join them
    times = dict(sorted(times.items())) # sort by times

    ans = []
    for t, v in times.items():
        common = defaultdict(list)
        if len(v) > 1:
            # for loop for all isntrs finding shared notes
            # ex: 0.5 : [a4, b2, c4]
            for note in v:
                common[note[1]].append(note[0]) # ie 4: a,c
            # add into ans
            print(common)
            for a,b in common.items():
                if len(b) == 1:
                    ans.append(b[0] + a) # a4
                else:
                    tmp2 = "["
                    tmp2 += ','.join(b)  + "]" + a
                    ans.append(tmp2)
        else:
            ans.append(v[0])
                    


    print()
    return " ".join(ans)



print(beat_notations("a 1 0 1 1", "b 0 0 1 1"))






        
    


































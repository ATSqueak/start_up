'''

MadLibs Prog

User enters as:
noun
adjective
verb ending in -ing

Make a story using these three inputs

Example:

    Crazy Monkey

    Once upon a time there was a rich lady who wished to travel to the jungle as she has never been before.
    She made her travel plans and departed on the day she had set and very soon was quickly immersed in the deepest part
    of the jungle she soon heard some rustling noises unmistakable animal noises but also something else not quite right.
    She crept careful, anticipating and came upon a small clearing where in the centre sat a frail old monkey cradling her knees, rocking back and
    forth. It was a strange scene and the rich lady froze unable to move mesmerised by the sadness that seemed to emanate from this old creature.
    Suddenly becoming aware the monkey stopped and looked up eyeing the stranger before warily.. for a few seconds both simply remained fixated
     staring at the other. Then slowly the rich lady crept forward an arm tentatively stretched with an air of supplication hoping to offer
     any possible help to the small sad creature in front of her. The old monkey did not move and simply stared then with a frightening
     suddeness leapt up and dashed off in the opposite direction disappearing quickly into the jungle ahead.
     The rich lady stopped half way towards the centre of the clearing clearly upset with this reaction but then focusing on the ground saw to her
     suprise a small collection of fruit just in front of where the monkey had been sitting arranged into what looked like ....


Example 2:
 I had run out of <noun> so I sped off to the shops to get a new one. When I was <verb>ing I suddenly bumped into a <adjective>horse.

'''

print('Hello let\'s play some MadLibs')
print()
keep_playing = True
while keep_playing:
    noun = input('Please give me a noun: ')
    print()
    adjective = input('Please now give me an adjective: ')
    print()
    verb = input('And finally now give me a verb ending in -ing: ')

    print(
        'I had run out of a collection of {} so I sped off to the shops to get a new one. On my way whilst I was {} I '
        'suddenly bumped into a {} horse.'.format(
            noun, verb, adjective))
    play = input('Do you want to have another go?')
    if play.casefold() == 'n':
        keep_playing = False
        print('Goodbye thanks for playing')
    elif play.casefold() != 'n' and play.casefold() != 'y':
        keep_playing = False
        print('Goodbye thanks for playing')
        break

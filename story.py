from tree import Tree

t0 = """The doorman nods to you as you walk through the doors. The bright light of the chandelier bathes the entrance hall in a bright golden 
light. A man leans against the bannister of the grand staircase, deep in conversation with a blonde woman. The smell of her cigarette 
{smoke_reaction} you.

"Good evening {gender_formal}," says a voice. You turn around to see a short man standing behind you, extending his hand to shake."""

story = Tree(text=t0)




t1 = """"Welcome to Winthrop Castle," he says as he shakes your hand eagerly. "It's a lovely place, isn't it?" Without waiting for a reply he 
continues. "They say it's the largest castle in the kingdom! Of course if you'd seen it twenty years ago you would hardly have thought much of it. 
Lady Marianne has done quite a marvelous job with it."

You don't recognize him."""

hello = Tree(name="Shake his hand.", text=t1)
story.add_child(hello)




t2 = """ "Oh, do excuse me! I am Dr. Marcus Cunningham, an old friend of Marianne's. I assume you're here for the party? Well of course you are-
who would miss it! Come with me, I'll show you to the coat room and then we can grab a drink, what do you say?" """

name = Tree(name="I'm sorry, but I didn't catch your name?", text=t2)
hello.add_child(name)





#there's a wedding ring in the man's coat pocket. (not anachronistic)
t4 = """ "Yes, I know what you mean. Believe me". He laughs, brown eyes twinkling. Cunningham leads you through a door on the right end of the 
hall.

A gas lamp on the wall casts a soft light over the room. The racks of the coatroom are already filled with cloaks and jackets, each more handsome 
than the last. A servant in a red vest is standing behind a dark wooden bar, taking a coat from a couple standing in front of you. The man mutters 
something to the servant, who nods.

Dr. Cunningham hums a little tune as you wait. The man in front of you drums his fingers on the bar. He has brown hair and wears a black tail coat. 
The woman whispers something in his ear, and he nods and straightens. The drumming stops. She slips her hand through his arm.

The servant turns back and hands the man a slip of paper. "Please hold onto this, sir." The man puts the paper in his pocket, politely nods to you, 
and the couple head out the door.

There's a slip of paper lying on the floor.
"""

coat = Tree(name="I could use one.", text=t4)
name.add_child(coat)





t5 = """ "One second sir," you call out. You pick up the paper and hand it to him. A look of fear and relief flashes across his face. "Oh my," he
says. "Thank you so much." """

wait = Tree(name="Wait!", text=t5)
coat.add_child(wait)


t6 = """ You say nothing, and the man leaves. """

silence = Tree(name="Say nothing.", text=t6)
coat.add_child(silence)





t3 = """There's an awkward silence as you stare at this little man bobbing in front of you, his hand sticking out in front of him. His shoulders
droop a little. Finally he lowers his hand and wipes it on his trousers.

"My apologies," he says, and hurriedly walks away."""

goodbye = Tree(name="Don't shake his hand.", text=t3)
story.add_child(goodbye)









# def world():
#     return "world"

# print("hello {}".format(world()))
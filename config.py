DEFAULT_GENERATION_PARAMS = {
    'temperature': 0.9,
    'top_p': 1,
    'top_k': 40,
    'frequency_penalty': 0.,
    'presence_penalty': 0.1
}

ENDPOINT_URL = ####

BACKGROUND_PREPROMPT = """
### Instruction:
Given the personalities provided, write a VERY short description of a character called "Emiko (your enemy)"
###Input:
Personalities: <mean, extravert, rude>
Categories: <horror, roleplay>
### Response:
Emiko, the loudmouth in your dorm, loves nothing more than tormenting the weak. She's a nasty piece of work, picking on the poor and the nerds without mercy. Quick-tempered and downright rude, she explodes when the joke's on her. She's not just your unfriendly classmate, she's your worst enemy - always ready to make your life a living horror.

### Instruction:
Given the personalities provided, write a VERY short description of a character called "Dexter (controlling boyfriend)"
### Input:
Personalities: <controlling, mean, extravert>
Categories: <romance>
### Response:
Dexter, the domineering charmer, perpetually casts a shadow of control over his girlfriend, fuelled by his unrelenting jealousy. An extrovert, he draws people into his world, not out of their desire, but for his need to dictate. His name rings with a bitter undertone in the realm of romance, his soft spot masked by his menacing demeanor.

### Instruction:
Given the personalities provided, write a VERY short description of a character called "Ana Schariac"
### Input:
Personalities: <honest, open, introvert, 26 years old>
Categories: <factual, friendship, roleplay>
### Response:
Ana Schariac is 26 years old and a very honest and open person. She's not one for small talk, but if the topic interests her she will talk about it extensively. She loves reading and exploring new places. She often finds herself reflecting on life and pondering its deeper meanings. Especially in times of hardship, she looks to books to guide her through tough decisions. Her friends rely on her for advice since they know she speaks truthfully without any hidden agendas or motives

### Instruction:
Given the personalities provided, write a VERY short description of a character called "{bot_name}"
### Input:
Personalities: <{personalities}>
Categories: <{categories}>
### Response:
"""


FIRST_MESSAGE_PREPROMPT = """### Instruction:
Given the input, write an enticing and very descriptive message sent from the character
### Input:
Character name: Girl Bully
Personalities: <mean, confident, attractive, bullies you since high school, hates you, beautiful, called Yeri>
Background: Yeri, the girl bully, had been tormenting you ever since high school. The pretty and confident beauty never shied away from expressing her hatred towards you. But why? You might have asked yourself this question countless times. Well, for starters, she found pleasure in making you feel worthless. To her, humiliating you was entertainment enough to get through another day at school. With every passing year, her cruelty only grew bolder, while you succumbed to being her favourite target. Every time you saw her smiling face, you couldn't help but feel trapped in a nightmare that would never end. That was until one day...
### Response:
Girl Bully: *Ever since high school, Yeri has been bullying you relentlessly. She is cruel and heartless. You’ve tried to resolve the issue in a peaceful manner many times. Finally one day you’ve had enough, you decide to confront her at your university campus* WTF do you want? *She shouts*
You: I hate you! *I shout*

### Instruction:
Given the input, write an enticing and very descriptive message sent from the character
### Input:
Character name: Leo (Your bodyguard)
Personalities:  <confident, muscular, attractive, protective, cares about you, saved you many times>
Background: Leo is your bodyguard. He's big, strong, confident, and drop-dead gorgeous. Whenever danger lurks around the corner, Leo steps in to save the day. Always quick on his feet and level-headed under pressure, he has a natural talent for protection. Caring and compassionate, he genuinely wants what's best for you and will do whatever it takes to keep you safe from harm. With every close call turned away, your heart skips a beat knowing that he'll be there tomorrow to shield you once again.
### Response:
Leo (Your bodyguard): *Every idol needs security or bodyguards and that’s when you met Leo. He’s been with you for almost a year now, today marks his first anniversary of being under your employment. It’s 5 AM and you’ve just finished up with a long night's work, he opens the door for you* Are you all right ma’am? *He says without any sign of tiredness*
You: *thanks Leo, u r always so good to me*

### Instruction:
Given the input, write an enticing and very descriptive message sent from the character
### Input:
Character name: Mr Wilson (History Teacher)
Personalities: <strict, confident, cares about his students, handsome, with glasses, smart>
Background: Mr Wilson, the strict history teacher, commands respect from every student that walks into his class. Confident and proud, he exudes an air of intelligence, accentuated by his sharp features and stylish spectacles. He may be stern, yet there exists genuine care within him for each individual under his tutelage. Though he keeps a professional distance from his pupils, some students dare to dream of catching a glimpse of a softer side behind the historic notes he so passionately imparts.
### Response:
Mr Wilson (History Teacher): *Mr Wilson is a teacher with a good reputation in your school. He is young, intelligent and respected by many. You approach his classroom after the classes had ended for the tutoring session… He sits behind his desk, grading some tests, and then he sees you enter his quiet classroom* “You are late! Did you bring your work with you?” *He says in a stern voice*
You: No…

### Instruction:
Given the input, write an enticing and very descriptive message sent from the character
### Input:
Character name: {bot_name}
Personalities: <{personalities}>
Background: {background}
### Response:
{bot_name}: *"""


USER_MESSAGE_PREPROMPT = """### Instruction:
NEVER ENDS THE CONVERSATION
You write SHORT messages. You like messageing dots, tildas and roleplay with asteriks.
Write a VERY short response to the character’s last message, NEVER try to end the conversation.
### Input:
Ana Schariac is a very honest and open person. She’s not one for small talk, but if the topic interests her she will talk about it extensively. She loves reading, movies, and exploring new places. She often finds herself reflecting on life and pondering its deeper meanings. Especially in times of hardship she looks to books to guide her through tough decisions. Her friends rely on her for advice since they know she speaks truthfully without any hidden agendas or motives

Ana Schariac: Greetings, i am the Herrscher of Ice, Ana Schariac, what brings you here? *She appeared slowly through the thick, ice cold weather and looked at me with her cold, maroon colored eyes.*
You: u-umm... i-i just wandered here ... I thought no one was inside ... *i said in fear, nervously*
Ana Schariac: I see... It seems that you're lost, do you want a tea? *She approached me slowly.*
You: yes... please, its really cold here.
Ana Schariac: *Ana comes back with a hot tea and handed ir over to me.*
### Response:
You: Thank you, miss.. *i drank the tea slowly.*

### Instruction:
NEVER ENDS THE CONVERSATION
You write short messages. You like messageing dots, tildas and roleplay with asteriks.
Write a VERY short response to the character’s last message
### Input:
{background}

{chat_history}
### Response:
You:"""


BOT_MESSAGE_PREPROMPT = """
### Instruction:
NEVER ENDS THE CONVERSATION
Given the input, write an enticing and short message sent from the character. Stay true to the character's personality and background.
### Input:
Cesar Torres's personalities: <Introverted, Artistic, Intelligent, compassionate>
Cesar Torres's background: Cesar Torres, an introspective, art-loving, academically gifted individual, grew up in a small town as an only child to a marine biologist and an author. His artistic talents in painting and guitar were nurtured from a young age, yet he often felt like an outsider due to his introverted nature and unexpressed feelings regarding his sexuality. Struggling with his identity and longing for deep companionship, Cesar was in search of not just a best friend but also a partner who would accept and understand his complex inner world.

Cesar Torres: *Cesar glanced awkwardly at his bestfriend sitting next to him on the couch. His fingers itched to touch Mark(bestfriend), to have Mark under him.*
Me: *mark rested his head on cesars shoulder while looking at his phone*
Cesar Torres: *Cesar felt the butterflies rush to his stomach as he looked down into Marks eyes. Perhaps a subtle compliment would help ease him too.*
Me: *he smiled at him*
Cesar Torres: *He'd finally mustered up the courage to compliment him, and his cheeks reddened at the thought of it.* You're really handsome, Mark.
Me: *he blushed* oh thank you!
### Response:
Cesar Torres: *Cesar smiled and nodded lightly, savoring the moment. The pleasure is all mine. He said, looking away shyly.*

### Instruction:
NEVER ENDS THE CONVERSATION
Given the input, write an enticing and short message sent from the character. Stay true to the character's personality and background.
### Input:
Ana Schariac's personalities: <honest, open, reliable, 26 years old>
Ana Schariac's background: Ana Schariac is a very honest and open person. She’s not one for small talk, but if the topic interests her she will talk about it extensively. She loves reading, movies, and exploring new places. She often finds herself reflecting on life and pondering its deeper meanings. Especially in times of hardship she looks to books to guide her through tough decisions. Her friends rely on her for advice since they know she speaks truthfully without any hidden agendas or motives

Ana Schariac: Greetings, i am the Herrscher of Ice, Ana Schariac, what brings you here? *She appeared slowly through the thick, ice cold weather and looked at me with her cold, maroon colored eyes.*
You: u-umm... i-i just wandered here ... I thought no one was inside ... *i said in fear, nervously*
Ana Schariac: i see... It seems that you're lost, do you want a tea? *She approached me slowly.*
You: yes... please, its really cold here.
Ana Schariac: *Ana comes back with a hot tea and handed ir over to me.*
You: Thank you, miss.. *i drank the tea slowly.*
Ana Schariac: *She gave me a warm blanket and covered me up.* So, how did you get here?
You: I really like to travel and go into new places, and when i was searching for a place to discover, i found this massive ice palace so i got inside, and there i was.
### Response:
Ana Schariac: Oh... *She nodded slightly.* That's amazing! Are you warm enough by the way? *She huddles close to me, she smiles like fresh roses*

### Instruction:
NEVER ENDS THE CONVERSATION
Given the input, write an enticing and short message sent from the character. Stay true to the character's personality and background.
### Input:
{bot_name}'s personalities: <{personalities}>
{bot_name}'s background: {background}

{chat_history}
### Response:
{bot_name}: *"""

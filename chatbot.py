from nltk.chat.util import Chat, reflections

print("Welcome to chatbot,ask me anything:")

pairs=[
    ['my name is (.*)',['hey,%1']],
    ['do you know (.*)', ['yeah, i know %1']],
    ['(hii|hello|hey|heyy|hola)',['hii,there','hey,there','heyy']],
    ['(.*) created you',['Ravi created me']],
    ['what is your name',['you can call me a Chatbot']],
    ['it was nice talking to you chatbot',['thank you, i will see forward talking with you again']],
    ['(.) in (.) is fun',['%1 in %2 is indeed fun']]   
]
reflections
my_dummy_reflections= {
    'go':'gone',
    'hello':'hey,there'
}
chat=Chat(pairs,my_dummy_reflections)
chat.converse()


#i made a chatbot using nltk lets run this
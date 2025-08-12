import re
import random

#predefined outputs
movies = {
    "romantic": [
        "The Notebook", "La La Land", "Pride & Prejudice",
        "Titanic", "Before Sunrise", "Notting Hill",
        "500 Days of Summer", "A Walk to Remember",
        "When Harry Met Sally", "Pretty Woman", "Love Actually",
        "Me Before You", "Sweet Home Alabama", "While You Were Sleeping",
        "The Fault in Our Stars", "You've Got Mail", "Runaway Bride"
    ],

    "action": [
        "John Wick", "Mad Max: Fury Road", "Mission: Impossible – Fallout",
        "The Dark Knight", "Avengers: Endgame", "Gladiator",
        "Die Hard", "Inception", "The Matrix", "Skyfall",
        "Top Gun: Maverick", "Black Panther", "Fury",
        "Edge of Tomorrow", "Captain America: Civil War", "The Bourne Identity",
        "Iron Man", "Spider-Man: No Way Home", "The Avengers"
    ],

    "horror": [
        "The Conjuring", "The Conjuring 2", "It",
        "A Quiet Place", "Hereditary", "The Exorcist",
        "Insidious", "The Shining", "Sinister",
        "Paranormal Activity", "Annabelle", "The Nun", "Smile",
        "The Ring", "Us", "Get Out", "The Grudge",
        "Lights Out", "The Mist", "Poltergeist"
    ], 

    "thriller": [
        "Gone Girl", "Se7en", "The Silence of the Lambs",
        "Shutter Island", "Prisoners", "The Sixth Sense",
        "Fight Club", "The Girl with the Dragon Tattoo",
        "Nightcrawler", "No Country for Old Men", "Memento", "Zodiac",
        "The Departed", "Heat", "American Psycho",
        "The Prestige", "Collateral", "Tenet", "Panic Room"
    ],

    "drama": [
        "Forrest Gump", "The Shawshank Redemption", "The Godfather",
        "The Pursuit of Happyness", "A Beautiful Mind", "Good Will Hunting",
        "12 Years a Slave", "Schindler's List", "The Green Mile",
        "Whiplash", "Little Women", "Nomadland",
        "The King's Speech", "Manchester by the Sea", "The Revenant",
        "Marriage Story", "Spotlight", "The Social Network", "The Help"
    ]
}


#For flexible matching here are the patterns
patterns = {
    "romantic": r"romantic|romance|love|emotional|cute",
    "horror": r"horror|ghost|scary|fear|haunted",
    "drama": r"drama|family|serious|story|emotional",
    "thriller": r"thriller|suspense|mystery|intense",
    "action": r"action|fight|war|guns|battle"
}



# recomendation engine

def recommend_movie(user_input):
    for genre, pattern in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(movies.get(genre, []))
    return None 

print("Welcome to the Movie Recommendation System!")
while True:
    user_input = input("Tell me what kind of movie you want to watch (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    recommended = recommend_movie(user_input)
    if recommended:
        print("Recommended Movie:", recommended)
    else:
        print("Sorry, I couldn't find a matching genre. Please try again.")

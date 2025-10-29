# opgave fra opgen kap 8


def display_message():
    """Display a message about what I'm learning."""
    print("I'm learning about functions in Python!")

# Call the function
display_message()

# Exercise 8-2: Favorite Book
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as "One of my favorite books is Alice in Wonderland."
# Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    print (f"min yndlings bog er {title}")

favorite_book("star wars")
favorite_book("time riders")         
# Here I will write the c

# Exercise 8-3: T-Shirt
# Write a function called make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt. The function should print a sentence summarizing
# the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt( text, size = "XXL"):
    print(f'stårelsen på din trøje bliver {size} og der kommer til at stå " {text} "')


make_shirt('what is up my freind',"small",)
make_shirt('are you fat like me')

# Exercise 8-7: Album
# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return
# a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
# If the calling line includes a value for the number of tracks, add that value to the album's dictionary.
# Make at least one new function call that includes the number of tracks on an album.


def make_album(name, album_title): 
    album= {
        'artist':name, 
        'title':album_title,}
    return album


album1=make_album("the weeknd", "starboy")
print(album1)

# Exercise 8-8: User Albums
# Start with your program from Exercise 8-7. Write a while loop that allows users
# to enter an album's artist and title. Once you have that information, call make_album()
# with the user's input and print the dictionary that's created.
# Be sure to include a quit value in the while loop.
print('album programmet')
print('skriv "qiut" ved artistens navn eller navnet på titlen for at stoppe ')

while True:
    name = input("hvad er navnet på din y kunsterne?  ")
    if name== 'slut':
        break

    album_title = input("hvad er dit y album fra  {name} ?  ")
    if album_title== 'slut':
        break   
    album =make_album(name,album_title)
    print(f"dit y album er {album}")
    print(' vil du forsætte ellrs skriv slut') 

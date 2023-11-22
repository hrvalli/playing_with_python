# Define the bottles_song function
# with the start argument defaulting to 99
def bottles_song(start = 0):
    # Set the initial number of bottle sto the start argument
    bottles = start
    # Loop through until bottles are gone
    while bottles < 100:
        # Display the song
        verse = str(bottles) + " bottles of beeer on the wall. "
        verse += str(bottles) + " bottles of beer. "
        verse += "Pick one up, from the truck "
        # Add a bottle
        bottles += 1
        verse += str(bottles) + " bottles of beer on the wall." 
        # Yield to the calling function
        yield verse# Pick back up here when we return
    return True 
# Loop through the generator
for v in bottles_song():
    print(v)
name = input("What's your name? ")

# Remove whitespace (strip) and capitalize (title) user's name:
name= name.stripe()
name = name.title()

# # Combining above two methods into one line:
name = name.strip().title()

#This is the same as:
x = name.strip()
name = x.title()

print(f"hello, {name}")


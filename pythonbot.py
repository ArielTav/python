print("hello, let's talk")
name = input("enter your name: ")

print("hello", name)
add = input("where do you live? ")

print("nice", add, "is a nice place")
race = input("what is your race? ")

print("oh, I love", race, "I mean, I am", race)
gender = input("what is your gender? ")

print("you've got a nice gender. I am a", gender)
hate = input("what do you hate the most? ")

print("I hate", hate, "too")
job = input("What do you do for a living? ")

print("Wow, being a", job, "sounds interesting.")
hobby = input("What's your favorite hobby? ")

print("That's cool! I like", hobby, "too.")
favorite_food = input("What's your favorite food? ")

print(favorite_food, "sounds delicious!")
dream = input("What's your biggest dream? ")

print("That's a beautiful dream!", dream)
print("it's really nice to talk to ya, let's talk more")

while True:
    rank = input("what is your rank in fortnite? ")
    
    if rank == "bronze":
        print("you are such a loser bro,", rank, "is a bad rank")
        break
    elif rank == "silver":
        print(rank, "is a bad rank bro")
        break
    elif rank == "gold":
        print("you have to get better,", rank, "is not enough")
        break
    elif rank == "platinum":
        print(rank, "is a nice rank")
        break
    elif rank == "diamond":
        print("yo bro,", rank, "is a very nice rank")
        break
    elif rank == "elite":
        print("good job man, keep working,", rank, "is a great rank")
        break
    elif rank == "champion":
        print("one more brooo, only one more! you are a freaking", rank, "it's amazing")
        break
    elif rank == "unreal":
        print("you are the best bro, let's play 1v1 one day,", rank, "is the best rank in fortnite. Please keep working hard")
        break
    elif rank == "I don't have a rank":
        print("loser!")
        break
    else:
        print("There is no such rank like that in fortnite. Please try again.")

while True:
    try:
        skin = int(input("how many skins do you have?"))
        
        if skin <= 10 and skin < 50:
            print("you are such a loser")
            break
        elif skin <= 50 and skin < 150:
            print("that's a nice collection")
            break
        elif skin <= 150 and skin < 500:
            print("you got it bro")
            break
        elif skin <= 500 and skin < 1800:
            print("you are crazy about skins!")
            break
        elif skin <= 1800 and skin < 1801:
            print("hell nah")
            break
        elif skin >= 1801:
            print("that is not possible, try again")
        else:
            print("that is not a number bro please try again")  
    except ValueError:
        print("that is not a number bro please try again")

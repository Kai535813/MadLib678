Start = input("Would you like to create a Mad Lib story? yes/no: ")
while Start == "yes":
    Topic = input("What kind of topic would you like? Simon Story/2/Colonoscopy/Political Speech: ")
    if Topic == "Simon Story":
        Input1 = input("Type a living thing: ")
        Input2 = input("Type a male name: ")
        Input3 = input("Type a name of a place: ")
        Input4 = input("Type a female name: ")
        Input5 = input("Type a ethnicity: ")
        Input6 = input("Type a body part: ")
        Input7 = input("Type a action: ")
        Input8 = input("Type a class subject: ")
        Input9 = input("Type a body part: ")
        Input10 = input("Type a: ")
        Input11 = input("Type a: ")
        Input12 = input("Type a: ")
        Input13 = input("Type a: ")
        Input14 = input("Type a: ")
        Input15 = input("Type a: ")
        print("Mad Libs Testing Format: " + Input1 + Input2 + Input3)
    if Topic == "2":
        Input1 = input("Type a: ")
        Input2 = input("Type a: ")
        Input3 = input("Type a: ")
        Input4 = input("Type a: ")
        Input5 = input("Type a: ")
        Input6 = input("Type a: ")
        Input7 = input("Type a: ")
        Input8 = input("Type a: ")
        Input9 = input("Type a: ")
        Input10 = input("Type a: ")
        Input11 = input("Type a: ")
        Input12 = input("Type a: ")
        Input13 = input("Type a: ")
        Input14 = input("Type a: ")
        Input15 = input("Type a: ")
        print("Mad Libs Testing Format: " + Input1 + Input2 + Input3)
    if Topic == "Colonoscopy":
        Input1 = input("Type a male name: ")
        Input2 = input("Type a reason : ")
        Input3 = input("Type a: ")
        Input4 = input("Type a: ")
        Input5 = input("Type a: ")
        Input6 = input("Type a: ")
        Input7 = input("Type a: ")
        Input8 = input("Type a: ")
        Input9 = input("Type a: ")
        Input10 = input("Type a: ")
        Input11 = input("Type a: ")
        Input12 = input("Type a: ")
        Input13 = input("Type a: ")
        Input14 = input("Type a: ")
        Input15 = input("Type a: ")
        print(Input1 + " is finally read for his Colonoscopy after a whole night of defecating loose liquid stool" + Input1 + " was very grouchy when he got to his appoitment because " 
             + Input2  + ". The real reason that" + Input1 + "decided to get a Colonoscopy on this day, was so that he could miss his daughter's " + Input3 + ".")
    if Topic == "Political Speech":
        Input1 = input("Choose a funny occupation: ")
        Input2 = input("Type of drug: ")
        Input3 = input("A type of company: ")
        Input4 = input("Something funny: ")
        Input5 = input("Something that you own: ")
        Input6 = input("A large positive integer number: ")
        Input7 = input("An even larger positive integer number: ")
        Input8 = input("One more even larger positive integer number: ")
        Input9 = input("Type a direction: ")
        Input10 = input("Something cute and friendly: ")
        Input11 = input("Any thing: ")
        Input12 = input("Another different thing: ")
        Input13 = input("Another funny occupation: ")
        Input14 = input("A large commercial website: ")
        Input15 = input("A type of service: ")
        print(f"""This Mad Lib is not meant to endores the speaker, " \
        "it is rather that this person is relavent and the speech was very convinient to use.""")
        Understand = input("Move forward? Type y: ")
        if Understand == "y":
            print(f"""In addition, I'm doing what no {Input1} of either party has ever done. 
                   Standing up to the special interests to dramatically reduce the price of {Input2} drugs. 
                   I negotiated directly with the {Input3}
                 and {Input4}, which were taken advantage of our {Input5} for many decades  
                to slash prices on drugs and pharmaceuticals by as much as {Input6}, {Input7} and even {Input8} 
                 percent. In other words, your drug costs will be "
                plummeting {Input9}, and I use the threat of {Input10} to get {Input4} who  
                would never have done it, to pay the cost of this giant {Input11} reduction. They 
                stop ripping us off. And it began as of four days ago.
                There has never been anything like this in the history of our country. 
                Drugs have only gone up, but now they'll be going down by {Input12} never conceived'
                ' possible. It's called most favored nation, and no {Input13}
                  has ever had the courage or ability to get this done, until now. 
                  The first of these unprecedented price reductions will be available starting in 
                  January through a new website, {Input14}. 
                  And these big price cuts will greatly reduce the cost of {Input15}.""")

    
    print("Why end now?! ")
while Start != "yes":
    print(f"""You could have had so much fun, but you choose not to. Bye Bye, 
          but I mean if you choose to leave it's obvious you do not value Util, 
          therefore you will loose your next ballot. And judge, 
          this is why you should vote for the affirmative. """)
    break
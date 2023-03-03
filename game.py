name = input("Type your name: ")
print("Welcome", name, "you are about to embark on a jungle adventure!")

answer = input("You are rafting on a river nestled in a dense forest, the river splits and you can choose to go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You notice a small set of rapids leading downwards to the left. Do you want to go down them? Type rapids to take the rapids or type carry on to continue straight: ")
    
    if answer == "rapids":
        answer = input("You cling on to the sides of raft and head down the rapids. The raft bounces off of rocks and nearly knocks you off, but you make it down safely to what seems to be a small lake with a pristine white sandy beach ahead. Type beach to explore the beach: ")
        if answer == "beach":
            answer = input("You notice a cave to the left and a skeleton perched up against a large rock to the right. Type left to go into the cave or type right to investigate the skeleton: ")
            
            if answer == "left":
                print("You enter the cave and see a glowing set of eyes open. The eyes jolt towards you and you feel two sharp fangs pierce your skin. The poison of the venemous snake sets in. Your adventure has ended. ")
            elif answer == "right":
                print("As you approach the skeleton, you trip over a chest and fall to the ground. You look behind you and see a pile of gold coins! Congratulations! ")
            else:print("Not a valid selection. Your adventure has ended. ")
              
    elif answer == "carry on":
        answer = input("As you continue down the river you notice a path outlined in the trees. As you get closer you notice the river seems to disapper ahead, but you see a path on the shore that leads into the woods on your right. Type keep going to continue straight or type woods to take the path: ")
        
        if answer == "keep going":
            answer = input("You continue heading down the river, you notice the current of the river speeds up drastically. Suddnly you hear rushing water, its a waterfall! You plummet down the waterfall..... You wake up in a turquoise bay underneatrh the waterfall. As you gather your bearings you notice a vibrant glow in the water underneath you. You also notice a grove behind the waterfall. Type dive to inspect the glow in the water or type grove to go behind the waterfall: ")
            if answer == "dive":
                answer = input("You dive beneath the water. You see there are now two glowing objects. A red glow seems be deeper, a blue glow is off to your left. Type red to investigate the red glow or blue to investigate the blue glow: ")
                if answer == "red":
                    print("You dive deeper and deeper but the red glow does not seem to be any closer. You continue to dive deeper... you run out of air. Your adventure has ended. ")
                elif answer == "blue":
                    print("You swim towards the blue light, you traverse through a door and stumble upon the lost city of atlantis! Congratulations you have won! ")
            elif answer == "grove":
                answer = input("You walk through a small opening behind the waterfall. You enter a dimly lit tunnel. You notice what looks to be a fire in the distance. Type forward to continue to towards the light in the distance or type leave to exit the cave: ")
                if answer == "forward":
                    answer = input("You continue forward and approcah an entrance into another room in the cave that is lit by a small torch. Type room to enter the room or tyoe exit to leave the cave: ")
                    if answer == "room":
                        print("You enter the room, you stumble upon a room filled with lost treasure. Congratulations! You have won! ")
                    elif answer == "exit":
                        print("You turn around to exit the cave, as you approach the exit the ground starts to rumble. You rush towards the exit... the exit crumbles in on you. Your adventure has ended.")
                    else:
                        print("Not a valid selection. Your adventure has ended. ")
                elif answer == "leave":
                    print("You turn around to exit the cave, as you approach the exit the ground starts to rumble. You rush towards the exit... the exit crumbles in on you. Your adventure has ended. ")
                else:
                    print("Not a valid selection. Your adventure has ended. ")
            else:
                print("Not a valid selection. Your adventure has ended. ")
        elif answer == "woods":
            answer = input("You exit the raft and enter the dense jungle forest. As you continue into the jungle, you spot a treehouse above you. Type up to investigate the treehouse or type continue to go further into the jungle. ")
            if answer == "up":
                print("You climb up the frailed rope ladder, as you near the treehouse entrance the rope ladder gives way! You plummet back to the ground. Your adventure has ended. ")
            elif answer == "continue":
                answer = input("You continue into the jungle and come across a cave entrance. Type enter to enter the cave or type coninue to traverse deeper into the forest: ")
                if answer == "continue":
                    print("You continue deeper into the jungle and stumble upon a snake nest! The snakes attack... Your adventure has ended. ")
                elif answer == "enter":
                    answer = input("You enter the cave and notice a glowing object in the distance. Type object to continue deeper into the cave or type exit to leave the cave: ")
                    if answer == "object":
                        print("You continue towards the object and stumble upon a stash of priate treasure! Congratulations you have won! ")
                    elif answer == "exit":
                        print("You turn around to exit the cave, as you approach the exit the ground starts to rumble. You rush towards the exit... the exit crumbles in on you. Your adventure has ended.")
                    else: 
                        print("Invalid selection. Your adventure has ended. ")
                else:
                    print("Invalid selection. Your adventure has ended. ")
            else:
                print("Invalid selection. Your adventure has ended. ")
        else:
            print("Invalid selection. Your adventure has ended. ")
    else:
        print("Not a valid selection. You lose. ")

elif answer == "right":
    answer = input("As you float down the river you begin to approach a beach. You tie your raft up to the dock and notice two paths leading into the jungle. Would you like to go left or right? ")

    if answer == "left":
        answer = input("As you make your way through the dense forest you come up on a large ravine. You notice an old rickity bridge that seems to be falling apart that crosses to the other side. You also notice a vine hanging from a tall tree that could be used to swing across. Type old bridge to use the rickity bridge, or type vine to swing across. ")

        if answer == "old bridge":
            answer = input("The bridge sways as you cross... the ropes holding the bridge up snap! You leap for the cliffside and manage to hang on. You climb up the cliffside and continue into the jungle. You notice small crashed airplane covered in vines to your left and a run down tree house to your right. Type left to investigate the airplane or type right to investigate the treehouse: ")
            if answer == "left":
                print("You approcah the airplane. It seems to have crashed long ago. You notice the door is propped open but a loud hissing sound is coming from the inside. Type enter to investigate the airplane or type back to continue into the jungle: ")
                if answer == "enter":
                    print("You enter the airplane and stumble upon a nest of venemous snakes! The snakes attack you... Your adventure has ended")
                elif answer == "back":
                    answer = input("You turn around and continue into the jungle. As you move forawrd you step on a pile of leaves and plummet into an underground cave. You stand up confused, you notice a glowing blue object to your left and a dimly lit torch to your right. Type left to move towards the blue light or type right to move towards the dimly lit torch. ")
                    if answer == "left":
                        print("You move towards the blue light and it becomes brighter and brigher. You trip over a large gold pot. You look up and discover you have stumbled upon a hidden treasure hoard! Congratulations you won!")
                    elif answer == "right":
                        ("You move toward the light and notice the cave splits. Type left to go into the left entrance or type right to go into the right entrance: ")
                        if answer == "left":
                            print("You move further into the cave... the gound starts shake. The roof collapses. Your adventure has ended. ")
                        elif answer == "right":
                            answer = input("You move further into the cave and notice a pool of water with a glowing light coming from it. Type dive to dive into the water or type exit to go back: ")
                            if answer == "dive":
                                print("You dive into the water and swim toward the light. You enter through a glowing door. You have discovered the lost city of Atlantis! Congratulations you won! ")
                            elif answer =="exit":
                                print("The gound starts shake. The roof collapses. Your adventure has ended. ")
                            else:
                                print("Invalid selection. Your adventure has ended.")
                        else:
                            print("Invalid selection. Your adventure has ended. ")
                    else:
                        print("Invalid selection. Your adventure has ended. ")
                else:
                    print("Invalid selection. Your adventure has ended. ")
            elif answer == "right":
                print("You begin climbing up the frailed ladder, as you approach the top the rope breaks! You plummet to the ground... Your adventure has ended. ")
            else:
                print("Invalid selection. Your adventure has ended. ")
        elif answer == "vine":
            print("You grab ahold of the vine, you attempt to swing across the ravine, the vine breaks! Your adventure has ended. ")
        else:
            print("Not a valid selection. Your adventure has ended. ")
    elif answer == "right":
        answer = input("You enter into the jungle and notice an old run down shack you also see a dock with an old canoe tied to it. Type shack to enter the shack or type canoe to enter the canoe: ")
        if answer == "shack":
            answer = input("You enter the shack, there is a staircase going up and one going down. Type up to go upstairs or type down to go downstairs: ")
            if answer == "up":
                print("You go upstairs and the floor collapses! You plummet to the ground... Your adventure has ended. ")
            elif answer == "down":
                answer = input("You head downstairs and notice an an open door to your left and another door to your right that seems to lead down further into the shack. Type right to enter the room or type door to move further down: ")
                if answer == "right":
                    print("You enter the room and stumble upon a treauser hoard! Congratulations you have won!")
                elif answer == "door":
                    print("You enter the doorway and there is no stair beneath you! You fall into a cold basement. Your adventure has ended. ")
                else:
                    print("Not a valid selection. Your adventure has ended. ")
            else:
                print("Not a valid selection. Your adventure has ended. ")
        elif answer == "canoe":
            answer = input("You enter the canoe and continue down the river. You spot a bay to your right and notice the current becomes faster in front of you. Type bay to enter the bay or type continue to move further down the river: ")
            if answer == "bay":
                answer = input("You enter the bay and notice a large abonded pirate ship and a waterfall to right of it. Type ship to board the pirate ship or type waterfall to investigate the waterfallL: ")
                if answer == "ship":
                    answer = input("You board the pirate ship and head below deck. You notice the captain's quarters door is propped open and you spot a staicase heading below deck. Type captain to enter the captain's quarters or type down to go down the staircase: ")
                    if answer == "captain":
                        print("You enter the captain's quarters and find a treasure chest! Congratulations you won the game. ")
                    elif answer == "down":
                        print("You head down the stairs and stumble upon a snake nest! Your adventure has ended. ")
                    else:
                        print("Not a valid selection. Your adventure has ended. ")
                elif answer == "waterfall":
                    print("You approach the waterfall but a shark attacks your canoe! Your adventure has ended. ")
                else:
                    print("Not a valid selection. Your adventure has ended. ")
            elif answer == "continue":
                answer = input("You move foward down the river and notice the water is beginning to change colors... you enter into a large bay, the water is pitch black... The kraken appears! It lunges one of it's tentacles at you. Type oar to try and block with your oar or type duck to try and avoid the attack: ")
                if answer == "oar":
                    answer = input("The tantacle lunges towards you and you raise your oar... you blocked the attack! The kraken dives back into the water to prepare for it's next attack. Large waves begin to form, the kraken raises it's tentacle out of the water attempting to split your canoe in half. Type right to lean to the right or left to lean to the left: ")
                    if answer == "right":
                        print("The kraken swings it tentacle with force to the righ of your canoe! Your adventure has ended. ")
                    elif answer == "left":
                        answer == input("You dodged the attack! The kraken peeks it's head out of the water. You see it's wide open eye and it's weak spot in it's tentacles. Type eye to lunge for the eye or tentacle to lunge for the tentacle: ")
                        if answer == ("eye"):
                            print("You lunge for the large eyeball... all of a sudden you feel a tentacle grab ahold of you. Your adventure has ended. ")
                        elif answer == "tentacle":
                            print("You lung for the tentacle, it expected you to lunge for the eye. You found the weak spot and have defeated the kraken! Congratulations you won. ")
                        else: 
                            print("Not a valid selection. Your adventure has ended. ")
                    else:
                        print("Not a valid selection. Your adventure has ended. ")
                elif answer == "duck":
                    answer = print("You attempt to duck but the kraken raises another tentacle and splits your canoe in half. Your adventure has ended. ")
                else:
                    ("Not a valid selection. Your adventure has ended. ")
            else:
                ("Not a valid selection. Your adventure has ended. ")
        else:
            print("Not a valid selection. Your adventure has ended. ")
    else:
        print("Not a valid selection. Your adventure has ended. ")
else:
    print("Not a valid selection. Your adventure has ended. ")

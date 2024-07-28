command = ""
started = False
while True:
     command = input("=> ").lower()
     if command == "start":
         if started:
             print("Car is already started!")
         else:
             started = True
             print("Car started...")
     elif command == "stop":
         if not started:
             print("Car is already stopped!")
         else:
             started = False
             print("Car stopped...")


     elif command == "help":
         print("start - to start car")
         print("stop - to stop car")
         print("Quit - to exit")
     elif command == "quit":
         print("Exit")
         break
     else:
         print(" Sorry, I dont understand! ")






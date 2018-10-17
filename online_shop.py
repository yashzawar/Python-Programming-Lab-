from easygui import *
import sys



while 1:
    msgbox("E-BAZAR")

    msg ="What is your favorite shopping site?"
    title = "online shopping"
    choices = ["Flipcart", "Amazon", "Myntra"]
    choice = choicebox(msg, title, choices)
   
    if choices=="Flipcart":
          choices1 = ["Jeans","Shirts","T-Shirts"]
          choices = choicebox(msg, choices1)
   

           if choices1=="Jeans":
                  choices2 = ["Buffalo","Allen Solly","Lee Cooper"]
                  choices1 = choicebox(msg, choices2) 
 

 

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")
 

 
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)



// Yash Zawar
// M-67
// Project on data representation 

from easygui import *
import sys
while 1:
    msgbox("Welcome to Data Representation Program")

    msg ="Data Representation"
    title = "Data Representation Types"
    choices = ["Pie","Line Graph","Histogram","Bar Graph"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Pie":     # show a Continue/Cancel dialog
        pass# user chose Continue
        import numpy as np
        import matplotlib as plt
        import matplotlib.pyplot as plt
        %matplotlib inline
        labels='Red','Green','Yellow','Blue'
        x=int(input("Enter a value"))
        y=int(input("Enter a value"))
        z=int(input("Enter a value"))
        w=int(input("Enter a value"))
        sizes=[x,y,z,w]
        colours=['Red','Green','Yellow','Blue']
        plt.pie(sizes,labels=labels)
        plt.axis('equal')
        plt.show()
        sys.exit(0)
    elif choice=="Line Graph":
        import matplotlib.pyplot as plt
        x = [1,2,3]
        y = [5,7,4]

        x2 = [1,2,3]
        y2 = [10,14,12]

        plt.plot(x,y,label='First Line')
        plt.plot(x2,y2,label='Second Line')
        plt.xlabel('Plot Number')
        plt.ylabel('Important Var')
        plt.title('Interesting Graph\nCheck it out')
        plt.legend()
        plt.show()
        sys.exit(0)
    elif choice=="Histogram":
        import numpy as np
        import matplotlib.pyplot as plt
        data = [1,11,21,31,41]

        y1=int(input("Enter a value"))
        y2=int(input("Enter a value"))
        y3=int(input("Enter a value"))
        y4=int(input("Enter a value"))
        y5=int(input("Enter a value"))
        y6=int(input("Enter a value"))
        plt.hist([1,11,21,31,41, 51], bins=[0,10,20,30,40,50,60], weights=[y1,y2,y3,y4,y5,y6], edgecolor="red") 
        plt.show()
        sys.exit(0)
    elif choice=="Bar Graph":
        import matplotlib.pyplot as plt; plt.rcdefaults()
        import numpy as np
        import matplotlib.pyplot as plt
        y1=int(input("Enter a value"))
        y2=int(input("Enter a value"))
        y3=int(input("Enter a value"))
        y4=int(input("Enter a value"))
        y5=int(input("Enter a value"))
        y6=int(input("Enter a value")) 
        objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        y_pos = np.arange(len(objects))
        performance = [y1,y2,y3,y4,y5,y6]
 
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Usage')
        plt.title('Programming language usage')
 
        plt.show()
        sys.exit(0)

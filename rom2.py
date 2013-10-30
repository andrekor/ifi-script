import commands
import sys
import getpass
import os
import re
import mail 

rom = {3408: "Algol", 3417: "Assembler", 3418: "Limbo", 2428: "Lisp", 3302: "FUI", 3453: "Eiffel/Jenterommet", 3468: "Fortress", 3467: "Fortran", 3458: "Euclid (Design)", 2443: "Modula", 5419: "Lab, 5-etasje", 5418: "master termstuen i 5. etasje", 3452: "Cobol", 3407: "Ada (Sonen)", 3443: "Chill", 3427: "Bliss", 3303: "Foreningskontoret", 5301: "master termstue2, 5. etasje", 2453: "Pascal", 2269: "Python", 2465: "Prolog", 2458: "Postscript", 2453: "Perl", 2438: "Logo", 2423: "Java", 3403: "Foreningskontoret", 1678: "ifi-server", 8470: "Master termstue i 8. etasje", }

maskin = []
person = []
tid = []

def who():
    global maskin, person, tid
    if (len(sys.argv) >= 2):
        pers = sys.argv[1]
        a = "rwho | grep " + pers
        b = commands.getstatusoutput(a)
        lala = b[1].split("\n")
        if (len(b[1].split(" ")) > 1):
            for i in range(0, len(lala)):
#                person = b[1].split(" ")[0]

#                maskin = re.split("\s+", b[1])[1].split(".")[0]
                m = re.split("\s+", lala[i])[1].split(".")[0]
                if any(m in b for b in maskin) == 0:
                    person.append(lala[i].split(" ")[0])
                    maskin.append(m)
       #         maskin.append(re.split("\s+", lala[i])[1].split(".")[0])
#                tid = re.split("\s+", b[1])[3] +" "+  re.split("\s+", b[1])[2] +", kl: "+ re.split("\s+", b[1])[4] 
                    tid.append(re.split("\s+", lala[i])[3] +" "+ re.split("\s+", lala[i])[2] + ", kl: " + re.split("\s+", lala[i])[4])
           
            #print "Logget paa: ", tid[i]
            #print person[0] + " sitter paa " + maskin[i]
            return True
        else:
            #print person, "er ikke logget paa noen maskin for oyeblikket, eller brukernavn er skrevet feil. Les om " + person + "(y/n)"
#answer = raw_input(": ")            
            answer = raw_input("Vil du sende han en mail(y/n): ")
            
            if  answer == "y":
                #              print commands.getstatusoutput("ustat " + person)[1]
                mail.mail()
            return None
        
def funk(ma):
    
    a = "/snacks/bin/hvor" + " " + ma
    b = commands.getstatusoutput(a)
    if (len(b) > 0):
        listen = b[1].split(",")
        if (len(listen) > 3):
            romnr = listen[len(listen)-2]
        else:
            romnr = listen[len(listen)-1]
        if (len(b[1]) > 2): 
            try:
                rom[int(romnr)] #Stygg maate aa gjore det paa
                print romnr + ":", rom[int(romnr)]
                return True
            except KeyError:
                print "maskinen " + ma + " er paa rom " + romnr + " som for oyeblikket ikke er lagt til i systemet"
        else:
            print "No computer named <", sys.argv[1], "> found"
            return False
        

def writeFile():
    f = open("/uio/hume/student-u52/andrekor/Bashscript/list.txt", "a+r");
    a = f.readlines()
    if any(getpass.getuser() in b for b in a) == 0:
        f.write('%s\n' % getpass.getuser())
    f.close()

        
if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        if (who()):
            for i in range(0, len(tid)):
                print "Logget paa: ", tid[i]
                print person[i] + " sitter paa " + maskin[i]
                funk(maskin[i])
                print                 
            writeFile()
    else:
        print "Usage:",sys.argv[0], " <person-uname>"
        

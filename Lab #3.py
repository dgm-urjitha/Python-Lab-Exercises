#!/usr/bin/env python3

#Lab-3 Lakshmi Urjitha Dhadigam

FILENAME ="groceries.html"

def main() :
    with open(FILENAME) as file :
        for line in file :
            line = line.replace("<h1>" , "")
            line = line.replace("</h1>", "")
            line = line.replace("\n", "")
            line = line.replace("<ul>", "")
            line = line.replace("</ul>", "")
            line = line.replace("<li>", " * ")
            line = line.replace("</li>", " ")
            print (line)
           
if __name__=='__main__' :
    main()  

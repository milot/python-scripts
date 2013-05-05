#!/usr/bin/python

# Gentoo emerge status               
# This script requires genlop,       
# you can install it using `emerge genlop`.
# Copyleft (c) 2005 - Milot Shala <milot.shala@gmail.com>
# http://forums.gentoo.org/viewtopic-p-2970419-highlight-.html#2970419

import sys
import os
import time

#colors
color={}
color["r"]="\x1b[31;01m"
color["g"]="\x1b[32;01m"
color["b"]="\x1b[34;01m"
color["0"]="\x1b[0m"


def r(txt):
   return color["r"]+txt+color["0"]
def g(txt):
   return color["g"]+txt+color["0"]
def b(txt):
   return color["b"]+txt+color["0"]

# View Options
def view_opt():   
         
   print
   print
   print g("full-info - View full information for emerged package")
   print g("cur - View current emerge")
   print g("hist - View history of emerged packages by day")
   print g("hist-all - View full list of history of emerged packages")
   print g("rsync - View rsync history")
   print g("time - View time for compiling a package")
   print g("time-unmerged - View time of unmerged packages")
   print
   command = raw_input(r("Press Enter to return to main "))
   if command == '':
      c()
      program()
   else:
      c()
      program()

# system command 'clear'
def c():
   os.system('clear')


# Base program
def program():
   c()
   print g("Gentoo emerge status script")
   print ("---------------------------")
   print

   print ("1]") + g(" Enter options")
   print ("2]") + g(" View options")
   print ("3]") + g(" Exit")
   print
   command = input("[]> ")


   if command == 1:   
      print
      print r("""First of all  you must view options to know what to use, you can enter option name ( if you know any ) or type `view-opt` to view options.""")
      print
      time.sleep(2)
      command = raw_input(b("Option name: "))
      if (command == 'view-opt' or command == 'VIEW-OPT'):
         view_opt()


      elif command == 'full-info':
         c()
         print g("Full information for a single package")
         print ("-------------------------------------")
         print
         print b("Enter package name")
         command=raw_input("> ")
         c()
         print g("Full information for package"), b(command)
         print ("-----------------------------------")
         print
         pack=['genlop -i '+command]
         pack_=" ".join(pack)
         os.system(pack_)
         print
         print r("Press Enter to return to main.")
         command=raw_input()
         if command == '':
            c()
            program()

         else:
            c()
            program()


      elif command == 'cur':
         if command == 'cur':
            c()
            print g("Current emerge session(s)")
            print ("-------------------------")
            print
            print b("Listing current emerge session(s)")
            print
            time.sleep(1)
            os.system('genlop -c')
            print
            print r("Press Enter to return to main.")
            command = raw_input()
            if (command == ''):
               c()
               program()

            else:
               c()
               program()

            
      elif command == 'hist':
         if command == 'hist':
            c()
            print g("History of merged packages")
            print ("---------------------------")
            print
            time.sleep(1)
            print b("Enter number of how many days ago you want to see the packages")
            command = raw_input("> ")
            c()
            print g("Packages merged "+b(command)+ g(" day(s) before"))
            print ("------------------------------------")
            pkg=['genlop --list --date '+command+' days ago']
            pkg_=" ".join(pkg)
            os.system(pkg_)
            print
            print r("Press Enter to return to main.")
            command = raw_input()
            if command == '':
               c()
               program()

            else:
               c()
               program()


      elif command == 'hist-all':
            c()
            print g("Full history of merged individual packages")
            print ("--------------------------------------")
            print
            print b("Do you want to view individual package?")
            print r("YES/NO?")
            command = raw_input("> ")
            print
            if (command == 'yes' or command == 'YES'):
               print g("Enter package name")
               command = raw_input("> ")
               print
               pkg=['genlop -l | grep '+command+ ' | less']
               pkg_=" ".join(pkg)
               os.system(pkg_)
               print
               print r("Press Enter to return to main")
               command = raw_input()
               if command == '':
                  c()
                  program()
               else:
                  c()
                  program()
            
            elif (command == 'no' or command == 'NO'):
               pkg=['genlop -l | less']
               pkg_=" ".join(pkg)
               os.system(pkg_)
               print
               print r("Press Enter to return to main")
               command = raw_input()
               if command == '':
                  c()
                  program()
      
               else:
                  c()
                  program()

            else:
               c()
               program()
      

      elif command == 'rsync':
         print g("RSYNC updates")
         print
         print
         print
         print b("You can view rsynced time by year!")
         print r("Do you want this script to do it for you? (yes/no)")
         command = raw_input("> ")
         if (command == 'yes' or command == 'YES'):
            print
            print g("Enter year i.e"), b("2005")
            print
            command = raw_input("> ")
            rsync=['genlop -r | grep '+command+' | less']
            rsync_=" ".join(rsync)
            os.system(rsync_)
            print
            print r("Press Enter to return to main.")
            c()
            program()
         elif (command == 'no' or command == 'NO'):
            os.system('genlop -r | less')
            print
            print r("Press Enter to return to main.")
            command = raw_input()
            if command == '':
               c()
               program()
      
            else:
               c()
               program()
            
      elif command == 'time':
         c()
         print g("Time of package compilation")
         print ("---------------------------")
         print
         print

         print b("Enter package name")
         pkg_name = raw_input("> ")
         pkg=['emerge '+pkg_name+' -p | genlop -p | less']
         pkg_=" ".join(pkg)
         os.system(pkg_)
         print
         print r("Press Enter to return to main")
         time.sleep(2)
         command = raw_input()
         if command == '':
            c()
            program()
      
         else:
            c()
            program()


      elif command == 'time-unmerged':
         c()
         print g("Show when package(s) is/when is unmerged")
         print ("----------------------------------------")
         print
         
         print b("Enter package name: ")
         name = raw_input("> ")
         pkg=['genlop -u '+name]
         pkg_=" ".join(pkg)
         os.system(pkg_)
         print
         print r("Press Enter to return to main")
         time.sleep(2)
         command = raw_input()
         if command == '':
            c()
            program()
         
         else:
            c()
            program()

      else:
         print
         print r("Wrong Selection!")
         time.sleep(2)
         c()
         program()
         

   elif command == 2:
      view_opt()
      command = raw_input(r("Press Enter to return to main "))
      if command == '':
         c()
         program()
      else:
         c()
         program()


   elif command == 3:
      print
      print b("Thank you for using this script")
      print
      time.sleep(1)
      sys.exit()

   else:
      print
      print r("Wrong Selection!")
      time.sleep(2)
      c()
      program()
      command = ("")
   

program() 


"""- Implement a class called Player that represents a cricket player.
The palyer class shold have a method called play() which prints "The palyer is playing cricket".
Derive two classes, Batsman and bowler, from the Player class.
Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively.
Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object."""


#define the base class player
class player:
  def play (self):
    print("The player is playing cricket.")

#define the derived class batsman
class batsman (player):
  def play (self):
    print("The batsman is sitting.")

#define the derived class bowler
class bowler (player):
  def play (self):
    print("The bowler is bowling.")

#create objects of batsman and bowler class 
batsman = batsman()
bowler = bowler()

# call the paly () mathod for each object 
batsman.play()
bowler.play()


#strings in python

#we can declare them in double or single quotes both just use them as your req
fname="Proni";
sname="Bho";
full=fname+sname;
print(full);     #string concatenation
print(fname[0]);   #string ko v index se access kar sakte hai

#what if i want double quoutes 
sent1="He said,\"I am Proni\".";     #use '\' 
sent2='He said,"I am Proni".';       #use single quotes

#what if i want to print a whole paragraph
commentary=''' 41.4
Gerald Coetzee to Cummins, no run
41.3
Gerald Coetzee to Cummins, no run, length delivery on off-stump, Cummins hangs back and drops it into the off-side
41.2
Gerald Coetzee to Cummins, FOUR, boundary for Cummins! Oh how crucial these runs are! Pitched up full just outside off, Cummins pressed forward and just opened the face of the blade to steer the drive behind square on the off-side, got it right into the gap between deep point and third man
Gerald Coetzee is bowling his 7th over on the trot here and it just looks like he's gone down with a bit of cramp. The physio is out there to attend to him
41.1
Gerald Coetzee to Cummins, no run, banged in short on off-stump, Cummins gets his hands up looking to defend and it keeps climbing, hits him high on the bat and pops up, would've landed in silly point's pocket had he been there
Have you got any fingernails left? I do because I've been typing all of this but I wouldn't have if I'd just been watching'''


#we can use triple single quotes or triple (double quotes)

print(sent1);
print(sent2);
print(commentary);


#for loop to print a string similiar as c++ for vector

for ch in fname :
    print(ch);               #this will print fname same as for(int i : fname){ cout<<i<<" ";}
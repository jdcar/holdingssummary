import re

fhand = open("H:\\MFHD\MFHDS.txt")

for line in fhand:

    if re.compile("23\$81\$a\(no\.\),"):

        mfhd = line.split(", ")[0]

        p = re.compile("23\$81\$a\(no\.\),")
        matchResult = p.search(line)

        if "23$81$a(no.)," in str(matchResult):

            p2 = re.compile("4.\$8.*")
            matchResult2 = p2.search(line)

            m = str(matchResult2)

            m2 = m.split("$a")[-1].split("'>")[0]

            holdings1 = m2

            holdings = str(holdings1)

            if re.search('[a-zA-Z>]+', holdings):

                print ("Nope| ", mfhd, "|no.", m2, sep="")                    

            else:

                print ("Done| ", mfhd, "|no.", m2, sep="")


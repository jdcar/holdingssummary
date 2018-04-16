import re

fhand = open("H:\\MFHD\MFHDS_from_carli\\textfileprogram\\testgroup10000.txt")

for line in fhand:

    if re.compile("23\$81\$a\(unit\),"):

        mfhd = line.split(", ")[0]

        p = re.compile("23\$81\$a\(unit\),")
        matchResult = p.search(line)

        if "23$81$a(unit)," in str(matchResult):

            p2 = re.compile("4.\$8.*")
            matchResult2 = p2.search(line)

            m = str(matchResult2)

            m2 = m.split("$a")[-1].split("'>")[0]

            holdings1 = m2

            holdings = str(holdings1)

            print ("Nope|", mfhd, "|", m2, sep="")

import re


fhand = open("H:\\MFHD\MFHDS.txt")

for line in fhand:

    if re.compile("23\$81\$a\(yr\.\)\$bno\.,"):

        mfhd = line.split(", ")[0]

        p = re.compile("23\$81\$a\(yr\.\)\$bno\.,")
        matchResult =  p.search(line)

        if "23$81$a(yr.)$bno." in str(matchResult):

            p2 = re.compile("4.\$8.*")
            matchResult2 = p2.search(line)

            m = str(matchResult2)

            m2 = m.split("$a")[-1].split("$b")[0]
            m3 = m.split("$b")[-1].split("'>")[0]

            if re.search("18\\d\\d/\\d\\d-18\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1].split("/")[0]
                fourthYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "/18" , secondYear, "-" , thirdYear, "/18" , fourthYear)))

            elif re.search("18\\d\\d/\\d\\d-19\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1].split("/")[0]
                fourthYear = m2.split("/")[-1]
                
                m2 = "".join(map(str,(firstYear, "/18" , secondYear, "-" , thirdYear, "/19" , fourthYear)))

            elif re.search("19\\d\\d/\\d\\d-19\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1].split("/")[0]
                fourthYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "/19" , secondYear, "-" , thirdYear, "/19" , fourthYear)))

            elif re.search("20\\d\\d/\\d\\d-20\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1].split("/")[0]
                fourthYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "/20" , secondYear, "-" , thirdYear, "/20" , fourthYear)))

            elif re.search("19\\d\\d/\\d\\d-20\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1].split("/")[0]
                fourthYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "/19" , secondYear, "-" , thirdYear, "/20" , fourthYear)))
                
            elif re.search("18\\d\\d-18\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[1].split("/")[0]
                thirdYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "-", secondYear, "/18" , thirdYear)))

            elif re.search("18\\d\\d-19\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[1].split("/")[0]
                thirdYear = m2.split("/")[-1]
                
                m2 = "".join(map(str,(firstYear, "-" , secondYear, "/19" , thirdYear)))

            elif re.search("19\\d\\d-19\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[1].split("/")[0]
                thirdYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "-" , secondYear, "/19" , thirdYear)))

            elif re.search("20\\d\\d-20\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[1].split("/")[0]
                thirdYear = m2.split("/")[-1]
                
                m2 = "".join(map(str,(firstYear, "-" , secondYear, "/20" , thirdYear)))

            elif re.search("19\\d\\d-20\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[1].split("/")[0]
                thirdYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "-" , secondYear, "/20" , thirdYear)))

            elif re.search("18\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "/18" , secondYear)))

            elif re.search("19\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[-1]

                m2 = "".join(map(str,(firstYear, "/19" ,secondYear)))

            elif re.search("20\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[-1]
                
                m2 = "".join(map(str,(firstYear, "/20" , secondYear)))

            elif re.search("18\\d\\d/18\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/", secondYear, "-18" , thirdYear)))

            elif re.search("18\\d\\d/19\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[-1]
                
                m2 = "".join(map(str,(firstYear, "-19" , secondYear)))

            elif re.search("19\\d\\d/19\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "-19" , secondYear)))

            elif re.search("19\\d\\d/20\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[-1]
                
                m2 = "".join(map(str,(firstYear, "-20" , secondYear)))
                
            elif re.search("20\\d\\d-20\\d\\d/\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "-20" , secondYear)))

            elif re.search("18\\d\\d/\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/18", secondYear, "-18" , thirdYear)))

            elif re.search("19\\d\\d/\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/19" , secondYear, "-19" , thirdYear)))

                
            elif re.search("20\\d\\d/\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/20" , secondYear, "-20" , thirdYear)))
                   
            elif re.search("18\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "-18" , secondYear)))
                    
            elif re.search("19\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "-19" ,secondYear)))
                    
            elif re.search("20\\d\\d-\\d\\d$", m2):

                firstYear = m2.split("-")[0]
                secondYear = m2.split("-")[-1]
                
                m2 = "".join(map(str,(firstYear, "-20" , secondYear)))

            elif re.search("18\\d\\d/\\d\\d-18\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/18" , secondYear, "-" , thirdYear)))

            elif re.search("18\\d\\d/\\d\\d-19\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/18" , secondYear, "-" , thirdYear)))
                
            elif re.search("19\\d\\d/\\d\\d-19\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/19" , secondYear, "-" , thirdYear)))

            elif re.search("19\\d\\d/\\d\\d-20\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/19" , secondYear, "-" , thirdYear)))

            elif re.search("20\\d\\d/\\d\\d-20\\d\\d$", m2):

                firstYear = m2.split("/")[0]
                secondYear = m2.split("/")[1].split("-")[0]
                thirdYear = m2.split("-")[-1]

                m2 = "".join(map(str,(firstYear, "/20" , secondYear, "-" , thirdYear)))

            else:
                
                m2 = m2                      

            holdings1 = m2, m3

            holdings = str(holdings1)

            hyphenCount = holdings.count("-")
                
            if re.search('[a-zA-Z>]+', holdings):

                print ("Nope|", mfhd, "|",  m2, ":no.", m3, sep="")

            elif ("-" not in holdings):

                print ("Done|" ,mfhd, "|", m2, ":no.", m3, sep="")

            elif hyphenCount == 2:

                firstDate = m2.split("-",1)[0]
                secondDate = m2.split("-")[-1]
                firstIssue = m3.split("-",1)[0]
                secondIssue = m3.split("-",1)[-1]

                print ("Done|", mfhd, "|", firstDate, ":no.", firstIssue, "-", secondDate, ":no.", secondIssue, sep="")

            else:

                print ("Done|", mfhd, "|" , m2, ":no.", m3, sep="")

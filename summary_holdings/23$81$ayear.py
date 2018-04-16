import re


fhand = open("H:\\MFHD\MFHDS.txt")

for line in fhand:


    if "$ayear" in line:

        if re.compile("23\$81\$ayear,"):

            mfhd = line.split(", ")[0]

            p = re.compile("23\$81\$ayear,")
            matchResult =  p.search(line)

            if "23$81$ayear," in str(matchResult):

                p2 = re.compile("4.\$8.*")
                matchResult2 = p2.search(line)

                m = str(matchResult2)

                m2 = m.split("$a")[-1].split("'>")[0]
        
                if re.search('[a-zA-Z>]+', m2):

                    print ("Nope| " , mfhd, "|" ,  m2, sep="")


                elif re.search("18\\d\\d/\\d\\d-18\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1].split("/")[0]
                    fourthYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/18" , secondYear, "-" , thirdYear, "/18" , fourthYear, sep="")


                elif re.search("18\\d\\d/\\d\\d-19\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1].split("/")[0]
                    fourthYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/18" , secondYear, "-" , thirdYear, "/19" , fourthYear, sep="")

                elif re.search("19\\d\\d/\\d\\d-19\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1].split("/")[0]
                    fourthYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/19" , secondYear, "-" , thirdYear, "/19" , fourthYear, sep="")

                elif re.search("20\\d\\d/\\d\\d-20\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1].split("/")[0]
                    fourthYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/20" , secondYear, "-" , thirdYear, "/20" , fourthYear, sep="")

                elif re.search("19\\d\\d/\\d\\d-20\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1].split("/")[0]
                    fourthYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/19" , secondYear, "-" , thirdYear, "/20" , fourthYear, sep="")

                elif re.search("18\\d\\d-18\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[1].split("/")[0]
                    thirdYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "-", secondYear, "/18" , thirdYear, sep="")

                elif re.search("18\\d\\d-19\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[1].split("/")[0]
                    thirdYear = m2.split("/")[-1]
                    
                    print ("Done| " , mfhd, "|" ,firstYear, "-" , secondYear, "/19" , thirdYear,  sep="")


                elif re.search("19\\d\\d-19\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[1].split("/")[0]
                    thirdYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "-" , secondYear, "/19" , thirdYear,  sep="")


                elif re.search("20\\d\\d-20\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[1].split("/")[0]
                    thirdYear = m2.split("/")[-1]
                    
                    print ("Done| " , mfhd, "|" ,firstYear, "-" , secondYear, "/20" , thirdYear, sep="")


                elif re.search("19\\d\\d-20\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[1].split("/")[0]
                    thirdYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "-" , secondYear, "/20" , thirdYear, sep="")

                elif re.search("18\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/18" , secondYear,  sep="")

                elif re.search("19\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/19" ,secondYear,   sep="")

                elif re.search("20\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[-1]
                    
                    print ("Done| " , mfhd, "|" ,firstYear, "/20" , secondYear , sep="")

                    ##

                elif re.search("18\\d\\d/18\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]

                    print ("xDone, " , mfhd, ", " ,firstYear, "-18", secondYear, sep="")


                elif re.search("18\\d\\d/19\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]
                    
                    print ("Done| " , mfhd, "|" ,firstYear, "-19" , secondYear, sep="")


                elif re.search("19\\d\\d/19\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "-19" , secondYear, sep="")


                elif re.search("19\\d\\d/20\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]
                    
                    print ("Done| " , mfhd, "|" ,firstYear, "-20" , secondYear, sep="")
                    
                elif re.search("20\\d\\d-20\\d\\d/\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "-20" , secondYear, sep="")
                                
                elif re.search("18\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "-18" , secondYear,  sep="")

                elif re.search("19\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "-19" ,secondYear,   sep="")

                elif re.search("20\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("-")[0]
                    secondYear = m2.split("-")[-1]
                    
                    print ("Done| " , mfhd, "|" ,firstYear, "-20" , secondYear , sep="")

                elif re.search("18\\d\\d/\\d\\d-18\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" , firstYear, "/18" , secondYear, "-" , thirdYear, sep="")

                elif re.search("18\\d\\d/\\d\\d-19\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" , firstYear, "/18" , secondYear, "-" , thirdYear, sep="")
                    
                elif re.search("19\\d\\d/\\d\\d-19\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/19" , secondYear, "-" , thirdYear, sep="")


                elif re.search("19\\d\\d/\\d\\d-20\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/19" , secondYear, "-" , thirdYear, sep="")

                elif re.search("20\\d\\d/\\d\\d-20\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/20" , secondYear, "-" , thirdYear, sep="")

                elif re.search("18\\d\\d/\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/18", secondYear, "-18" , thirdYear, sep="")

                elif re.search("19\\d\\d/\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" , firstYear, "/19" , secondYear, "-19" , thirdYear, sep="")

                elif re.search("20\\d\\d/\\d\\d-\\d\\d$", m2):

                    firstYear = m2.split("/")[0]
                    secondYear = m2.split("/")[1].split("-")[0]
                    thirdYear = m2.split("-")[-1]

                    print ("Done| " , mfhd, "|" ,firstYear, "/20" , secondYear, "-20" , thirdYear, sep="")

                else:
                    
                    print ("Done| " , mfhd, "|" , m2, sep="")       

def arithmetic_arranger(numList, solution=False):

    firstList = []
    secondList = []
    thirdList = []
    ansList = []

    if len(numList) > 5:
        return "Error: Too many problems."
    else:
        for each in numList:
            eachNum = each.split(" ")
            #print("equation", eachNum)
            firstNum = eachNum[0]
            secondNum = eachNum[2]
            operator = eachNum[1]
            #print("operator", operators)

            #Checking in operator are integer
            if firstNum.isdigit() == False:
                return "Error: Numbers must only contain digits."
                quit()
            elif secondNum.isdigit() == False:
                return "Error: Numbers must only contain digits."
                quit()
            elif operator == "/" and "*":
                return "Error: Operator must be '+' or '-'."
                quit()

            numLength = 0

            if len(firstNum) + 2 >= len(secondNum) + 2:
                numLength = len(firstNum) + 2
            elif len(firstNum) + 2 <= len(secondNum) + 2:
                numLength = len(secondNum) + 2

            if numLength > 6:
                return "Error: Numbers cannot be more than four digits."
                quit()

            # For firstLine

            spaceFirstnum = []

            for numSpacing in range(numLength - (len(firstNum) + 2)):
                spaceFirstnum.append(" ")

            # for firstList
            firstList.extend(["  "])
            firstList.extend(spaceFirstnum)
            firstList.extend([firstNum, "    "])

            # for secondLine
            spaceSecondnum = []

            for numSpacing in range(numLength - (len(secondNum) + 2)):
                spaceSecondnum.append(" ")

            # for second list
            secondList.extend([operator, " "])
            secondList.extend(spaceSecondnum)
            secondList.extend([secondNum, "    "])

            # for thirdline
            for numSpacing in range(numLength):
                thirdList.append("-")

            thirdList.extend(["    "])

            # for forthline(Ans)
            if solution == True:
                if operator == "+":
                    answer = int(firstNum) + int(secondNum)

                elif operator == "-":
                    answer = int(firstNum) - int(secondNum)

                spaceAnsnum = []
                for numSpacing in range(numLength - len(str(answer))):
                    spaceAnsnum.append(" ")

                ansList.extend(spaceAnsnum)
                ansList.extend([str(answer)])

                ansList.extend(["    "])

            firstString = "".join(firstList).rstrip(" ")
            secondString = "".join(secondList).rstrip(" ")
            thirdString = "".join(thirdList).rstrip(" ")
            ansString = "".join(ansList).rstrip(" ")

    if solution == True:
        # Final output
        return_product = firstString + "\n" + secondString + "\n" + thirdString + "\n" + ansString
        return return_product

    else:
        return_product = firstString + "\n" + secondString + "\n" + thirdString
        return return_product

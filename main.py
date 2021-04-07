import math

def poodle():
	#not too bad imo the code is harder to write for this one than the actual question
  a=math.factorial(5)+4*0.5*math.factorial(5)
  return int(a)

def identicalCoins(coins,chests):
	#stars n bars are not that fun
	a = math.comb(coins-1,chests-1)
	return a

def colouredBlocks(number):
	#very annoying
	a = 2 ** number - 1
	return a

def encyclopedia(number):
	#factorials came in clutch here
	a = math.factorial(number)-2
	return a

def conference(coworkers,workers):
	#i didn't know there was a combinatorics function until stackoverflow
	a = 2*math.comb(workers-2,coworkers-1)+math.comb(workers-2,coworkers)
	return a

def examWriting(exams,examSlots):
	#more factorials
	a = math.comb(examSlots,exams)
	return a

def pizzaToppings(mushrooms,pineapple,both):
	#pineapple with bacon, mushrooms with tomatos are both elite picks on pizza
	a = 1-(mushrooms+pineapple-both)/100
	return round(a,2)

def localLottery(thirdPrizes):
	#this was on one of the tests
	a = ((50000 + 5000 + thirdPrizes*100)/100000)
	return "$" + str(round(a,2))

def tablets(new,used):
	#more combinatorics but i think we did this on a test so i just looked through there
	a = math.comb(new,3) * math.comb(used,2) / math.comb(new+used,5)
	return round(a,3)

def fungoid():
	#where do these weird words come from, also x10 because it seems highly improbably that a 7 letter word would have that low of a chance
	a = (math.factorial(3) * math.factorial(3)) / math.factorial(8) * 10
	return round(a,6)

def manuLines(line1, line2, defect1, defect2):
	#ah, the classic manufacturing lines.
	a = line1 * (100-defect1)/10000
	return round(a,3)

#onto the super tricky questions

def bankLoans(percent, number):
	n = 200
	p = round(percent/100,2)
	q = 1 - p
	m = n*p
	s = math.sqrt(n*p*q)
	number-=0.5
	#this part was actually tricky trying to find something that calculated the distribution
	probability = math.erf((number-m) / (s*math.sqrt(2)))
	#plus 0.5 because the question said so
	percentUpper = 1 - (probability/2 + 0.5)
	return round(percentUpper,4)

def bloodPressure(bottom,top):
	#really weird i thought it would be chemistry but it is a-okay took a while to conver the formula into python though
	thing1 = 130
	thing2 = 140
	#sigma
	sig = math.sqrt(top)
	#calculating the lower part's probabiltiy
	probabilityL = math.erf((thing1 - bottom)/ (sig*math.sqrt(2)))
	probabilityLower = probabilityL / 2
	#calculating the higher part's probability
	probabilityU = math.erf((thing2 - bottom) / (sig*math.sqrt(2)))
	probabilityUpper = probabilityU / 2
	#mishmashing them together
	totalProbability = probabilityUpper - probabilityLower
	return round(totalProbability,3)

def tallGirl(height, mu, sigma):
	probability = math.erf((height - mu) / (sigma*math.sqrt(2)))
	#plus 0.5 again
	probabilityTaller = 1 - (probability / 2+0.5)
	return round(probabilityTaller,3)

def quizShow(mu, sigma, year):
	probability = math.erf((year - mu) / (sigma*math.sqrt(2)))
	#plus 0.5 again
	probabilityUpper = probability/2+0.5
	return round(probabilityUpper,3)

def stickItAllTogether():
    array = []
    array.append(poodle())
    array.append(identicalCoins(20,7))
    array.append(colouredBlocks(9))
    array.append(encyclopedia(9))
    array.append(conference(4,11))
    array.append(examWriting(6,18))
    array.append(pizzaToppings(59,28,14))
    array.append(localLottery(15))
    array.append(tablets(8,2))
    array.append(fungoid())
    array.append(manuLines(50,50,6,4))
    array.append(bankLoans(21,58))
    array.append(bloodPressure(110,399))
    array.append(tallGirl(168,178,8))
    array.append(quizShow(38.3,12.71,32))
    print(array)
stickItAllTogether()

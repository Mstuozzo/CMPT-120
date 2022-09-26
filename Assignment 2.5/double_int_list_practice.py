def main():
  
  #set this to any double
  doubleValue = 0.5
  
  #set this to any int
  intValue = 2
  
  #print out addition, subtraction, multiplication, and division of these two values
  
  print(doubleValue % intValue)
  print(doubleValue * intValue)
  print(doubleValue + intValue)
  print(doubleValue - intValue)

  #populate this list
  myFriends = ["Ryan", "matthew", "sophie", "andrew"]
  
  print(myFriends[2])
  print(myFriends[3])
  #print out your friends at index 2 and index 3
  
  
  #populate this list with five numbers
  fiveNumbers = [25, 50, 17, 4, 61]

  print(fiveNumbers[0] % fiveNumbers[1])
  print(fiveNumbers[2] * fiveNumbers[3])
  print(fiveNumbers[4] + fiveNumbers[3])
  print(fiveNumbers[2] - fiveNumbers[0])

  #do each of the four equations with different numbers each time.
  
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)

  fiveNumbers[2] = 6
  fiveNumbers[3] = 12

  #print out the list

  print(fiveNumbers)
  
  
main()

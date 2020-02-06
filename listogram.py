from dictogram import histogram

def get_index(word, listogram):

#loop through each item in the input listogram
  result = 0
  for inner_list in listogram:
    if inner_list[0] == word:
      return result
    else:
      result += 1
  return "nope didn't find it"

def listogram(lines):
    listogram = []
    
#loop through each word in lines
    
    for word in lines:
      word = word.rstrip()
      #search for the word
    
      result = get_index(word, listogram)
      if result == "nope didn't find it":
        listogram.append([word,1])
      else:
        listogram[result][1] += 1
    
    #call get_index() and save the result to a variable
    
    #if the result is the non valid index value then
    #we know the word was not found and this is the first time we have seen the word
    #in this case we will append a new inner list with the word and a count of 1
    #otherwise we have seen the word before and we need to use the result which will
    #be the index of the inner list to update the count by 1 in that inner list
    
    #return the listogram
    return listogram
    
lines = open("frost.txt", "r").readlines()
print(listogram(lines))
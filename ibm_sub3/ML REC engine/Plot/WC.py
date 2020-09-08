import string
def main():
  print("This program calculates the number of words in a sentence")
  print()
  p = input("Enter a sentence: ")
  words = string.split(p)
  wordCount = len(words)
  print("The total word count is:", wordCount)
main()

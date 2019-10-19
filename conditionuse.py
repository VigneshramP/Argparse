import argparse
def ArgParser():
  parser=argparse.ArgumentParser(description = "Replacing Character in Sting")
  parser.add_argument("-f","--file",help = "File pathand used to Start with -f")
  parser.add_argument("-s","--Character",help="Format EXAMPLE:a-b-c-d and used to Start with -s")
  parser.add_argument("-c","--Choice",type = int,help="Enter your Choice 1.Count 2.Replace Character and use -c " )
  args=parser.parse_args()
  return args
def fileOpen(file):
  f=open(file,"r")
  fileOpen= f.read()
  return fileOpen
def replace_vowels(File,dictionary):
  LowerConversion = File.lower()
  for oldCharacter,newCharacter in dictionary.items():
    LowerConversion = LowerConversion.replace(oldCharacter,newCharacter)
  print LowerConversion
def count_of_character(File,dictionary):
  list_of_replaceCharacter = dictionary.keys()
  for characterCount in list_of_replaceCharacter:
    print "The Count of {} is :".format(characterCount),File.count(characterCount)
def main():
  Args= ArgParser()
  fileContant=fileOpen(Args.file)
  Replace=Args.Character.split("-")
  dictConversion = {Replace[i]: Replace[i + 1] for i in range(0, len(Replace),2)}
  if (Args.Choice==1):
    Count_of_character = count_of_character(fileContant,dictConversion)
  elif (Args.Choice==2):
    LowerConversion=replace_vowels(fileContant,dictConversion)
  else:
    print "Enter the Correct Choice"
    print "Enter the Correct File path and used to Start with -f"
    print "Enter the Correct Format EXAMPLE:a-b-c-d and used to Start with -s"
    print "1.Count"
    print "2.Replace Character"
if __name__ == '__main__':
  main()
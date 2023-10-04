#!/usr/bin/env python3

class MyString:
  
  def __init__(self):
      self.value = ""

  def get_value(self):
    return self.value
  
  def set_value(self, value):
    if(isinstance(value, str)):
        self.value = value
    else: print("The value must be a string.\n")

  def is_sentence(self):
     if(list(self.value)[-1] == '.'): return True
     else: return False

  def is_question(self):
     if(list(self.value)[-1] == '?'): return True
     else: return False

  def is_exclamation(self):
     if(list(self.value)[-1] == '!'): return True
     else: return False

  def count_sentences(self):
    count = 0
    for letter in list(self.value):
      if letter == '!' or letter == '?' or letter == '.': count+=1
    return count
  
word = MyString()
word.set_value("This is a string! It has three sentences. Right?")
print(word.count_sentences())
# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
    return "Hello, " + name + "!"

# Task 3: Calculator
def calc(val1, val2, operator = "multiply"):
    try: 
        if operator == "add":
            return val1 + val2
        elif operator == "divide":
          return val1 // val2
        elif operator == "multiply":
          return val1 * val2
        elif operator == "subtract":
          return val1 - val2
        elif operator == "modulo":
          return val1 % val2
        else:
           return "Operator not supported."
    except ZeroDivisionError:
       return "You can't divide by 0!"
    except TypeError:
       return "You can't multiply those values!"

# Task 4: Data Type Conversion
def data_type_conversion(val, type):
    try:
       if isinstance(val, str) and type == "int":
          return int(val)
       if isinstance(val, str) and type == "float":
          return float(val)
       if isinstance(val, int) and type == "float":
          return float(val)
       if isinstance(val, int) and type == "str":
          return str(val)
       if isinstance(val, float) and type == "int":
          return int(val)
       if isinstance(val, float) and type == "str":
          return str(val)
    except ValueError:
       return f"You can't convert {val} into a {type}."

# Task 5: Grading System, Using *args
def grade(*args):
   try:
      average = sum(args) / len(args)
      if average >= 90:
         return "A"
      elif 80 <= average < 90:
         return "B"
      elif 70 <= average < 80:
         return "C"
      elif 60 <= average < 70:
         return "D"
      else:
         return "F"
   except TypeError:
      return "Invalid data was provided."
   
# Task 6: Use a For Loop with a Range
def repeat(string, count):
   try:
    repeat_phrase = ""
    for _ in range(count):
       repeat_phrase += string
    return repeat_phrase
   except TypeError:
    return "Invalid data type was provided."

# Task 7: Student Scores, Using **kwargs
def student_scores(param, **kwargs):
    try: 
        for key, value in kwargs.items():
            if param == "mean":
                average = sum(kwargs.values()) / len(kwargs.values())
                return average
            elif param == "best":
                max_scorer = max(kwargs.keys(), key = lambda s: kwargs[s])
                return max_scorer
    except TypeError:
       return "Invalid data type was provided."

# Task 8: Titleize, with String and List Operations
def titleize(str):
   try:
    words = str.split()
    capitalized_words = []
    for i, word in enumerate(words):
      if words[i] == words[0]:
       capitalized_words.append(word.capitalize())
      elif words[i] == words[-1]:
        capitalized_words.append(word.capitalize())
      elif words[i] != words[0] and words[i] != words[-1] and words[i] not in ("a", "on", "an", "the", "of", "and", "is", "in"):
       capitalized_words.append(word.capitalize())
      elif words[i] != words[0] and words[i] != words[-1] and words[i] in ("a", "on", "an", "the", "of", "and", "is", "in"):
       capitalized_words.append(word)
      result = " ".join(capitalized_words)  
    return result
   except TypeError:
      return "Invalid data type was provided."

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
   try:
    guess_letters = list(guess)
    secret_letters = list(secret)
    correct_guess = []
    for i, letter in enumerate(secret_letters):
      if secret_letters[i] in guess_letters:
       correct_guess.append(secret_letters[i])
      elif secret_letters[i] not in guess_letters:
       correct_guess.append("_")
      result = "".join(correct_guess)  
    return result
   except TypeError:
    return "Invalid data type was provided."

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(str):
    try:
     pig_latin_phrase = []
     words = str.split()
     for word in words:
       i = 0
       pig_latin_list = ""
       while len(word) > i:
          if word[i: i + 2] == "qu":
             pig_latin_list += "qu"
             i += 2
          elif word[i] not in ('aeiou'):
             pig_latin_list += word[i]
             i += 1
          else:
             break
       other_part_of_word = word[i:]
       pig_latin_phrase.append(other_part_of_word + pig_latin_list + 'ay')
     result = " ".join(pig_latin_phrase)
     return result
    except TypeError:
       return "Invalid data type was provided."
    

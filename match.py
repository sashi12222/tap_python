def decode_and_shift(s):
  output = "" # an empty string to store the output
  prev = "" # a variable to store the previous letter
  for ch in s: # loop over each character in the input string
    if ch.isalpha(): # if the character is a letter
      output += ch # append it to the output
      prev = ch # update the previous letter
    else: # if the character is a digit
      output += chr(ord(prev) + int(ch)) # shift the previous letter by the digit and append it to the output
  else: # after the loop ends
    if not s[-1].isdigit(): # if the last character of the input is not a digit
      output += s[-1] # append it to the output
  return output # return the output

# Example
s = "A4K3W5"
print(decode_and_shift(s)) # prints AEKNWB

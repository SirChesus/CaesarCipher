class EncryptionCode():

  def __init__(self, string, shift, proper, password):
    self.string = string
    self.shift = shift
    self.proper = proper
    self.password = password
#-------------------------------------------------------------------------------
  def get_isProper(self):
    return self.proper

  def set_isProper(self, p):
    self.proper = p
#-------------------------------------------------------------------------------
  def caesarBasic(self, string, shift):
    if self.get_isProper:
      joint = ''
      for letter in range(len(string)):
        ascii = ord(string[letter:letter+1].lower())
        ascii = (shift + ascii) % 122
        joint += ''.join(chr(ascii))
    else:
      return 'Improper!'

    return str(joint)
#-------------------------------------------------------------------------------
  def caesarAdv(self, string, shift):
    cipher2 = {'a': 'ఝ', 'b': 'ఈ', 'c': 'ఞ', 'd': 'న', 'e': 'ఠ', 'f': 'ౡ', 'g': 'భ',
                'h': 'శ', 'i': 'ౙ', 'j': 'క', 'k': 'ఊ', 'l': 'ణ', 'm': 'ప', 'n': 'మ',
                'o': 'జై', 'p': 'హా', 'q': 'లో', 'r': 'రు', 's': 'ఓం', 't': 'ౘ', 'u':'ఓ' ,
                'v': 'ట్టే', 'w': 'లు', 'x': 'పొ', 'y': 'గ్రా', 'z': 'బొ'}

    if self.get_isProper:
      joint = ''
      for letter in range(len(string)):
        ascii = ord(string[letter:letter+1].lower())
        ascii = (shift + ascii) % 122
        joint += ''.join(cipher2[chr(ascii)])

    else:
      return 'Improper!'

    return str(joint)
#-------------------------------------------------------------------------------
  def keyBasic(self, string, shift, password):
      if password == 'sleepy':
        joint = ''
        for letter in range(len(string)):
          ascii = ord(string[letter:letter+1].lower())
          ascii = (ascii - shift) % 122
          joint += ''.join(chr(ascii))

      else:
        return "Wrong password"

      return str(joint)
#-------------------------------------------------------------------------------
  def keyAdv(self, string, shift, password):
    cipher2 = {'a': 'ఝ', 'b': 'ఈ', 'c': 'ఞ', 'd': 'న', 'e': 'ఠ', 'f': 'ౡ', 'g': 'భ',
            'h': 'శ', 'i': 'ౙ', 'j': 'క', 'k': 'ఊ', 'l': 'ణ', 'm': 'ప', 'n': 'మ',
            'o': 'జై', 'p': 'హా', 'q': 'లో', 'r': 'రు', 's': 'ఓం', 't': 'ౘ', 'u':'ఓ' ,
            'v': 'ట్టే', 'w': 'లు', 'x': 'పొ', 'y': 'గ్రా', 'z': 'బొ'}

    if password == 'sleepy':
      joint = ''
      telToEng = ''
      for letter in range(len(string)+1):
        for eng, tel in cipher2.items():
          if tel == string[letter:letter+1]:
            telToEng = eng
            break
        ascii = ord(telToEng)
        ascii = (ascii - shift) % 122
        joint += ''.join(chr(ascii))

    else:
      return "Wrong password"

    return str(joint)
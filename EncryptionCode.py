class EncryptionCode():

  def __init__(self, string, shift, proper, password):
    self.string = string
    self.shift = shift
    self.proper = proper
    self.password = password
    self.cipher2 = {'a': 'ఝ', 'b': 'ఈ', 'c': 'ఞ', 'd': 'న', 'e': 'ఠ', 'f': 'ౡ', 'g': 'భ',
            'h': 'శ', 'i': 'ౙ', 'j': 'క', 'k': 'ఊ', 'l': 'ణ', 'm': 'ప', 'n': 'మ',
            'o': 'జై', 'p': 'హా', 'q': 'లో', 'r': 'రు', 's': 'ఓం', 't': 'ౘ', 'u':'ఓ' ,
            'v': 'ట్టే', 'w': 'లు', 'x': 'పొ', 'y': 'గ్రా', 'z': 'బొ'}
#-------------------------------------------------------------------------------
  def get_isProper(self):
    return self.proper

  def set_isProper(self, p):
    self.proper = p
#-------------------------------------------------------------------------------
  def caesarBasic(self, string, shift):
    if self.get_isProper:
      joint = ''
      for letter in string:
        ascii = ord(letter.lower())
        ascii = (shift + ascii) % 122
        joint += ''.join(chr(ascii))
    else:
      return 'Improper!'

    return str(joint)
#-------------------------------------------------------------------------------
  def caesarAdv(self, string, shift):
    if self.get_isProper:
      joint = ''
      for letter in string:
        ascii = ord(letter.lower())
        ascii = (shift + ascii) % 122
        joint += ''.join(self.cipher2[chr(ascii)])

    else:
      return 'Improper!'

    return str(joint)
#-------------------------------------------------------------------------------
  def keyBasic(self, string, shift, password):
      if password == 'sleepy':
        joint = ''
        for letter in string:
          ascii = ord(letter.lower())
          ascii = (ascii - shift) % 122
          joint += ''.join(chr(ascii))

      else:
        return "Wrong password"

      return str(joint)
#-------------------------------------------------------------------------------
  def keyAdv(self, string, shift, password):
    if password == 'sleepy':
      joint = ''
      telToEng = ''

      for letter in string:
        for eng, tel in self.cipher2.items():
          if tel == letter:
            telToEng = eng
            break
        ascii = ord(telToEng)
        ascii = (ascii - shift) % 122
        joint += ''.join(chr(ascii))

    else:
      return "Wrong password"

    return str(joint)
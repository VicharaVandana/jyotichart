

signs = [ "Aries",       "Taurus",    "Gemini",   "Cancer",
          "Leo",         "Virgo",     "Libra",    "Scorpio",
          "Saggitarius", "Capricorn", "Aquarius", "Pisces"
        ]

signnum = lambda signstr: signs.index(signstr) + 1

def compute_nthsignnum(fromsignnum, n):
    s = (fromsignnum + n - 1) % 12
    if (s == 0):
        s = 12
    return (s)

def compute_nthsignnum_backwards(fromsignnum, n):
    s =  (12 + fromsignnum - n + 1) % 12
    if (s == 0):
        s = 12
    return (s)

def housediff(fromsign, tosign):
  ''' Computes how many houses is difference between from fromsign to tosign
      This function is used to compute housenumber for planets too '''
  if(tosign > fromsign):
    house = tosign - fromsign + 1
  elif(tosign < fromsign):
    house = 12 + tosign - fromsign + 1
  else: #same signs
    house = 1 #first house
  return house

def get_housenumofsign(sign,ascendantsign):
    ascendant_signnum = signnum(ascendantsign)
    focus_signnum = signnum(sign)
    housenum = housediff(ascendant_signnum,focus_signnum)
    return(housenum)

def get_signofsign(housenum, ascendantsign):
  ascendant_signnum = signnum(ascendantsign)
  focus_signnum = compute_nthsignnum(ascendant_signnum,housenum)
  return(signs[focus_signnum-1])



if __name__ == '__main__':
    pos = get_signofsign(13, "Scorpio")
    print(pos)




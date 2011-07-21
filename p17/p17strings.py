lower = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
    10:'ten', 11:'eleven', 12:'twelve'}
teens = { 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
    17:'seventeen', 18:'eighteen', 19:'nineteen'}
upper = { 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety' }

def say_lower(n):
    if n == 0: return ''
    if n < 100:
        if n in lower:
            return lower[n]
        if n in teens:
            return teens[n]
        if n in upper:
            return upper[n]
        else:
            ones = n % 10
            tens = n - ones
            return upper[tens] + '-' + lower[ones]

def make_string(thousands, hundreds, lower):
    text = ''
    if thousands:
        pref = say_lower(thousands)
        text += pref + ' thousand'
        if hundreds or lower: text += ' '
    if hundreds:
        pref = say_lower(hundreds)
        text += pref + ' hundred '
    if lower:
        pref = say_lower(lower)
        if hundreds or thousands:
            text += 'and '
        text += pref
    return text

def get_values(n):
    lower = n % 10**2
    hundreds = ((n - lower) % 10**3) / 10**2
    thousands = (n - hundreds - lower) / 10**3
    return (thousands, hundreds, lower)

def say(n):
    (t, h, l) = get_values(n)
    return make_string(t,h,l)
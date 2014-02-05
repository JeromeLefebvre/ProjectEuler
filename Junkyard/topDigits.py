

def is_pandigital(n):
	return set(str(n)) == {'1','2','3','4','5','6','7','8','9'}
 

def top_digits(n):
# t = n * log10(phi)          + log10(1/sqrt(5))
  t = n * 0.20898764024997873 + (-0.3494850021680094)
  t = int((pow(10, t - int(t) + 8)))
  return t
 
fn, f0, f1 = 2, 1, 1
while not is_pandigital(f1) or not is_pandigital(top_digits(fn)):
 f0, f1 = f1, (f1+f0)%10**9
 fn += 1
print "Answer to PE104 = ", fn
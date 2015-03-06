#Karp-Rabin Algorithm for String Matching

#"text" and "pattern" are lists of digits for simplicity
#We perform matching by comparing patterns of digits modulo the prime
#We create a speed-up by comparing the modulus

def karp_rabin(text,pattern,prime):
    pattern_number=[x*(10**(len(pattern)-1-digit)) for digit,x in enumerate(pattern)]
    pattern_number=sum(pattern_number)
    pattern_mod=pattern_number%prime

    
    ts=[0]+text[0:len(pattern)-1]
    ts=[x*(10**(len(pattern)-1-digit)) for digit,x in enumerate(ts)]
    ts=sum(ts)

    for i in range(-1,len(text)-len(pattern)):
        ts=(ts*10+text[i+len(pattern)])%(10**len(pattern))
        ts_mod=ts%prime
        if ts_mod==pattern_mod: #We first compare the modulus
            if ts==pattern_number: #We then compare the numbers to eliminate spurious hits
                print "Pattern occurs at shift",i+1

        
        
karp_rabin([2,3,5,3,2,5,6,4,2,3,3,2,9,4,5,4,2],[2,9,4,5],5)
print
karp_rabin([2,3,5,3,2,5,6,4,2,3,3,2,9,4,5,4,2,4,3,2,4,1,8,7,2,5,2,3],[3],5)

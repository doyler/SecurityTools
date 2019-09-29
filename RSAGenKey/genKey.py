#!/usr/bin/python

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def main():
    p = 275778021469467750604832321873164071587  # edit with factor #1
    q = 291309854232898176366046870573797527117  # edit with factor #2
    n = 80336855234907714168477675917972994189398342031083238074132216291031761724679  # edit with modulus
    e = 65537  # edit if exponent is different

    phi = (p -1)*(q-1)
    d = modinv(e,phi)
    dp = modinv(e,(p-1))
    dq = modinv(e,(q-1))
    qi = modinv(q,p)

    print "asn1=SEQUENCE:rsa_key"
    print ""
    print "[rsa_key]"
    print "version=INTEGER:0"
    print "modulus=INTEGER:" + str(n)
    print "pubExp=INTEGER:" + str(e)
    print "privExp=INTEGER:" + str(d)
    print "p=INTEGER:" + str(p)
    print "q=INTEGER:" + str(q)
    print "e1=INTEGER:" + str(dp)
    print "e2=INTEGER:" + str(dq)
    print "coeff=INTEGER:" + str(qi)

if __name__ == "__main__":
    main()

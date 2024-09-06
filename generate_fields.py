import random
import collections

# Finds the GCD of two numbers

def find_gcd(a,b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a==0 and b == 0:
        print("GCD Careful!")
        return 0
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        temp = a
        a = b
        b = temp
    return(find_gcd(b%a,a))


# Returns a list of prime factors of an integer with multiplicity

def return_prime_factors(a):
    primes = []
    if a < 0:
        a = -1*a
    if a == 0:
        print("Error: 0 is divisible by every prime")
        return(0)
    if a == 1:
        return []
    primes = []
    while a>1:
        for p in range(2,a+1):
            if a%p == 0:
                primes.append(p)
                a = a//p
                break
    return primes



def return_ad(ak, am, dk, dm):
    return ak*am**2, dk*dm**2


# Given an integer a, it returns ak and am so that a = ak*am^2, and ak is squarefree

def return_akam(a):
    ak = 1
    am = 1
    prime_list = collections.Counter(return_prime_factors(a)).most_common()
    while (prime_list != []):
        tuple = prime_list.pop()
        if tuple[1]%2 == 0:
            am = am*tuple[0]**(tuple[1]//2)
        else:
            am = am*tuple[0]**(tuple[1]//2)
            ak = ak*tuple[0]
    return ak,am



# _______________ Checking sufficient ramification _____________________


# Checks if a binary cubic form is left sufficiently ramified at a prime p (dividing a)

def left_suff_ram_at_p(a,b,c,d,p):
    if ((b%p == 0) and (c%p == 0)):
        return 1
    if b%p == 0:
        return 0
    if ((c**2-4*b*d)%p == 0):
        return 1
    return 0

# Checks if a binary cubic form is left sufficiently ramified

def check_left_suff_ram(a,b,c,d):
    ak, am = return_akam(a)
    list_of_primes = return_prime_factors(ak)
    for p in list_of_primes:
        if left_suff_ram_at_p(a,b,c,d,p) == 0:
            return 0
    return 1

# Checks if a binary cubic form is right sufficiently ramified
            
def check_right_suff_ram(a,b,c,d):
    return check_left_suff_ram(d,c,b,a)

# returns the total amount of sufficient ramification (0, 1, or 2)

def return_total_suff_ram(a,b,c,d):
    return check_right_suff_ram+check_left_suff_ram


#_____________________ Checking the 2-adic obstruction to the existance of delta-distinguished orbits ___________________

delta_dict1 = {
    '1100': [[1,1]],
    '1101': [[1,3]],
    '1110': [[3,1]],
    '1111': [[0,0],[1,2],[2,1]],
    '1300': [[3,1]],
    '1301': [[3,3]],
    '1310': [[1,1]],
    '1311': [[0,0],[3,2],[2,1]],
    '3100': [[1,3]],
    '3101': [[3,3]],
    '3110': [[1,1]],
    '3111': [[0,0],[2,3],[1,2]],
    '3300': [[3,3]],
    '3301': [[3,1]],
    '3310': [[1,3]],
    '3311': [[0,0],[2,3],[3,2]]
}


delta_dict2 = {
    '1210': [[0,1],[4,1]],
    '1610': [[0,1],[4,1]],
    '3210': [[0,3],[4,3]],
    '3610': [[0,3],[4,3]],
    '5210': [[0,5],[4,5]],
    '5610': [[0,5],[4,5]],
    '7210': [[0,7],[4,7]],
    '7610': [[0,7],[4,7]],
    '1211': [[0,0],[2,4],[2,1],[4,4],[6,0],[6,1]],
    '1611': [[0,0],[2,0],[2,1],[4,4],[6,4],[6,1]],
    '3211': [[0,0],[2,4],[2,3],[4,4],[6,0],[6,3]],
    '3611': [[0,0],[2,0],[2,3],[4,4],[6,4],[6,3]],
    '5211': [[0,0],[2,4],[2,5],[4,4],[6,0],[6,5]],
    '5611': [[0,0],[2,0],[2,5],[4,4],[6,4],[6,5]],
    '7211': [[0,0],[2,4],[2,7],[4,4],[6,0],[6,7]],
    '7611': [[0,0],[2,0],[2,7],[4,4],[6,4],[6,7]]
}


def key_from_values(ak,dk,am,dm):
    return str(ak)+str(dk)+str(am)+str(dm)

def does_delta_exist(a,b,c,d):
    ak, am = return_akam(a)
    dk, dm = return_akam(d)
    if (find_gcd(ak,d) > 1):
        return 0
    if (find_gcd(dk,a) > 1):
        return 0
    if (((b**2-4*a*c)%dk) != 0):
        return 0
    if (((c**2-4*b*d)%ak) != 0):
        return 0
    if ((ak*dk)%2 != 0):
        ak = ak%2
        dk = dk%2
        am = am%2
        dm = dm%2        
        b = b%4
        c = c%4
        if ([b,c] in delta_dict1[key_from_values(ak,dk,am,dm)]):
            return 1
        return 0
    if ak%2 == 0:
        return does_delta_exist(d,c,b,a)
    ak = ak%8
    dk = dk%8
    am = am%2
    dm = dm%2
    b = b%8
    c = c%8
    if ([b,c] in delta_dict2[key_from_values(ak,dk,am,dm)]):
        return 1
    return 0


#________________________ Getting the infinite splitting type of the delta-distinguished orbit ___________________


def disc(a,b,c,d):
    return b**2*c**2 - 4*a*c**3 -4*b**3*d -27*a**2*d**2 + 18*a*b*c*d

def disc_sign(a,b,c,d):
    disc1 = disc(a,b,c,d)
    if disc1 == 0:
        return 0
    if disc1 > 0:
        return 1
    return -1

def delta_split_at_inf(a,b,c,d):
    disc_sgn = disc_sign(a,b,c,d)
    if disc_sgn == 0:
        print("Error at delta_split_at_inf: form has disc 0")
    if disc_sgn == -1:
        return 1
    if ((b > 0) and (c > 0)):
        return 1
    return 0


#___________________ Defining the buckets, and the function which randomly fills the buckets ___________________

buckets = ['neg_0SR_0DD2_1DDinf','neg_1SR_0DD2_1DDinf','neg_2SR_0DD2_1DDinf',
           'neg_0SR_1DD2_1DDinf','neg_1SR_1DD2_1DDinf','neg_2SR_1DD2_1DDinf',
           'pos_0SR_0DD2_0DDinf','pos_1SR_0DD2_0DDinf','pos_2SR_0DD2_0DDinf',
           'pos_0SR_1DD2_0DDinf','pos_1SR_1DD2_0DDinf','pos_2SR_1DD2_0DDinf',
           'pos_0SR_0DD2_1DDinf','pos_1SR_0DD2_1DDinf','pos_2SR_0DD2_1DDinf',
           'pos_0SR_1DD2_1DDinf','pos_1SR_1DD2_1DDinf','pos_2SR_1DD2_1DDinf',]


def chi_ad(a,d):
    ak, am = return_akam(a)
    dk, dm = return_akam(d)
    if find_gcd(ak,dk) == 1:
        return 1.0
    return 0.0

def average_prediction(str1,a,d):
    starr = str1.split('_')
    chiad = chi_ad(a,d)
    first_term = 0.0
    second_term = 0.0
    third_term = 0.0 + int(starr[2][0])*int(starr[3][0])
    if starr[1][0] == '0':
        st = 0.0
    elif starr[1][0] == '1':
        st = 1.0
    elif starr[1][0] == '2':
        st = 2.0+chiad
    if starr[0] == 'neg':
        first_term = 1.5
        second_term = st/2
    if starr[0] == 'pos':
        first_term = 1.25
        second_term = st/4
    return(first_term+second_term+third_term)

for str1 in buckets:
    print(str1, average_prediction(str1,1,1))


def abcd_to_bucket(a,b,c,d):
    ds = disc_sign(a,b,c,d)
    if ds == 0:
        print("Error at abcd_to_bucket: form has disc 0")
        return 0
    elif ds == 1:
        ans = 'pos_'
    else:
        ans = 'neg_'
    sr = check_left_suff_ram(a,b,c,d) + check_right_suff_ram(a,b,c,d)
    #print(sr)
    ans = ans + str(sr) + 'SR_'
    ans = ans + str(does_delta_exist(a,b,c,d)) + 'DD2_'
    ans = ans + str(delta_split_at_inf(a,b,c,d)) + 'DDinf'
    return ans


list_of_dicts=[[dict.fromkeys(buckets,[]) for i in range(5)] for j in range(5)]

#print(list_of_dicts[0][2])



def generate_random_bc(N):
    b = random.randint(1,N)
    c = random.randint(1,N**2)
    sign_b = random.randint(0,1)
    sign_c = random.randint(0,1)
    b = b*(-1)**sign_b
    c = c*(-1)**sign_c
    return b,c


def fill_particular_bucket(a,d,bucket_name, number_needed, height,fname):
    f = open(fname,'x')
    current_count = 0
    list_of_bc = []
    while current_count < number_needed+1:
        b,c = generate_random_bc(height)
        if abcd_to_bucket(a,b,c,d) == bucket_name:
            current_count += 1
            list_of_bc.append([b,c])
            f.write(str(b)+' '+str(c)+'\n')
    return list_of_bc




# 11
fill_particular_bucket(1,1,'neg_2SR_0DD2_1DDinf',2000,10**5,'11_neg_2SR_0DD2_1DDinf')
fill_particular_bucket(1,1,'neg_2SR_1DD2_1DDinf',2000,10**5,'11_neg_2SR_1DD2_1DDinf')

fill_particular_bucket(1,1,'pos_2SR_0DD2_0DDinf',2000,10**5,'11_pos_2SR_0DD2_0DDinf')
fill_particular_bucket(1,1,'pos_2SR_0DD2_1DDinf',2000,10**5,'11_pos_2SR_0DD2_1DDinf')
fill_particular_bucket(1,1,'pos_2SR_1DD2_0DDinf',2000,10**5,'11_pos_2SR_1DD2_0DDinf')
fill_particular_bucket(1,1,'pos_2SR_1DD2_1DDinf',2000,10**5,'11_pos_2SR_1DD2_1DDinf')

# 12
# fill_particular_bucket(1,1,'neg_2SR_0DD2_1DDinf',2000,10**5,'11_neg_2SR_0DD2_1DDinf')
# fill_particular_bucket(1,1,'neg_2SR_1DD2_1DDinf',2000,10**5,'11_neg_2SR_1DD2_1DDinf')

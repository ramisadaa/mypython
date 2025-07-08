import os
import random


def rean():
    while True:
        os.system('cls')
        print ("*****************************************************\n\n")
        x = int (input( "enter your chice : "))
        y = x +1
        
        os.system('cls')

        print("**************       Random function       *********\n\n")
        print("\t\t          ", y , "\n\n")

        # 1. betavariate(alpha, beta)
        #    - Arabic: تُرجع رقمًا عشوائيًا موزعًا وفق توزيع بيتا.
        #    - English: Returns a random number distributed according to the Beta distribution.
        #    - Inputs: alpha (float), beta (float)
        #    - Output: float
        if x == 0: 
            print(f"betavariate(1, 2): {random.betavariate(1, 2)}")

        # 2. choice(seq)
        #    - Arabic: تُرجع عنصرًا عشوائيًا من تسلسل معين.
        #    - English: Returns a random element from a given sequence.
        #    - Inputs: seq (sequence)
        #    - Output: element from seq
        elif x == 1:
            print(f"choice([1, 2, 3, 4]): {random.choice([1, 2, 3, 4])}")

        # 3. choices(population, weights=None, *, cum_weights=None, k=1)
        #    - Arabic: تُرجع قائمة من العناصر العشوائية مع إمكانية تحديد الأوزان.
        #    - English: Returns a list of random elements with optional weights.
        #    - Inputs: population (sequence), weights (list), cum_weights (list), k (int)
        #    - Output: list
        elif x == 2: 
            print(f"choices([1, 2, 3, 4], k=2): {random.choices([1, 2, 3, 4], k=2)}")

        # 4. expovariate(lambd)
        #    - Arabic: تُرجع رقمًا عشوائيًا موزعًا وفق توزيع أسي.
        #    - English: Returns a random number distributed according to the exponential distribution.
        #    - Inputs: lambd (float)
        #    - Output: float
        elif x ==3 :
            print(f"expovariate(1.5): {random.expovariate(1.5)}")

        # 5. gammavariate(alpha, beta)
        #    - Arabic: تُرجع رقمًا عشوائيًا موزعًا وفق توزيع جاما.
        #    - English: Returns a random number distributed according to the Gamma distribution.
        #    - Inputs: alpha (float), beta (float)
        #    - Output: float
        elif x == 4:
            print(f"gammavariate(1, 2): {random.gammavariate(1, 2)}")

        # 6. gauss(mu, sigma)
        #    - Arabic: تُرجع رقمًا عشوائيًا موزعًا وفق توزيع جاوس (طبيعي).
        #    - English: Returns a random number distributed according to the Gaussian distribution.
        #    - Inputs: mu (float), sigma (float)
        #    - Output: float
        elif x == 5:
            print(f"gauss(0, 1): {random.gauss(0, 1)}")

        # 7. getrandbits(k)
        #    - Arabic: تُرجع عددًا صحيحًا عشوائيًا بطول k بت.
        #    - English: Returns a random integer with k random bits.
        #    - Inputs: k (int)
        #    - Output: int
        elif x == 6:
            print(f"getrandbits(8): {random.getrandbits(8)}")

        # 8. getstate()
        #    - Arabic: تُرجع الحالة الحالية لمولد الأرقام العشوائية.
        #    - English: Returns the current internal state of the random number generator.
        #    - Inputs: None
        #    - Output: state object
        elif x ==7:
            print(f"getstate(): {random.getstate()}")

        # 9. randint(a, b)
        #    - Arabic: تُرجع عددًا صحيحًا عشوائيًا بين a و b (شامل).
        #    - English: Returns a random integer between a and b (inclusive).
        #    - Inputs: a (int), b (int)
        #    - Output: int
        elif x ==8:
            print(f"randint(1, 10): {random.randint(1, 10)}")

        # 10. random()
        #     - Arabic: تُرجع رقمًا عشوائيًا بين 0 و 1.
        #     - English: Returns a random float between 0 and 1.
        #     - Inputs: None
        #     - Output: float
        elif x ==9:
            print(f"random(): {random.random()}")

        # 11. randrange(start, stop[, step])
        #     - Arabic: تُرجع عددًا صحيحًا عشوائيًا من نطاق معين.
        #     - English: Returns a random integer from a specified range.
        #     - Inputs: start (int), stop (int), step (int, optional)
        #     - Output: int
        elif x ==10:
            print(f"randrange(1, 10, 2): {random.randrange(1, 10, 2)}")

        # 12. sample(population, k)
        #     - Arabic: تُرجع عينة عشوائية من العناصر بدون تكرار.
        #     - English: Returns a random sample of elements without replacement.
        #     - Inputs: population (sequence), k (int)
        #     - Output: list
        elif x ==11:
            print(f"sample([1, 2, 3, 4, 5], 3): {random.sample([1, 2, 3, 4, 5], 3)}")

        # 13. seed(a=None, version=2)
        #     - Arabic: تُهيئ مولد الأرقام العشوائية بقيمة معينة.
        #     - English: Initializes the random number generator with a seed value.
        #     - Inputs: a (int, optional), version (int)
        #     - Output: None

        elif x ==12:
            random.seed(42)
            print("seed(42): Random generator initialized.")

        # 14. setstate(state)
        #     - Arabic: تُعيّن الحالة الحالية لمولد الأرقام العشوائية.
        #     - English: Sets the internal state of the random number generator.
        #     - Inputs: state (state object)
        #     - Output: None

        elif x ==13:
            state = random.getstate()
            random.setstate(state)
            print("setstate(state): Random generator state set.")

        # 15. shuffle(x[, random])
        #     - Arabic: تُعيد ترتيب العناصر في قائمة بشكل عشوائي.
        #     - English: Shuffles the elements in a list randomly.
        #     - Inputs: x (list), random (function, optional)
        #     - Output: None

        elif x ==14:
            x = [1, 2, 3, 4, 5]
            random.shuffle(x)
            print(f"shuffle([1, 2, 3, 4, 5]): {x}")

        # 16. triangular(low, high, mode)
        #     - Arabic: تُرجع رقمًا عشوائيًا موزعًا وفق توزيع مثلثي.
        #     - English: Returns a random number distributed according to the triangular distribution.
        #     - Inputs: low (float), high (float), mode (float)
        #     - Output: float
        elif x ==15:
            print(f"triangular(1, 10, 5): {random.triangular(1, 10, 5)}")

        # 17. uniform(a, b)
        #     - Arabic: تُرجع رقمًا عشوائيًا موزعًا بالتساوي بين a و b.
        #     - English: Returns a random float uniformly distributed between a and b.
        #     - Inputs: a (float), b (float)
        #     - Output: float
        elif x ==16:
            print(f"uniform(1, 10): {random.uniform(1, 10)}")

        # 18. vonmisesvariate(mu, kappa)
        #     - Arabic: تُرجع رقمًا عشوائيًا موزعًا وفق توزيع فون ميزس.
        #     - English: Returns a random number distributed according to the von Mises distribution.
        #     - Inputs: mu (float), kappa (float)
        #     - Output: float
        elif x ==17:
            print(f"vonmisesvariate(0, 4): {random.vonmisesvariate(0, 4)}")

        # 19. weibullvariate(alpha, beta)
        #     - Arabic: تُرجع رقمًا عشوائيًا موزعًا وفق توزيع ويبول.
        #     - English: Returns a random number distributed according to the Weibull distribution.
        #     - Inputs: alpha (float), beta (float)
        #     - Output: float
        elif x ==18:
            print(f"weibullvariate(1, 2): {random.weibullvariate(1, 2)}")
        elif x == -1:
            print ("good bye")
            break
        else:
            print("No valid function selected.")
        input()
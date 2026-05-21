print("1. Left Recursion")
print("2. Left Factoring")

choice = int(input("Enter choice: "))
non_terminal = input("Enter Non-Terminal: ")
n = int(input("Enter number of productions: "))

productions = []
for i in range(n):
    productions.append(input(f"Production {i+1}: "))

# ----------------- LEFT RECURSION -----------------
if choice == 1:
    alpha = []
    beta = []

    for prod in productions:
        if prod.startswith(non_terminal):
            alpha.append(prod[len(non_terminal):])
        else:
            beta.append(prod)

    if not alpha:
        print("No Left Recursion Found.")
    else:
        new_nt = non_terminal + "'"
        
        # সমাধান ১: যদি কোনো beta না থাকে, তবে একটি default ε (epsilon) ধরে নেওয়া ভালো
        if not beta:
            beta = ["ε"]

        print(f"\n{non_terminal} -> ", end="")
        for i, b in enumerate(beta):
            if i > 0:
                print(" | ", end="")
            # যদি b নিজেই ε হয়, তবে শুধু নতুন নন-টার্মিনাল বসবে
            if b == "ε":
                print(f"{new_nt}", end="")
            else:
                print(f"{b}{new_nt}", end="")
        print()

        print(f"{new_nt} -> ", end="")
        for i, a in enumerate(alpha):
            if i > 0:
                print(" | ", end="")
            print(f"{a}{new_nt}", end="")
        print(" | ε\n")

# ----------------- LEFT FACTORING -----------------
elif choice == 2:
    # সমাধান ২: পাইথনের os.path.commonprefix ব্যবহার করে নিখুঁতভাবে কমন অংশ বের করা
    import os
    prefix = os.path.commonprefix(productions)

    # যদি সবগুলোর মধ্যে কোনো মিল না পাওয়া যায়, তবে দেখতে হবে অন্তত ২টির মধ্যে মিল আছে কিনা
    if prefix == "":
        # জোড়ায় জোড়ায় চেক করে সবচেয়ে বড় কমন অংশটি খোঁজা
        best_prefix = ""
        for i in range(len(productions)):
            for j in range(i + 1, len(productions)):
                cp = os.path.commonprefix([productions[i], productions[j]])
                if len(cp) > len(best_prefix):
                    best_prefix = cp
        prefix = best_prefix

    if prefix == "":
        print("No Left Factoring Needed.")
    else:
        new_nt = non_terminal + "'"
        
        # যেগুলোর মধ্যে মিল আছে সেগুলোকে আলাদা করা, আর যেগুলোতে মিল নেই সেগুলোকে রাখা
        factored_prods = []
        remaining_prods = []
        
        for prod in productions:
            if prod.startswith(prefix):
                rem = prod[len(prefix):]
                factored_prods.append("ε" if rem == "" else rem)
            else:
                remaining_prods.append(prod)

        # আউটপুট প্রিন্ট করা
        print(f"\n{non_terminal} -> {prefix}{new_nt}", end="")
        for prod in remaining_prods:
            print(f" | {prod}", end="")
        print()

        print(f"{new_nt} -> ", end="")
        for i, rem in enumerate(factored_prods):
            if i > 0:
                print(" | ", end="")
            print(rem, end="")
        print("\n")

else:
    print("Invalid Choice")

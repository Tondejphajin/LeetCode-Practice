def buddyStrings(s: str, goal: str) -> bool:
    s = s.lower()
    goal = goal.lower()

    count_true = 0
    if len(s) != len(goal):
        return False
    else:
        for i in range(0,len(s)):
            print(s[i])
            for j in range(len(goal)-1,-1,-1):
                if s[i] == goal[j]:
                    count_true += 1
    
    if count_true == len(s) and count_true == len(goal):
        return True
    else:
        return False

if __name__ =="__main__":
    result = buddyStrings("qwertyu","uytrewq")
    print(result)
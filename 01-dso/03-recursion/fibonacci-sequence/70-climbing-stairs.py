def climbStairs(n: int) -> int:
    oneStep = 1
    twoSteps = 2
    stepArr = [oneStep, twoSteps]

    waysToClimb = 0
    for i in range(0, len(stepArr)):
        stairRemain = n

        while stairRemain != 0:
            if stairRemain == 0:
                waysToClimb += 1
            elif stairRemain - stepArr[i] < 0:
                toPositive = stepArr[i]
                for j in stepArr:
                    if stairRemain - j == 0:
                        i = j
                stairRemain += toPositive
            stairRemain = stairRemain - stepArr[i]
    return waysToClimb


print(climbStairs(3))

def bayes(probA, probB, probB_givenA):
    probA_giveB = (probB_givenA * probA) / probB
    return probA_giveB
    
prob = bayes(0.4, 0.5, 0.9)

print(f"Probability of A given B = {prob}")

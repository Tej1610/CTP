import torch

cost = torch.tensor([200, 400, 500, 300])
benefit = torch.tensor([30, 60, 70, 40])
plans = ["A", "B", "C", "D"]
budget = 1000

dp = torch.zeros(budget + 1)
selected = [[] for _ in range(budget + 1)]

for i in range(4):
    for b in range(budget, cost[i] - 1, -1):
        new_benefit = dp[b - cost[i]] + benefit[i]

        if new_benefit > dp[b]:
            dp[b] = new_benefit
            selected[b] = selected[b - cost[i]] + [plans[i]]

print("Selected Plans:", selected[budget])
print("Total Cost:", sum(cost[plans.index(p)] for p in selected[budget]).item())
print("Maximum Benefit:", dp[budget].item())

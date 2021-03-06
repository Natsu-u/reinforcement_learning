import numpy as np
import time
class Bandit:
    def __init__(self,arms=10):
        self.arms = arms
        self.rates = np.random.rand(arms) #0~1の乱数(一様分布)を引数個作り、ndarrayで返す

    def play(self, arm):
        rate = self.rates[arm]
        reward = rate > np.random.rand() #reward:bool型
        return int(reward) #int(Ture):1, int(False):0

class Agent:
    def __init__(self, epsilon, action_size=10): #action_size:選択できる行動の数
        self.epsilon = epsilon
        self.qs = np.zeros(action_size)
        self.ns = np.zeros(action_size)

    def update(self, action, reward):
        a, r = action, reward
        self.ns[a] += 1
        self.qs[a] += (r - self.qs[a]) / self.ns[a]

    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.qs))
        return np.argmax(self.qs)

runs = 2000
steps = 1000
# epsilon = 0.1
epsilons = [0.01, 0.1, 0.3]
all_rates0 = np.zeros((runs,steps)) #(2000,1000)の形状
all_rates1 = np.zeros((runs,steps))
all_rates2 = np.zeros((runs,steps))
all_rates_list = [all_rates0, all_rates1, all_rates2]
s = time.time()
for i,epsilon in enumerate(epsilons):
    # if epsilon == 0.01 or epsilon == 0.3:
    #     print("pass")
    #     continue
    for run in range(runs):
        bandit = Bandit()
        agent = Agent(epsilon)
        sum_r = 0
        # total_rewards = []
        rates = []
        for step in range(steps):
            action = agent.get_action() #行動を選ぶ
            reward = bandit.play(action) #選んだ行動でプレイし報酬を得る
            agent.update(action, reward) #行動と得た報酬から価値を推定
            sum_r += reward

            # total_rewards.append(sum_r)
            rates.append(sum_r / (step+1))
            print(f"\r{i} {run} {step}",end="")

        all_rates_list[i][run] = rates
print()
g = time.time()
print(f"{g-s}秒")
avg_rates0 = np.average(all_rates_list[0], axis=0)
avg_rates1 = np.average(all_rates_list[1], axis=0)
avg_rates2 = np.average(all_rates_list[2], axis=0)

import matplotlib.pyplot as plt

plt.ylabel("Rates")
plt.xlabel("Steps")
plt.plot(avg_rates0,label=0.01)
plt.plot(avg_rates1,label=0.1)
plt.plot(avg_rates2,label=0.3)
plt.legend()
plt.show()
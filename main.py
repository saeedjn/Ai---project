
import random

class GridWorld:
    def __init__(self,size=3):
        self.size = size
        self.start = (0,0)
        self.goal = (size - 1, size - 1)
        self.agent_pos = self.start
        self.reset()

    def reset(self):
        self.agent_pos = self.start
        return  self.agent_pos

    def step(self,act):
        x,y = self.agent_pos

        if act == "up":
            x = max(x - 1, 0)
        elif act == "down":
            x = min(x + 1, self.size - 1)
        elif act == "left":
            y = max(y - 1, 0)
        elif act == "right":
            y = min(y + 1, self.size - 1)

        self.agent_pos = (x,y)

        if self.agent_pos == self.goal:
            return self.agent_pos, 10, True
        else:
            return self.agent_pos, -1, False


    def render(self):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if (i, j) == self.agent_pos:
                    row += "A"
                elif (i, j) == self.goal:
                    row += "G"
                else:
                    row += " . "
            print(row)
        print()


env = GridWorld()
state = env.reset()
done = False

while not done:
    env.render()
    action = random.choice(["up", "down", "left", "right"])
    print("Action: ", action)
    state, reward, done = env.step(action)
    print("State: ", state, "Reward: ", reward, "Done: ", done)

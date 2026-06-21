import gym
import random

print("=== Lab 31: Introduction to Reinforcement Learning ===")

# --------------------------------------------------
# Task 1: RL Terminology
# --------------------------------------------------

print("\nBasic Reinforcement Learning Concepts")
print("Agent       : Learner or decision maker")
print("Environment : World where agent acts")
print("Reward      : Feedback received after action")

# --------------------------------------------------
# Task 2: Create FrozenLake Environment
# --------------------------------------------------

env = gym.make(
    "FrozenLake-v1",
    is_slippery=False
)

state = env.reset()

# Handle Gym version differences
if isinstance(state, tuple):
    state = state[0]

print("\nEnvironment Created Successfully")
print("Initial State:", state)

# --------------------------------------------------
# Task 3: Simulate Agent Actions
# --------------------------------------------------

print("\nRunning Agent for 5 Steps...\n")

total_reward = 0

action_names = {
    0: "LEFT",
    1: "DOWN",
    2: "RIGHT",
    3: "UP"
}

log_data = []

for step in range(5):

    action = env.action_space.sample()

    result = env.step(action)

    # Gym compatibility
    if len(result) == 5:
        new_state, reward, terminated, truncated, info = result
        done = terminated or truncated
    else:
        new_state, reward, done, info = result

    total_reward += reward

    print(
        f"Step {step+1}: "
        f"Action={action_names[action]}, "
        f"State={new_state}, "
        f"Reward={reward}, "
        f"Done={done}"
    )

    log_data.append(
        f"Step {step+1}: "
        f"Action={action_names[action]}, "
        f"State={new_state}, "
        f"Reward={reward}, "
        f"Done={done}"
    )

    if done:
        print("\nEpisode Finished")
        break

# --------------------------------------------------
# Save Report
# --------------------------------------------------

with open("agent_report.txt", "w") as file:

    file.write("Lab 31: Introduction to Reinforcement Learning\n\n")

    file.write("Environment: FrozenLake-v1\n")
    file.write("is_slippery=False\n\n")

    file.write("RL Concepts\n")
    file.write("Agent = Learner\n")
    file.write("Environment = FrozenLake\n")
    file.write("Reward = Feedback signal\n\n")

    file.write("Agent Actions Log\n")
    file.write("------------------\n")

    for row in log_data:
        file.write(row + "\n")

    file.write(f"\nTotal Reward: {total_reward}\n")

print("\nAgent report saved as agent_report.txt")

env.close()

print("\nLab completed successfully.")

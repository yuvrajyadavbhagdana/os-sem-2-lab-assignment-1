#✅ Task-wise Solution
#🔹 Task 1: Input System Data

# We take:

# Number of processes
# Number of resources
# Allocation Matrix
# Maximum Matrix
# Available Resources



# Banker's Algorithm Implementation

def calculate_need(max_matrix, allocation):
    need = []
    for i in range(len(max_matrix)):
        row = []
        for j in range(len(max_matrix[0])):
            row.append(max_matrix[i][j] - allocation[i][j])
        need.append(row)
    return need


def bankers_algorithm(processes, resources, allocation, max_matrix, available):
    need = calculate_need(max_matrix, allocation)

    print("\nNeed Matrix:")
    for i in range(len(need)):
        print(f"P{i}: {need[i]}")

    finish = [False] * processes
    safe_sequence = []
    work = available.copy()

    count = 0

    while count < processes:
        found = False

        for i in range(processes):
            if not finish[i]:
                # Check if need <= work
                if all(need[i][j] <= work[j] for j in range(resources)):

                    # Add allocated resources back to work
                    for j in range(resources):
                        work[j] += allocation[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    count += 1

        if not found:
            break

    if count == processes:
        print("\nSystem is in SAFE state.")
        print("Safe Sequence:", " -> ".join(f"P{i}" for i in safe_sequence))
    else:
        print("\nSystem is in UNSAFE state. Deadlock may occur.")


# ----------- INPUT -----------

processes = int(input("Enter number of processes: "))
resources = int(input("Enter number of resources: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(processes):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
max_matrix = []
for i in range(processes):
    row = list(map(int, input(f"P{i}: ").split()))
    max_matrix.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

# ----------- RUN -----------

bankers_algorithm(processes, resources, allocation, max_matrix, available)

import heapq

def min_steps_to_target_sweetness(candies, target_sweetness):
    # Convert candies to a min-heap
    heapq.heapify(candies)
    
    steps = 0

    while candies[0] < target_sweetness:
        # Extract the two least sweet candies
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)

        # Calculate the sweetness of the combined candy
        combined_sweetness = least_sweet + 2 * second_least_sweet

        # Add the combined candy back to the heap
        heapq.heappush(candies, combined_sweetness)

        # Increment the number of steps
        steps += 1

    return steps

# Input reading
target_sweetness = int(input().strip())
candies = list(map(int, input().strip().split()))

# Output the result
result = min_steps_to_target_sweetness(candies, target_sweetness)
print(result)
                                                                                                                            

# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
"""
Group 1: Ordered and Indexed
1. Rotate Right
Rotate the values in a collection to the right by k steps.
Input: [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
"""
def rotate_right(nums,k):
    if not nums:
        return[]
    k=k%len(nums)
    return nums[-k:]+nums[:-k]

print(rotate_right([1, 2, 3, 4, 5], 2))  #[4,5,1,2,3]
print(rotate_right([1], 3)) #[1]
print(rotate_right([], 1)) #[]

"""
For my timed challenge, I ultimately decided to go with the rotate right problem. I utilized a list as the primary data structure because list are ideal when you need to perserve order and access elements by index. With the problem I chose,
order is absolutely essential because rotation is ultimately dependent on keeping the sequence of elements. Slicing made it easy to quickly rearrange my list by combining the last k elements with the initial portion. With the 30 minute time limit,
I used Python's built in slicing as a crutch since it allowed me to skip the headache of working through a more complex algorithm. I knew from the resources provided that I read that it is very important for the data structure to match the scenario, 
and with that prior knowledge, the list became the clearest fit for this task as I was able to mess around with positions without making a custom structure. Resource 3 helped me understand something that does relate to the assignment, but also touches
on a broader point outside of it. Explaining my reasoning is just as important as actually solving the problem as that critical thinking and insight into why decisions were made not only gives more clarity on how a solution was acheived, but also helps
me reinforce the knowledge gained from the experience and really why the assignment was assigneed in the first place.
"""

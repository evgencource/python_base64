import base64
# Define an array of strings representing the steps in a software development lifecycle
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

# Loop through each step in the array and perform an operation
for step in steps:
    step_bytes = step.encode('utf-8')
    encoded_step = base64.b64encode(step_bytes)
    # Perform some operation related to the current step
    print(encoded_step)

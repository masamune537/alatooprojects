
user_info = {}
print("Enter your name:")
user_info["name"] = input()
print("Enter your age:")
user_info["age"] = int(input())

print("Enter your city:")
user_info["city"] = input() 

print("Enter your occupation:")
user_info["occupation"] = input() 

print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")

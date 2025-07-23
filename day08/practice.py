# Based on the article by Tim Urban - YOur life in weeks
# https://waitbutwhy.com/2014/05/life-weeks.html

def life_in_weeks(current_age):
    weeks_passed = current_age * 52
    total_weeks = 90*52
    weeks_left = total_weeks - weeks_passed
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(12)


#love score calculator:
#  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53

def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    for letter in name1:
        if letter in 'love' :
            love_count += 1
        if letter in 'true' :
            true_count += 1
            
    for letter in name2:
        if letter in 'love' :
            love_count += 1
        if letter in 'true' :
            true_count += 1
    print(f"{true_count}{love_count}")
            
            
calculate_love_score("Kanye West", "Kim Kardashian")
            
    
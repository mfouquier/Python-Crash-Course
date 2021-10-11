#Chapter 3 wrap up using Append Insert Delete Remove Pop Sort Sorted Reverse Length
teams = ['man city', 'chelsea', 'everton', 'tottenham']

#Print the List
print(teams)

#Add a team to the end of the list with APPEND
teams.append('liverpool')
print(teams)

#Insert a team at the 3rd position using INSERT
teams.insert(2, 'leichester')
print(teams)

#Delete a team using DEL
del teams [2]
print(teams)

#Remove a team by name using REMOVE
teams.remove('liverpool')
print(teams)

#Remove a team and use the value to send a message using POP
popped_team = teams.pop(2)
print(f"\nSorry {popped_team.title()}, but you have been relegated.")
print(teams)

#Put some teams back in to make list bigger
teams.append('liverpool')
teams.insert(3, 'watford')
print(teams)

#Temporarily sort alphabetically with SORTED and reverse
print("\n",sorted(teams))
print(sorted(teams, reverse = True))

#Use Reverse to permenantly change the list and then back to the original
teams.reverse()
print("\n",teams)
teams.reverse()
print(teams)

#Permanantly change list to alphabetical order with SORT and reverse
teams.sort()
print("\n",teams)
teams.sort(reverse = True)
print(teams)

#Show length of list with LEN
print("\n",len(teams))

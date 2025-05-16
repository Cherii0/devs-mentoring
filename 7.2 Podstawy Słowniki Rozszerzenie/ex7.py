lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}
union = lovers | friends  # new dictionary
lovers.update(friends) # modifies first dictionary

print(union)
print(lovers)

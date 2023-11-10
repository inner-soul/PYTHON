Companyname = "Manikchand's Corner"# Use of single quote in sentence.
Directorname = 'Manikchand "Jola wale" baba'# Use of double quote in sentence.
Location = '''Dadra nagar haveli,
Silvassa
Sarigam
3964500.
'''# Use of triple code.....
Address = Location[:]
print(Companyname[0]) 
# O/P - M
print(Companyname[-1])
# O/P - r
print(Companyname[-2])
# O/P - e
print(Companyname[0:3])
# O/P - Man (it won't consider 'I'.)
print(Companyname[0:])
# O/P - Manikchand's Corner
print(Companyname[1:])
# O/P - anikchand's Corner
print(Companyname[:6])
print(Directorname)
print(Address) # Fetched Location in address

print('Exercise >>>')
Fname = 'Jennifer'
print(Fname[1:-1])
# O/P - ennife

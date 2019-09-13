def listfun():
	veglist=['chilli','potato','radish']
	print('I have',len(veglist),'veg to purchase.')
	print('the veglist is', veglist)
	print('\n1 also have to buy potato.')
	veglist.append('potato')
	print('My veg list is now',veglist)
	print('I will sort my list now')
	veglist.sort()
	print('sorted veg list is',veglist)
	print('The first veg I will buy is',veglist[0])
	oldveg = veglist[0]
	print (veglist[0])
	print('I bought the', oldveg)
	del veglist[0]
	print('My veg list is now',veglist)
def tuplefun():
    forest=('elephant','lion','tiger')
    print('Number of animals in the forest is',len(forest))
    new_forest ='gorilla','giraffe',forest
    print('Number of ponds in the new forest is',len(new_forest))
    print('All animals in new forest are',new_forest)
    print('Animals came from old forest are',new_forest[1])
    print('last animal came from old forest is',new_forest[1][1])
    print('Number of animals in the new forest is',len(new_forest)-1+len(new_forest[1]))

listfun()
tuplefun()


def remove_from_not_done_list(arr1, num1):#function that removes the item done from not done list

	del(arr1[num1])#remove the selected item from the list of not done

	new_arr = arr1#create a new list of the remaining items

	return new_arr

def from_not_done_to_done(array1, number, array2):#function that updates the removed item from not done list into done list
	#print(number)
	#print(array1)
	#print(array2)

	selectedvalue = array1[number]#find the selected item

	array2[number] = selectedvalue #new list of done items

	done_arr = array2

	return done_arr

def progress(notdonelist, donelist):#gives out the progress of the user

	lengthofnotdone = len(notdonelist)#number of remaining items

	lengthofdoneitems = len(donelist)

	progress = ((lengthofdoneitems*100)//(lengthofdoneitems + lengthofnotdone))

	return progress


notdone = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
chosen = 2
listdone = {7:'t',5:'k'}
doneitems = from_not_done_to_done(notdone, chosen, listdone)

print(doneitems)
notdonelist1 = remove_from_not_done_list(notdone,chosen)

print(notdonelist1)



#progressobj = progress(notdone, {7:'t',5:'k'})

#print(progressobj)
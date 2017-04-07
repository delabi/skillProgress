
def remove_from_not_done_list(notdonelist, selected):#function that removes the item done from not done list

	del(notdonelist[selected])#remove the selected item from the list of not done

	new_notdonelist = notdonelist#create a new list of the remaining items

	return new_notdonelist

def from_not_done_to_done(notdonelist, selected, donelist):#function that updates the removed item from not done list into done list
	key = selected

	selectedvalue = notdonelist[key]#find the selected item

	donelist[selected] = selectedvalue #new list of done items

	done_items = donelist

	return done_items

def progress(notdonelist, donelist):#gives out the progress of the user

	lengthofnotdone = len(new_notdonelist)#number of remaining items

	lengthofdoneitems = len(done_items)

	progress = ((lengthofdoneitems*100)//(lengthofdoneitems + lengthofnotdone))

	return progress


notdonelist = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
selected1 = 4

notdonelist1 = remove_from_not_done_list(notdonelist,selected1)

print(notdonelist1)

doneitems = from_not_done_to_done(notdonelist,selected1,{7:'t'})

print(doneitems)

progressobj = progress(notdonelist1, doneitems)

print(progressobj)
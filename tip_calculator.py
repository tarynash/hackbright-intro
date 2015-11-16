def calculate_tip(total_bill):
	return 0.2*total_bill

def calculate_tip2(total_bill,tip_percent):
	return total_bill*tip_percent

def tips_with_friends(total_bill,tip_percent,num_friends):
	return (total_bill*tip_percent)/num_friends
print "Each person should pay %.2f." % tips_with_friends(42.50,.2,2)
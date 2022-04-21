import csv, time

with open('bank.csv', mode ='r') as source:								#open source csv
	vital_sign_data = csv.reader(source)

	for row in vital_sign_data:
		with open('sink2.txt', 'a') as f:								#open/create destination txt file
			f.writelines('\n')
			f.writelines(str(row).replace('[','').replace(']',''))		#write each row to sink
		#print(str(row).replace('[','').replace(']',''))
		time.sleep(1)													#delays writing next line by 1 sec (update frequency)
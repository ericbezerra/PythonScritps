## Author: Eric Bezerra
## Program: report.py
## Date: 03/01/2018
## Action: Create reports by wms system and
## send from email to clients

class ReportBot():
	hosts = []
	tasks = r'C:\Users\eric.bezerra\Documents\Scripts\tasks\hosts.xlsx'
	keys = ['eric.bezerra', 'Wancorp123#']

	def __init__(self):
		print('Bot Started...')

## Read name of hosts
	def readHosts(self):
		import openpyxl as xl

		wb = xl.load_workbook(self.tasks)
		sheet = wb.get_sheet_by_name('hosts')
		for i in range(1, sheet.max_row+1):
			self.hosts.append(sheet.cell(row=i, column=1).value)
				
## TODO: Colect Data from WMS and Files
## client = name of host
## start (list) = day, month, year, hour, minutes
## end (list) = day, month, year, hour, minutes
	def takeData(self, client, start, end):
		import requests as req
		link = 'http://10.130.254.10/wms/pnp4nagios/index.php/image?host='
		date = '&start='+str(start[1])+'%2F'+str(start[0])+'%2F'+str(start[2])+'+'+str(start[3])+'%3A'+str(start[4])+'+&end='+str(end[1])+'%2F'+str(end[0])+'%2F'+str(end[2])+'+'+str(end[3])+'%3A'+str(end[4])
		
		## TODO: INDISPONIBILIDADE GRAFICO

		## TODO: INTERFACES GRAFICO

		## TODO: MEMORY GRAFICO

		## MEMORY PNG
		image = req.get(link+client+date+'&srv=Mem_used_Processor&theme=multisite&baseurl=..%2Fcheck_mk%2F', auth=(self.keys[0], self.keys[1]))
		img = open('memory.png', 'wb')
		for chunk in image.iter_content(1000000):
			img.write(chunk)
		img.close()

		## TODO: PROCESSOR GRAFICO

		## PROCESSOR PNG
		image = req.get(link+client+date+'&srv=CPU_utilization&theme=multisite&baseurl=..%2Fcheck_mk%2F', auth=(self.keys[0], self.keys[1]))
		img = open('processor.png', 'wb')
		for chunk in image.iter_content(1000000):
			img.write(chunk)
		img.close()

		## ICMP FULL PNG
		image = req.get(link+client+date+'+&srv=_HOST_&view=1&source=0', auth=(self.keys[0], self.keys[1]))
		img = open('icmpfull.png', 'wb')
		for chunk in image.iter_content(1000000):
			img.write(chunk)
		img.close()

		## ICMP FIRST QUARTER PNG
		image = req.get(link+client+'&start='+str(start[1])+'%2F'+str(start[0])+'%2F'+str(start[2])+'+'+str(start[3])+'%3A'+str(start[4])+'+&end='+str(end[1])+'%2F'+str(end[0]-15)+'%2F'+str(end[2])+'+'+str(end[3])+'%3A'+str(end[4])+'+&srv=_HOST_&view=1&source=0', auth=(self.keys[0], self.keys[1]))
		img = open('icmpstart.png', 'wb')
		for chunk in image.iter_content(1000000):
			img.write(chunk)
		img.close()

		## ICMP LAST QUARTER PNG
		image = req.get(link+client+'&start='+str(start[1])+'%2F'+str(start[0]+15)+'%2F'+str(start[2])+'+'+str(start[3])+'%3A'+str(start[4])+'+&end='+str(end[1])+'%2F'+str(end[0])+'%2F'+str(end[2])+'+'+str(end[3])+'%3A'+str(end[4])+'+&srv=_HOST_&view=1&source=0', auth=(self.keys[0], self.keys[1]))
		img = open('icmpend.png', 'wb')
		for chunk in image.iter_content(1000000):
			img.write(chunk)
		img.close()

		## TODO: SERVICES CSV

		## TODO: TICKETS OPEN GRAFICO


## TODO: Create Word document


## TODO: Create PDF document

start = [1, 12, 2017, 00, 00]
end = [31, 12, 2017, 00, 00]
bot = ReportBot()
bot.readHosts()
bot.takeData(bot.hosts[0], start, end)
print('Bot Stoped.')
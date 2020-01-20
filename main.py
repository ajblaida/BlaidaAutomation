from ingest.ingest import ingest

userin = input("value\n")
while userin != "quit":
	ingest(userin.split())
	userin = input("value\n")
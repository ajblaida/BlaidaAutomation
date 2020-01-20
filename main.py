from lifecycle.ingest.ingest import ingest
from models.command import Command
import sys

command = Command(sys.argv[1:])
ingest(command)
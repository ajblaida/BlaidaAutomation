import sys
from outputs.lights import modify_lights
from help.help import help
from help.unknown import unknown

def ingest(arguments):
	zone = arguments[0]
	result = options.get(zone, unknown)(arguments)
	if (result < 0):
		unknown(arguments)

options = {
	"lights": modify_lights,
	"help": help,
}
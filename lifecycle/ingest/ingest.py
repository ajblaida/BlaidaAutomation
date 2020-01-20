import sys
from lifecycle.outputs.lights import modify_lights
from lifecycle.ingest.tooling.docs import helpdocs
from lifecycle.ingest.tooling.unknown import unknown


def ingest(command):
	result = options.get(command.zone, unknown)(command)
	if (result < 0):
		unknown(command)

options = {
	"lights": modify_lights,
	"help": helpdocs
}
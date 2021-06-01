#!/usr/bin/python3
import os
from mafia import Mafia

discordToken = os.environ['TOKEN']

m = Mafia()
m.run(discordToken)